from PySide6.QtWidgets import QLabel, QLineEdit, QWidget
from PySide6 import QtCore, QtGui
from PySide6.QtCore import QMargins, QRect, Qt, QPoint, QSize, Signal
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor, QGuiApplication, QImage, QPaintEvent, QPainter, QFont, QPen, QPixmap, QIcon

import tempfile
import requests
import os

try:
    from custom_widgets import AddPopUp
    from custom_widgets.ui import Ui_dataViewWidget, Ui_dataEntryCreator
    from functions import UIFunctions
    from model import Scholar, Account, DefaultTools

except ModuleNotFoundError:
    from src.custom_widgets import AddPopUp
    from src.custom_widgets.ui import Ui_dataViewWidget, Ui_dataEntryCreator
    from src.functions import UIFunctions
    from src.model import Scholar, Account, DefaultTools


class scholarsDataView(QWidget):

    # signals
    need_update_home = Signal(bool)

    def __init__(self, ) -> None:
        super(scholarsDataView, self).__init__()
        self.ui = Ui_dataViewWidget()
        self.ui.setupUi(self)
        self.func = UIFunctions()

        # properties
        self.width_default = 1131
        self.height_default = 540
        self.data_entry_info = []
        self.data_entry_widgets = []

        # variables
        self.actual_percent_screen = None
        self.default_height = 680
        self.current_height = self.height()
        self.scholars_db_handle = Scholar()
        self.account_db_handle = Account()

        # pages variables
        self.current_page = 1
        self.goto_page = 0
        self.receivers_count = 0

        # leaderboard variables
        self.leaderboard_widget = None

        # add pop_up
        self.pop_up = AddPopUp()
        self.pop_up.close_signal.connect(self.after_pop_up_handle)

        # configs
        self.font_configuration()
        self.btn_configuration()
        self.installEventFilter(self)

        # default init
        self.data_entry_creator()
        if len(self.data_entry_widgets) > 0:
            self.show_widgets_each_page(self.current_page, direction=None)
        self.set_leaderboard_ranks()

    def btn_configuration(self):
        self.ui.verticalLayout_10.setAlignment(Qt.AlignCenter)
        self.ui.addBtn.setText('Add')
        self.ui.addBtn.setMinimumSize(QSize(120, 25))
        self.ui.addBtn.setMaximumSize(QSize(120, 25))
        self.ui.addBtn.clicked.connect(self.pop_up_handle)

    def pop_up_handle(self):
        self.pop_up.show()

    def after_pop_up_handle(self):
        self.set_new_data()

        self.need_update_home.emit(True)
        
    def need_update_data_view(self, value):
        if value:
            self.set_new_data()

    def set_new_data(self):
        if len(self.data_entry_widgets) > 0:
            for widget in self.data_entry_widgets:
                widget._close_widget()

            self.data_entry_info = []
            self.data_entry_widgets = []

        self.data_entry_creator()
        self.show_widgets_each_page(self.current_page, direction=None)
        self.set_leaderboard_ranks()

    def set_leaderboard_ranks(self):

        if self.leaderboard_widget != None:
            for widgets in self.leaderboard_widget:
                widgets._close_widget()
                self.leaderboard_widget = None
        
        self.leaderboard_widget = []

        scholars_list = self.scholars_db_handle.get_all_scholars(
            DefaultTools.session_handle)

        if len(scholars_list) > 0:

            top_scholars = []

            for scholar in scholars_list:
                top_scholars.append(scholar.rank)

            top_scholars.sort()

            if len(top_scholars) > 3:
                top_scholars = top_scholars[:3]
            elif len(top_scholars) <= 3:
                top_scholars = top_scholars

            scholars_obj = self.scholars_db_handle.find_by_rank(DefaultTools.session_handle, top_scholars)

            id_list = [scholar.account_id for scholar in scholars_obj]
            images_list = self.account_db_handle.get_axie_image(DefaultTools.session_handle ,id_list)
            
            if len(top_scholars) == 3:
                
                for i in range(0, 3):
                    self.leaderboard_widget.append(RankLeaderboard(
                        image_url=images_list[i], name=scholars_obj[i].name, pos=i))
                
            else:

                for i in range(0, 3):

                    if i < len(top_scholars):
                        self.leaderboard_widget.append(RankLeaderboard(image_url=images_list[i], name=scholars_obj[i].name, pos=i))
                    else:
                        self.leaderboard_widget.append(RankLeaderboard(pos=i))
        else:
            # default theres no ranks
            for i in range(0, 3):
                self.leaderboard_widget.append(RankLeaderboard(pos=i))

        self.ui.verticalLayout_11.addWidget(self.leaderboard_widget[1])
        self.ui.verticalLayout_12.addWidget(self.leaderboard_widget[2])
        self.ui.verticalLayout_15.addWidget(self.leaderboard_widget[0])

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:

        if event.type() == QtCore.QEvent.Type.Resize:

            if self.ui.verticalLayout_15.contentsMargins() != QMargins(45, 0, 0, 30):
                self.ui.verticalLayout_15.setContentsMargins(45, 0, 0, 30)
                self.ui.verticalLayout_11.setContentsMargins(26, 0, 0, 13)
                self.ui.verticalLayout_12.setContentsMargins(26, 0, 0, 13)

            app_height = self.get_app_height()

            if app_height != self.current_height:
                self.set_max_height(default=False)
                self.current_height = app_height

        return super().eventFilter(watched, event)

    def get_height(self) -> int:

        try:
            app_height = self.get_app_height()
        except AttributeError:
            app_height = 680

        default_percent = (self.height_default / 680)

        height = default_percent * app_height

        return (int(height))

    def get_app_height(self) -> int:
        parent = self
        app_height = 680

        for i in range(0, 101):
            parent = parent.parent()

            if hasattr(parent, 'objectName'):

                name = parent.objectName()

                if name == 'MainWindow':
                    break
            else:
                break

            try:
                app_height = parent.height()
            except AttributeError:
                pass

        return app_height

    def get_number_pages(self, max_widgets) -> int:

        pages = len(self.data_entry_widgets) / max_widgets

        if type(pages) == float:
            dif = abs(pages - int(pages))

            if 0 < dif < 1:
                pages += 1

        if int(pages) > 1:

            was_blocked = self.ui.rigthBtn.signalsBlocked()

            self.ui.rigthBtn.blockSignals(was_blocked)

            if self.receivers_count == 0:
                self.ui.leftBtn.clicked.connect(self.previus_page)
                self.ui.rigthBtn.clicked.connect(self.next_page)
                self.receivers_count += 1

        return int(pages)

    def get_max_widgets(self, height) -> int:

        max_widgets = (height / 30) - 2

        return int(max_widgets)

    def get_data_info(self):

        scholars_list = Scholar.get_all_scholars(DefaultTools.session_handle)

        for scholar in scholars_list:
            self.data_entry_info.append({'name': scholar.name,
                                         'ronin': scholar.account.ronin_address,
                                         'mmr': str(scholar.mmr),
                                         'rank': str(scholar.rank),
                                         'total_acc_slp': str(scholar.total_acc_slp),
                                         'total_average_slp': str(scholar.total_average_slp),
                                         'daily_goal': str(scholar.daily_goal),
                                         'today_profit': str(scholar.daily_profit)})

    def set_max_height(self, default) -> int:
        if default:
            height = self.height_default
        else:
            height = self.get_height()

        self.setMaximumHeight(height)

        max_widgets = self.get_max_widgets(height)
        max_pages = self.get_number_pages(max_widgets)
        
        if max_pages == 0:
            self.current_page = 1
        elif self.current_page > max_pages:
            self.current_page = max_pages

        self.show_widgets_each_page(self.current_page, direction=None)

    def next_page(self):
        print('go_next')

        height = self.get_height()
        max_widgets = self.get_max_widgets(height)
        number_pages = self.get_number_pages(max_widgets)

        if self.current_page < number_pages:
            self.goto_page = self.current_page + 1
            self.show_widgets_each_page(self.goto_page, direction='right')

    def previus_page(self):
        print('go_back')

        height = self.get_height()
        max_widgets = self.get_max_widgets(height)
        number_pages = self.get_number_pages(max_widgets)

        if self.current_page > 1:
            self.goto_page = self.current_page - 1
            self.show_widgets_each_page(self.goto_page, direction='left')

    def show_widgets_each_page(self, goto_page, direction=None):

        height = self.get_height()
        max_widgets = self.get_max_widgets(height)
        number_pages = self.get_number_pages(max_widgets)
        total_widget = len(self.data_entry_widgets)
        
        # pos text correctly
        self.min_max_text()

        start_list = []

        if number_pages == 0:
            return

        if direction == 'left':
            # goto <-
            for i in range(0, number_pages):
                start_list.append(max_widgets * i)

            start_i = goto_page - 1
            end_i = goto_page

            start_clean_i = goto_page
            end_clean_i = goto_page + 1

            widget_width = self.width()

            visible_widgets = self.data_entry_widgets[start_list[start_clean_i]: start_list[end_clean_i]] \
                if goto_page != abs(number_pages-1) else \
                self.data_entry_widgets[start_list[start_clean_i]:]

            new_widgets = self.data_entry_widgets[start_list[start_i]:start_list[end_i]]

            for widget in visible_widgets:
                widget.close()
                
            for widget in new_widgets:
                if not widget.isVisible():
                    self.ui.layoutDataWidgets.addWidget(widget)
                    widget.show()

        elif direction == 'right':
            # goto ->
            # list dos indices de onde começar a mostrar os widgets
            for i in range(0, number_pages):
                start_list.append(max_widgets * i)

            start_i = goto_page - 1
            end_i = goto_page

            start_clean_i = goto_page - 2
            end_clean_i = goto_page - 1

            widget_width = self.width()

            visible_widgets = self.data_entry_widgets[start_list[start_clean_i]:start_list[end_clean_i]]
            new_widgets = self.data_entry_widgets[start_list[start_i]: start_list[end_i]] \
                if goto_page != number_pages else \
                self.data_entry_widgets[start_list[start_i]:]

            for widget in visible_widgets:
                widget.close()

            for widget in new_widgets:
                if not widget.isVisible():
                    self.ui.layoutDataWidgets.addWidget(widget)
                    widget.show()

        elif direction == None:

            for widget in self.data_entry_widgets:
                widget.close()
                widget.need_update_signal.connect(self.need_update_data_view)

            for i in range(0, number_pages):
                start_list.append(max_widgets * i)

            start_i = goto_page - 1
            end_i = goto_page

            new_widgets = self.data_entry_widgets[start_list[start_i]: start_list[end_i]] \
                if goto_page != number_pages else \
                self.data_entry_widgets[start_list[start_i]:]

            for widget in new_widgets:
                if not widget.isVisible():
                    widget.show()
                self.ui.layoutDataWidgets.addWidget(widget)

        self.ui.indiceLabel.setText(f'{goto_page}')
        self.current_page = goto_page

    def min_max_text(self):
        
        height = self.get_app_height()
        
        if len(self.data_entry_widgets) > 0:

            for widget in self.data_entry_widgets:
                name = self.scholars_db_handle.get_name(DefaultTools.session_handle, int(widget.ui.mmrData.text()))
                ronin = self.scholars_db_handle.get_ronin_address(DefaultTools.session_handle, name)
                rank =  str(self.scholars_db_handle.get_rank(DefaultTools.session_handle, name))

                if height > 1000:
                    widget.ui.roninData.setText(ronin)
                    widget.ui.nameData.setText(name)
                    widget.ui.nameEdit.setMaximumWidth(250)
                else:
                    widget.ui.roninData.setText(ronin[:9]+'...')
                    name_list = name.split()
                    widget.ui.nameData.setText(name_list[0])
                    widget.ui.nameEdit.setMaximumWidth(100)

                if len(rank) > 7:
                    widget.ui.rankData.setText(rank[:7]+'...')

    def font_configuration(self):

        # header widgets
        h_labels = [self.ui.nameLabel, self.ui.mmrLabel, self.ui.rankLabel, self.ui.totalSlpLabel, self.ui.averageLabel, self.ui.roninLabel, self.ui.slpGoalLabel,
                    self.ui.slpTodayLabel, self.ui.leaderLabel]

        font_config = [self.func.set_font(label, 9, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True, True) for label in
                       h_labels]

        self.func.set_font(self.ui.indiceLabel, 9,
                           ':/font/fonts/Saira-Bold.ttf', '#7A8289', True, True)

        self.func.set_font(self.ui.addBtn, 10,
                           ':/font/fonts/Saira-Bold.ttf', '#E64C3C', False, False)

    def shadow_configuration(self):
        self.func.set_drop_shadow(self)

    def data_entry_creator(self):

        # get data
        self.get_data_info()

        # make widget with the data
        for data_info in self.data_entry_info:
            self.data_entry_widget_creator(data_info)

    def data_entry_widget_creator(self, dict_info):
        widget = dataEntryCreator(dict_info=dict_info)

        self.data_entry_widgets.append(widget)


