from PySide2.QtWidgets import QDesktopWidget, QLabel, QWidget
from PySide2 import QtCore, QtGui
from PySide2.QtCore import QRect, Qt, QPoint, QSize
from PySide2.QtWidgets import QGraphicsDropShadowEffect
from PySide2.QtGui import QColor, QImage, QPaintEvent, QPainter, QFont, QPen, QPixmap

import tempfile
import requests
import os

try:
    from custom_widgets.ui import Ui_dataViewWidget, Ui_dataEntryCreator
    from functions import UIFunctions
    from model import Scholar, Account, DefaultTools

except ModuleNotFoundError:
    from src.custom_widgets.ui import Ui_dataViewWidget, Ui_dataEntryCreator
    from src.functions import UIFunctions
    from src.model import Scholar, Account, DefaultTools


class StudentsDataView(QWidget):

    def __init__(self, ) -> None:
        super(StudentsDataView, self).__init__()
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

        # font config
        self.font_configuration()

        self.data_entry_creator()

        self.installEventFilter(self)

        self.students_db_handle = Scholar()

        # pages variables
        self.current_page = 1
        self.goto_page = 0
        self.receivers_count = 0
        self.show_widgets_each_page(self.current_page, direction=None)

    def set_new_data(self):
        for widget in self.data_entry_widgets:
            widget._close_widget()

        self.data_entry_info = []
        self.data_entry_widgets = []

        self.data_entry_creator()
        self.show_widgets_each_page(self.current_page, direction=None)
    
    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        
        if event.type() == QtCore.QEvent.Type.Resize:
            
            app_height = self.get_app_height()

            print('width:', self.ui.dataContainer.width())
            
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

        students_list = Scholar.get_all_scholars(DefaultTools.session_handle)

        for student in students_list:
            self.data_entry_info.append({'name': student.name,
                                         'ronin': student.account.ronin_address,
                                         'mmr': str(student.mmr),
                                         'rank': str(student.rank),
                                         'total_acc_slp':str(student.total_acc_slp),
                                         'total_average_slp':str(student.total_average_slp),
                                         'daily_goal': str(student.daily_goal),
                                         'today_profit': str(student.daily_profit)})

    def set_max_height(self, default) -> int:
        if default:
            height = self.height_default
        else:
            height = self.get_height()

        self.setMaximumHeight(height)

        max_widgets = self.get_max_widgets(height)
        max_pages = self.get_number_pages(max_widgets)

        if self.current_page > max_pages:
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

        start_list = []

        print(f'height: {height}, max:{max_widgets}, number_pages: {number_pages}, total_widgets: {total_widget}')
        print(f'Goto page: {goto_page}')

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

            height = self.get_app_height()
            
            for widget in self.data_entry_widgets:
                widget.close()
                ronin = self.students_db_handle.get_ronin_address(DefaultTools.session_handle, widget.ui.nameData.text())

                if height > 1000:
                    widget.ui.roninData.setText(ronin)
                else:
                    widget.ui.roninData.setText(ronin[:10]+'...')

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

    def font_configuration(self):

        # header widgets
        h_labels = [self.ui.nameLabel, self.ui.mmrLabel, self.ui.rankLabel, self.ui.totalSlpLabel, self.ui.averageLabel, self.ui.roninLabel, self.ui.slpGoalLabel,
                    self.ui.slpTodayLabel]

        font_config = [self.func.set_font(label, 9, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True, True) for label in
                       h_labels]

        self.func.set_font(self.ui.indiceLabel, 9, ':/font/fonts/Saira-Bold.ttf', '#7A8289', True, True)

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

    def __init__(self, dict_info: dict) -> None:
        super(dataEntryCreator, self).__init__()
        self.ui = Ui_dataEntryCreator()
        self.ui.setupUi(self)
        self.func = UIFunctions()

        # set info
        self.ui.nameData.setText(dict_info['name'])
        self.ui.roninData.setText(dict_info['ronin'][:10]+'...')
        self.ui.mmrData.setText(dict_info['mmr'])
        self.ui.rankData.setText(dict_info['rank'])
        self.ui.averageData.setText(dict_info['total_average_slp'])
        self.ui.totalSlpData.setText(dict_info['total_acc_slp'])
        self.ui.slpGoalData.setText(dict_info['daily_goal'])
        self.ui.slpTodayData.setText(dict_info['today_profit'])

        # font config
        self.font_configuration()

    def _close_widget(self):
        self.deleteLater()
    
    def font_configuration(self):
        data_labels = [self.ui.nameData, self.ui.mmrData, self.ui.rankData, self.ui.averageData,self.ui.totalSlpData, self.ui.roninData, self.ui.slpGoalData,
                       self.ui.slpTodayData]

        font_config = [self.func.set_font(label, 10, ':/font/fonts/Saira-Bold.ttf', '#F9F9F9', True, True) for label in
                       data_labels]

