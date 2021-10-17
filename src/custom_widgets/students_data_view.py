from PySide2.QtWidgets import QDesktopWidget, QWidget
from PySide2 import QtCore, QtGui
from PySide2.QtCore import QAbstractAnimation
from PySide2.QtWidgets import QGraphicsOpacityEffect

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

        # font config
        self.font_configuration()

        self.data_entry_creator()

        # pages variables
        self.current_page = 1
        self.goto_page = 0
        self.receivers_count = 0
        self.show_widgets_each_page(self.current_page, direction=None)

    def event(self, event: QtCore.QEvent) -> bool:

        if event.type() == QtCore.QEvent.Type.Resize:
            try:
                app_height = self.get_app_height()
            except AttributeError:
                app_height = 680

            app_default_height = 680

            if app_height == app_default_height:
                self.set_max_height(default=True)
            elif app_height > app_default_height:
                self.set_max_height(default=False)

        return super().event(event)

    def get_height(self) -> int:

        try:
            app_height = self.get_app_height()
        except AttributeError:
            app_height = 540

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

        """for i in range(0, 40):
            self.data_entry_info.append({'name': f'{i}',
                                         'ronin': 'asd',
                                         'email': 'asd',
                                         'daily_goal': 'asd',
                                         'today_profit': 'asd'})

        return"""

        students_list = Scholar.get_all_scholars(DefaultTools.session_handle)

        for student in students_list:
            self.data_entry_info.append({'name': student.name,
                                         'ronin': student.account.ronin_address,
                                         'email': student.email,
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
        if direction == 'left':
            # goto <-
            for i in range(0, number_pages):
                start_list.append(max_widgets * i)

            start_i = goto_page - 1
            end_i = goto_page

            start_clean_i = goto_page
            end_clean_i = goto_page + 1

            widget_width = self.width()

            # transition current itens to ->
            start_place_out = QtCore.QPoint(0, 0)
            end_place_out = QtCore.QPoint(widget_width + 1000, 0)
            start_place_in = QtCore.QPoint(-1000, 0)
            end_place_in = QtCore.QPoint(0, 0)

            visible_widgets = self.data_entry_widgets[start_list[start_clean_i]: start_list[end_clean_i]] \
                if goto_page != abs(number_pages-1) else \
                self.data_entry_widgets[start_list[start_clean_i]:]

            new_widgets = self.data_entry_widgets[start_list[start_i]:start_list[end_i]]

            for widget in visible_widgets:
                self.transition_animation(start_place_out, end_place_out, duration=150, widget=widget, out=True)
                start_place_out.setY(start_place_out.y() + 30)
                end_place_out.setY(end_place_out.y() + 30)

            for widget in new_widgets:
                if not widget.isVisible():
                    self.ui.layoutDataWidgets.addWidget(widget)
                self.transition_animation(start_place_in, end_place_in, duration=150, widget=widget)
                start_place_in.setY(start_place_in.y() + 30)
                end_place_in.setY(end_place_in.y() + 30)

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

            # transition current itens to <-
            start_place_out = QtCore.QPoint(0, 0)
            end_place_out = QtCore.QPoint(-2000, 0)
            start_place_in = QtCore.QPoint(widget_width + 2000, 0)
            end_place_in = QtCore.QPoint(0, 0)

            visible_widgets = self.data_entry_widgets[start_list[start_clean_i]:start_list[end_clean_i]]
            new_widgets = self.data_entry_widgets[start_list[start_i]: start_list[end_i]] \
                if goto_page != number_pages else \
                self.data_entry_widgets[start_list[start_i]:]

            for widget in visible_widgets:
                self.transition_animation(start_place_out, end_place_out, duration=150, widget=widget, out=True)
                start_place_out.setY(start_place_out.y() + 30)
                end_place_out.setY(end_place_out.y() + 30)

            for widget in new_widgets:
                if not widget.isVisible():
                    self.ui.layoutDataWidgets.addWidget(widget)
                self.transition_animation(start_place_in, end_place_in, duration=150, widget=widget)
                start_place_in.setY(start_place_in.y() + 30)
                end_place_in.setY(end_place_in.y() + 30)

        elif direction == None:

            for widget in self.data_entry_widgets:
                widget.close()

            for i in range(0, number_pages):
                start_list.append(max_widgets * i)

            start_i = goto_page - 1
            end_i = goto_page

            new_widgets = self.data_entry_widgets[start_list[start_i]: start_list[end_i]] \
                if goto_page != number_pages else \
                self.data_entry_widgets[start_list[start_i]:]

            for widget in new_widgets:
                if not widget.isVisible():
                    self.ui.layoutDataWidgets.addWidget(widget)
                    widget.show()

        self.ui.indiceLabel.setText(f'{goto_page}')
        self.current_page = goto_page

    def set_opacity(self, widget, value):
        effect = QGraphicsOpacityEffect(widget)
        effect.setOpacity(value)
        widget.setGraphicsEffect(effect)

    def transition_animation(self, start_point, end_point, duration, widget, out=False):
        widget.animation = QtCore.QPropertyAnimation(widget, b'pos')
        widget.animation.setDuration(duration)
        widget.animation.setStartValue(start_point)
        widget.animation.setEndValue(end_point)
        widget.animation.setEasingCurve(QtCore.QEasingCurve.InQuad)

        if out == True:
            widget.animation.finished.connect(lambda: self.out_widget_func(widget))
        else:
            widget.animation.stateChanged.connect(lambda: self.in_widget_func(widget))

        widget.animation.start()

    def out_widget_func(self, widget):
        self.set_opacity(widget, 0)
        widget.close()

    def in_widget_func(self, widget):
        if widget.animation.state() == QAbstractAnimation.State.Running:
            self.set_opacity(widget, 1)
            widget.show()

    def font_configuration(self):

        # header widgets
        h_labels = [self.ui.nameLabel, self.ui.emailLabel, self.ui.roninLabel, self.ui.slpGoalLabel,
                    self.ui.slpTodayLabel]

        font_config = [self.func.set_font(label, 11, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True, True) for label in
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
        self.ui.roninData.setText(dict_info['ronin'])
        self.ui.emailData.setText(dict_info['email'])
        self.ui.slpGoalData.setText(dict_info['daily_goal'])
        self.ui.slpTodayData.setText(dict_info['today_profit'])

        # font config
        self.font_configuration()

    def font_configuration(self):
        data_labels = [self.ui.nameData, self.ui.emailData, self.ui.roninData, self.ui.slpGoalData,
                       self.ui.slpTodayData]

        font_config = [self.func.set_font(label, 10, ':/font/fonts/Saira-Bold.ttf', '#F9F9F9', True, True) for label in
                       data_labels]