class dataEntryCreator(QWidget):
    
    need_update_signal = Signal(bool)

    def __init__(self, dict_info: dict) -> None:
        super(dataEntryCreator, self).__init__()
        self.ui = Ui_dataEntryCreator()
        self.ui.setupUi(self)
        self.func = UIFunctions()
        
        self.scholars_db_handle = Scholar()
        self.enable_mouse_changing = True

        # set info
        self.ui.nameData.setText(dict_info['name'])
        self.ui.roninData.setText(dict_info['ronin'])
        self.ui.mmrData.setText(dict_info['mmr'])
        self.ui.rankData.setText(dict_info['rank'])
        self.ui.averageData.setText(dict_info['total_average_slp'])
        self.ui.totalSlpData.setText(dict_info['total_acc_slp'])
        self.ui.slpGoalData.setText(dict_info['daily_goal'])
        self.ui.slpTodayData.setText(dict_info['today_profit'])
        
        # default
        self.ui.editBtn.hide()
        self.ui.delBtn.hide()
        self.ui.nameEdit.hide()
        self.ui.slpGoalEdit.hide()
        
        self.ui.copyBtn.clicked.connect(self.copy_to_clipboard)
        self.ui.editBtn.clicked.connect(self.edit)
        self.ui.delBtn.clicked.connect(self.delete)

        # configs
        self.font_configuration() 
        self.installEventFilter(self)
        
    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        
        if self.enable_mouse_changing:
            if watched == self and event.type() == QtCore.QEvent.Type.Enter:
                self.ui.editBtn.show()
                self.ui.delBtn.show()
            
            elif watched == self and event.type() == QtCore.QEvent.Type.Leave:
                self.ui.editBtn.hide()
                self.ui.delBtn.hide()
        
        return super().eventFilter(watched, event)  
    
    def delete(self):
        
        name = self.scholars_db_handle.get_name(DefaultTools.session_handle, int(self.ui.mmrData.text()))
        ronin = self.scholars_db_handle.get_ronin_address(DefaultTools.session_handle, name)
        
        self.scholars_db_handle.delete(DefaultTools.session_handle, ronin)
        
        self.need_update_signal.emit(True)
    
    def edit(self):
        # change icon
        self.edit_to_save()
        
        name = self.scholars_db_handle.get_name(DefaultTools.session_handle, int(self.ui.mmrData.text()))
        self.ui.nameData.hide()
        self.ui.nameEdit.show()
        self.ui.nameEdit.setPlaceholderText(name)
        
        daily = self.ui.slpGoalData.text()
        self.ui.slpGoalData.hide()
        self.ui.slpGoalEdit.show()
        self.ui.slpGoalEdit.setPlaceholderText(daily)
        
        for label in [self.ui.nameEdit, self.ui.slpGoalEdit]:
            self.func.set_font(label, 10, ':/font/fonts/Saira-Bold.ttf', '#F9F9F9', True, False)
            
        self.ui.editBtn.show()
        self.ui.delBtn.show()
        self.enable_mouse_changing = False
    
    def edit_to_save(self):
        icon = QIcon()
        icon.addFile(u":/images/img/save.svg", QSize(), QIcon.Normal, QIcon.Off)        
        self.ui.editBtn.setIcon(icon)
        self.ui.editBtn.setIconSize(QSize(18, 18))
        
        self.ui.editBtn.clicked.connect(self.save)
    
    def save_to_edit(self):
        icon = QIcon()
        icon.addFile(u":/images/img/edit.png", QSize(), QIcon.Normal, QIcon.Off)        
        self.ui.editBtn.setIcon(icon)
        self.ui.editBtn.setIconSize(QSize(18, 18))
        
        self.ui.editBtn.clicked.connect(self.edit)
    
    def save(self):
        # change icon
        self.save_to_edit()
        
        name = self.ui.nameEdit.text()
        daily_goal = self.ui.slpGoalEdit.text()
        old_name = self.scholars_db_handle.get_name(DefaultTools.session_handle, int(self.ui.mmrData.text()))
        ronin = self.scholars_db_handle.get_ronin_address(DefaultTools.session_handle, old_name)
        
        if name == '':
            name = self.ui.nameData.text()
            
        if daily_goal == '':
            daily_goal = self.ui.slpGoalData.text()
        
        self.scholars_db_handle.update_name(DefaultTools.session_handle, ronin, name)
        self.scholars_db_handle.update_slp_goal(DefaultTools.session_handle, ronin, int(daily_goal))
        
        self.ui.nameData.show()
        self.ui.nameEdit.hide()
        self.ui.nameData.setText(name)
        
        self.ui.slpGoalData.show()
        self.ui.slpGoalEdit.hide()
        self.ui.slpGoalData.setText(daily_goal)
        
        self.ui.editBtn.hide()
        self.ui.delBtn.hide()
        self.enable_mouse_changing = True
    
    def copy_to_clipboard(self):
        clipboard = QGuiApplication.clipboard()
        originalText = clipboard.text()
        
        name = self.scholars_db_handle.get_name(DefaultTools.session_handle, int(self.ui.mmrData.text()))
        ronin = self.scholars_db_handle.get_ronin_address(DefaultTools.session_handle, name)
        
        clipboard.setText(ronin)

    def _close_widget(self):
        self.deleteLater()

    def font_configuration(self):
        data_labels = [self.ui.nameData, self.ui.mmrData, self.ui.rankData, self.ui.averageData, self.ui.totalSlpData, self.ui.roninData, self.ui.slpGoalData,
                       self.ui.slpTodayData]

        font_config = [self.func.set_font(label, 10, ':/font/fonts/Saira-Bold.ttf', '#F9F9F9', True, True) for label in
                       data_labels]