class RankLeaderboard(QWidget):
    def __init__(self, name='Gustavo', font_family='Segoe UI', color=0xB9AA1A, image=':/images/img/1st.png'):
        super(RankLeaderboard, self).__init__()
        self.setGeometry(0, 0, 200, 200)
        
        self.current_heigth = self.height()
        self.current_width = self.width()
        
        self.medal_image_label = QLabel(self)
        self.icon_image_label = QLabel(self)
        
        # properties
        self.color = color
        self.text_color = 0x7A8A98
        self.line_width = 5
        self.font_family = font_family
        self.font_size = 11
        self.image = image
        self.name = name
        self.image_url = 'https://storage.googleapis.com/assets.axieinfinity.com/axies/3557949/axie/axie-full-transparent.png'
        self.tempdir_image = None
        
        self.installEventFilter(self)
        self.enable_shadow(True)
        
    def update_widget(self):
        self.repaint()

    def enable_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect()
            self.shadow.setBlurRadius(6)
            self.shadow.setOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 90))
            self.setGraphicsEffect(self.shadow)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self and event.type() == QtCore.QEvent.Resize:
            print(self.width(), self.height())
            
            if self.width() < self.height():
                size = QSize(self.height(), self.height())
                rect = QRect(self.pos(), size)
                self.setGeometry(rect)
            elif self.height() < self.width():
                size = QSize(self.width(), self.width())
                rect = QRect(self.pos(), size)
                self.setGeometry(rect)
                
            self.update_widget()
        
        return super().eventFilter(watched, event)
    
    def paintEvent(self, event: QPaintEvent) -> None:
        
        if self.tempdir_image == None:
            self.save_picture()
        
        margin_w = self.width() * 0.3
        margin_h = self.width() * 0.3
        height = self.height() - margin_h
        width = self.width() - margin_w
        
        dinamic_font_size = 0.055 * self.width()
        font_size = dinamic_font_size
        
        if dinamic_font_size < self.font_size:
            font_size = 9
        
        if height != width:
            height = width

        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)  # remove pixelated edges
        paint.setFont(QFont(self.font_family, font_size))
        
        pen = QPen()
        pen.setWidth(self.line_width)
        pen.setCapStyle(Qt.RoundCap)
        paint.setPen(pen)

        rect_center = QRect(QPoint(margin_w/2, margin_h/2), QSize(width, height))
        
        size_sides_rect = margin_h/2
        height_bottom_r = rect_center.height() + (margin_h/2)
        rect_bottom = QRect(0, height_bottom_r, self.width(), size_sides_rect)
        
        rect_top = QRect(0, 0, self.width(), size_sides_rect)
        
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect_bottom)        
        paint.drawRect(rect_center)
        paint.drawRect(rect_top)
        
        # name
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect_top, Qt.AlignCenter, f'{self.name}')
        
        size = QSize(margin_h/2, margin_h/2)
        height = rect_center.height() + (margin_h/2)
        width = (self.width()/2) - (size.width()/2)    
        
        # medal image
        self.medal_image_label.setPixmap(QPixmap(f'{self.image}'))
        self.medal_image_label.setGeometry(width, height, size.width(), size.height())
        self.medal_image_label.setMaximumSize(size)
        self.medal_image_label.setMinimumSize(size)
        self.medal_image_label.setScaledContents(True)
        
        # icon image
        size = QSize(self.width(), self.height())
        self.icon_image_label.setPixmap(QPixmap(f'{self.tempdir_image}'))
        self.icon_image_label.setGeometry(0, 0, self.width(), self.height())
        self.icon_image_label.setMinimumSize(size)
        self.icon_image_label.setMaximumSize(size)
        self.icon_image_label.setScaledContents(True)
        
        # arc    
        pen.setColor(QColor(self.color))
        pen.setWidth(self.line_width)
        paint.setPen(pen)
        paint.drawEllipse(rect_center) 
        
        paint.end()        
        
    def save_picture(self):
        self.tempdir_image = tempfile.mkdtemp(prefix='axie-manager')
        r = requests.get(self.image_url, allow_redirects=True)
        self.tempdir_image = os.path.join(self.tempdir_image, 'image.png')
        open(f'{self.tempdir_image}', 'wb').write(r.content)
        