class RankLeaderboard(QWidget):
    def __init__(self, name='', pos=0, image_url=None):
        super(RankLeaderboard, self).__init__()

        # default data
        default_data = [{'image_medal': ':/images/img/1st.png',
                         'color': 0xB9AA1A,
                         'size': QSize(205, 210)},
                        {'image_medal': ':/images/img/2st.png',
                         'color': 0xC2C2C2,
                         'size': QSize(99, 117)},
                        {'image_medal': ':/images/img/3st.png',
                         'color': 0xB15C21,
                         'size': QSize(99, 117)}]

        self.setMinimumSize(default_data[pos]['size'])
        self.setMaximumSize(default_data[pos]['size'])

        # properties
        self.default_width = 126
        self.color = default_data[pos]['color']
        self.text_color = 0x7A8A98
        self.line_width = 5
        self.font_family = 'Segoe UI'
        self.font_size = 11
        self.name = name
        self.image_url = image_url
        self.tempdir_image = None
        self.already_painted = False
        self.current_heigth = self.height()
        self.current_width = self.width()
        self.medal_image = default_data[pos]['image_medal']

        # image handle
        self.medal_image_label = QLabel(self)
        self.icon_image_label = QLabel(self)
        if self.tempdir_image == None:
            self.save_picture()
        self.repos_images()

        # configurations
        self.installEventFilter(self)

    def update_widget(self):
        self.repaint()

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self and event.type() == QtCore.QEvent.Resize:

            self.current_width = self.width()
            self.current_heigth = self.height()
            self.setMinimumSize(QSize(self.current_width, self.current_heigth))
            self.setMaximumSize(QSize(self.current_width, self.current_heigth))

            if self.width != self.default_width:
                self.repos_images()

            self.update_widget()

        return super().eventFilter(watched, event)

    def repos_images(self):
        # medal
        size_percent = 0.16 if self.height() < 130 else 0.11
        size = QSize(size_percent * self.current_heigth,
                     size_percent * self.current_heigth)
        circle_size = 0.58 * self.current_heigth
        margin_w = 0.075 * self.current_width
        margin_h = self.width() * 0.32
        width = (self.width()/2) - (size.width()/2)
        height = circle_size + margin_h

        self.medal_image_label.setPixmap(QPixmap(f'{self.medal_image}'))
        self.medal_image_label.setGeometry(
            width, height, size.width(), size.height())
        self.medal_image_label.setMaximumSize(size)
        self.medal_image_label.setMinimumSize(size)
        self.medal_image_label.setScaledContents(True)

        # icon
        if self.tempdir_image != None:
            size = QSize(self.width(), (0.75 * self.width()))
            margin_h = (0.195 * self.height()) / \
                1.1 if self.height() < 130 else (0.195 * self.height())/1.5

            self.icon_image_label.setStyleSheet(
                'background-color: rgba(255, 255, 255, 0);')
            self.icon_image_label.setPixmap(QPixmap(f'{self.tempdir_image}'))
            self.icon_image_label.setGeometry(
                0, margin_h, self.width(), self.height())
            self.icon_image_label.setMinimumSize(size)
            self.icon_image_label.setMaximumSize(size)
            self.icon_image_label.setScaledContents(True)
        else:
            size = QSize(self.width(), (0.75 * self.width()))
            margin_h = (0.195 * self.height()) / \
                1.1 if self.height() < 130 else (0.195 * self.height())/1.5

            self.icon_image_label.setStyleSheet(
                'background-color: rgba(255, 255, 255, 0);')
            self.icon_image_label.setGeometry(
                0, margin_h, self.width(), self.height())
            self.icon_image_label.setMinimumSize(size)
            self.icon_image_label.setMaximumSize(size)

    def paintEvent(self, event: QPaintEvent) -> None:

        margin_w = self.width() * 0.3
        margin_h = self.width() * 0.45 if self.height() < 130 else self.width() * 0.34
        height = self.height() - margin_h
        width = self.width() - margin_w

        dinamic_font_size = 0.055 * self.width()
        font_size = dinamic_font_size

        if dinamic_font_size < self.font_size:
            font_size = 9

        if height != width:
            height = width

        # center rect
        rect_center = QRect(QPoint(margin_w/2, margin_h/2),
                            QSize(width, height))
        size_sides_rect = margin_h/2
        # top rect
        rect_top = QRect(0, 0, self.width(), size_sides_rect)

        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)  # remove pixelated edges
        paint.setFont(QFont(self.font_family, font_size))

        pen = QPen()
        pen.setWidth(self.line_width)
        pen.setCapStyle(Qt.RoundCap)

        paint.setPen(Qt.NoPen)
        paint.drawRect(rect_center)
        paint.drawRect(rect_top)

        # name
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect_top, Qt.AlignCenter, f'{self.name}')

        # arc
        pen.setColor(QColor(self.color))
        pen.setWidth(self.line_width)
        paint.setPen(pen)
        paint.drawEllipse(rect_center)

        paint.end()
        self.already_painted = True

    def save_picture(self):
        self.tempdir_image = tempfile.mkdtemp(prefix='axie-manager') if self.image_url != None else None
        if self.image_url != None:
            r = requests.get(self.image_url, allow_redirects=True)
            self.tempdir_image = os.path.join(self.tempdir_image, 'image.png')
            open(f'{self.tempdir_image}', 'wb').write(r.content)
    
    def _close_widget(self):
        self.deleteLater()
