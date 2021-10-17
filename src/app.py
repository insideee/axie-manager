from PySide2.QtGui import QMovie
from PySide2.QtWidgets import *
from PySide2.QtCore import QThread, QTimer, Signal, QPoint, QRect, Qt, QEvent, QAbstractAnimation
from datetime import datetime, timezone
import os
import sys

# gui file and gui functions
try:
    from ui.ui_main import Ui_MainWindow
    from functions import UIFunctions
    from custom_widgets import *
    from model import DefaultTools, Account, Scholar
    from api import AccAxie, FullData
except ModuleNotFoundError:
    from src.ui.ui_main import Ui_MainWindow
    from src.functions import UIFunctions
    from src.custom_widgets import *
    from src.model import DefaultTools, Account, Scholar
    from src.api import AccAxie, FullData


class MainWindow(QMainWindow, UIFunctions):

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # worker variables
        self.load_info_worker = None
        self.load_home_info_thread_handle(initialization=True)

        # qtimer variables
        self.update_infos_timer = None
        self.timer_handle()

        # slot initialization variables
        self.initialization_slot = False
        self.updating_slot = False
        self.add_popup_slot = False
        self.students_amount_slot = None
        self.students_goal_percent_slot = None
        self.actual_month_slot = None
        self.last_month_slot = None
        self.next_last_month_slot = None
        self.axie_amount_slot = None

        # pop up variables
        self.pop_up = AddPopUp()
        self.pop_up.close_signal.connect(lambda: self.load_home_info_thread_handle(after_add_popup=True))

        # graph widgets variables
        self.students_goal_graphic = None
        self.profit_graphic = None
        self.axies_graphic = None

        # window configs
        self.window_centered = False
        self.window_gui_configuration()

        # button configs
        self.btn_gui_configuration()

        # fonts configs
        self.fonts_gui_configuration()

        # drop shadow configs
        self.drop_shadow_gui_configuration()

        # home page graphics configuration
        self.graph_configurations()

        # students page configuration
        self.students_page_configuration()

        # work in progress
        self.set_work_in_progress_pages()

        # show gui
        self.show()

        self.active_screen_geometry = QDesktopWidget().screenGeometry(self)

    def window_gui_configuration(self):
        # center and config window
        self.config_window(config_widget=self, title='', width=1200, height=680, resizable=True,
                           minimum_size=True)
        # remove title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.window_centered = True

    def btn_gui_configuration(self):
        # toggle button
        self.ui.btn_toggle.clicked.connect(lambda: self.toggle_menu(self.ui.menu_container, 140, True))

        # title bar buttons
        self.ui.btn_exit.clicked.connect(lambda: sys.exit(1))
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.ui.btn_expand.clicked.connect(lambda: self.min_and_max_window(self))

        # add student home page
        self.ui.add_home_btn.setMinimumWidth(100)
        self.ui.add_home_btn.setMaximumWidth(100)
        self.ui.add_home_btn.close()
        self.ui.add_home_btn.clicked.connect(self.show_add_pop_up)

        # link button -> pages
        self.link_pages(self.ui.pages_container,
                        list_btn=[self.ui.btn_home, self.ui.btn_profit, self.ui.btn_students,
                                  self.ui.btn_inventory,
                                  self.ui.btn_mail, self.ui.btn_settings],
                        list_pages=[self.ui.home_page, self.ui.profit_page, self.ui.students_page,
                                    self.ui.inventory_page,
                                    self.ui.mail_page, self.ui.settings_page])

        # link home_page buttons -> pages
        self.link_pages(self.ui.pages_container,
                        list_btn=[self.ui.goto_students_btn, self.ui.goto_profit_btn, self.ui.goto_axies_btn],
                        list_pages=[self.ui.students_page, self.ui.profit_page, self.ui.inventory_page])

        # home_btn style

        # clicked gui
        self.btn_style_handle(list_btn=[self.ui.btn_home, self.ui.btn_profit, self.ui.btn_students,
                                        self.ui.btn_inventory,
                                        self.ui.btn_mail, self.ui.btn_settings])

    def fonts_gui_configuration(self):
        # title bar
        self.set_font(self.ui.title1_label, 12, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False, True)
        self.set_font(self.ui.title2_label, 12, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True, True)

        # info bottom
        self.set_font(self.ui.info_label, 10, ':/font/fonts/Saira-Light.ttf', '#E64C3C', True, True)

        # menu
        menu_labels = [self.set_font(label, 12, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False, False) for label in
                       [self.ui.btn_home, self.ui.btn_profit, self.ui.btn_students, self.ui.btn_inventory,
                        self.ui.btn_mail, self.ui.btn_settings]]

        # home widgets
        # title
        home_widgets_labels = [self.set_font(label, 12, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False, True) for
                               label in
                               [self.ui.title_students, self.ui.title_profit, self.ui.title_axies]]

        # data
        home_widgets_labels = [self.set_font(label, 40, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False, True) for
                               label in
                               [self.ui.data_label_students, self.ui.data_label_profit, self.ui.data_label_axies]]

        # add home btn
        self.set_font(self.ui.add_home_btn, 10, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', False, False)

    def drop_shadow_gui_configuration(self):
        # shadow top bar
        self.set_drop_shadow(self.ui.top_bar)

        # shadow add home btn
        self.set_drop_shadow(self.ui.add_home_btn)

        # shadow home widgets
        self.set_drop_shadow(self.ui.axies_widget, self.ui.profit_widget, self.ui.students_widget)

    def graph_configurations(self):
        self.students_goal_graphic = CircularProgress(200, 200, font_family='Saira')

        self.profit_graphic = BarGraph(250, 250, font_family='Saira')

        self.axies_graphic = HomeMarketFeature(200, 200)

        add_widget = [self.ui.graphics_layout.addWidget(widget) for widget in
                      [self.students_goal_graphic, self.profit_graphic, self.axies_graphic]]

    def set_work_in_progress_pages(self):

        work_pages = [self.ui.label_2, self.ui.label_4, self.ui.label_5, self.ui.label_6]

        for v in work_pages:
            self.set_font(v, 25, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True, True)
            v.setText('Work in progress...')

    def students_page_configuration(self):
        self.students_widget = StudentsDataView()

        self.ui.verticalLayout_5.addWidget(self.students_widget)

    def event(self, event: QEvent) -> bool:
        # black screen on initilization because \
        # students widget was showing first

        if event.type() == QEvent.Type.Show:
            self.students_widget.show()

        if event.type() == QEvent.Type.Move:
            if self.window_centered and hasattr(self, 'active_screen_geometry'):
                self.check_window_changed()

        return super().event(event)

    def showMaximized(self) -> None:
        if self.ui.icon_label.isVisible() or self.ui.info_label.isVisible():
            stopped = self.ui.icon_label.animation.state() == QAbstractAnimation.State.Stopped \
                      and self.ui.info_label.animation.state() == QAbstractAnimation.State.Stopped

            if self.ui.icon_label.y() == 0 and stopped:
                self.animate(QPoint(10, 0), self.ui.info_label)
                self.animate(QPoint(110, 0), self.ui.icon_label)

        return super().showMaximized()

    def showNormal(self) -> None:
        if self.ui.icon_label.isVisible() or self.ui.info_label.isVisible():
            stopped = self.ui.icon_label.animation.state() == QAbstractAnimation.State.Stopped \
                      and self.ui.info_label.animation.state() == QAbstractAnimation.State.Stopped

            if self.ui.icon_label.y() == 0 and stopped:
                self.animate(QPoint(1009, 0), self.ui.info_label)
                self.animate(QPoint(1109, 0), self.ui.icon_label)

        return super().showNormal()

    def show_add_pop_up(self):
        # show
        self.pop_up.show()

    def load_home_info_thread_handle(self, initialization=False, after_add_popup=False, update=False) -> None:

        if initialization:
            self.load_info_worker = LoadHomeInfoWorker(initialization=True)
        elif after_add_popup:
            self.load_info_worker = LoadHomeInfoWorker(after_add_popup=True)
        elif update:
            self.load_info_worker = LoadHomeInfoWorker(update=True)

        self.load_info_worker.students_amount_signal.connect(self.students_amount_receive)
        self.load_info_worker.students_goal_percent_signal.connect(self.students_goal_percent_receive)
        self.load_info_worker.actual_month_signal.connect(self.actual_month_receive)
        self.load_info_worker.last_month_signal.connect(self.last_month_receive)
        self.load_info_worker.next_last_month_signal.connect(self.next_last_month_receive)
        self.load_info_worker.axie_amount_signal.connect(self.axie_amount_receive)
        self.load_info_worker.initalization_signal.connect(self.initialization_receive)
        self.load_info_worker.updating_signal.connect(self.updating_receive)
        self.load_info_worker.after_add_popup_signal.connect(self.after_add_popup_receive)
        self.load_info_worker.message_signal.connect(self.message_handle)

        self.load_info_worker.start()

        self.load_info_worker.finished.connect(self.home_info_setter)

    def message_handle(self):
        if self.updating_slot:
            if self.students_amount_slot != None and int(self.students_amount_slot) > 0:
                self.info_setter('', update=True)

    def info_setter(self, message, update=False):
        if update:
            # label config
            self.ui.info_label.setText('Updating infos')
            self.ui.info_label.setGeometry(0, 0, 100, 30)
            self.ui.info_label.setAlignment(Qt.AlignVCenter)
            self.ui.info_label.close()

            # label movie config
            self.ui.icon_label.setGeometry(QRect(0, 0, 25, 25))
            gif_dir = os.path.dirname(os.path.abspath(__name__)) + '/img/loading.gif'
            self.movie = QMovie(gif_dir)
            self.ui.icon_label.setMovie(self.movie)
            self.ui.icon_label.close()
            self.movie.start()
            self.movie.started.connect(lambda: print('started'))

            widget_width = self.ui.info_container.width()
            widget_height = self.ui.info_container.height()

            state_maximized = self.isMaximized()
            # closing animation
            if state_maximized:
                self.animate(QPoint(10, 30), self.ui.info_label, duration=1000,
                             start_pos=QPoint(abs(widget_width - (widget_width - 140)), abs(widget_height + 10)))
                self.animate(QPoint(110, 30), self.ui.icon_label, duration=1000,
                             start_pos=QPoint(abs(widget_width - (widget_width - 40)), abs(widget_height + 10)))
            else:
                self.animate(QPoint(abs(widget_width - 140), abs(widget_height - 30)), self.ui.info_label,
                             duration=1000, start_pos=QPoint(abs(widget_width - 140), abs(widget_height + 10)))
                self.animate(QPoint(abs(widget_width - 40), abs(widget_height - 30)), self.ui.icon_label, duration=1000,
                             start_pos=QPoint(abs(widget_width - 40), abs(widget_height + 10)))

    def home_info_setter(self):
        print('setting')
        if self.initialization_slot:
            self.load_home_info_thread_handle(update=True)
            self.initialization_slot = False

        elif self.updating_slot:
            state_maximized = self.isMaximized()

            # closing animation
            if state_maximized:
                self.animate(QPoint(10, 30), self.ui.info_label, duration=1000, closing=True)
                self.animate(QPoint(110, 30), self.ui.icon_label, duration=1000, closing=True)
            else:
                self.animate(QPoint(1009, 30), self.ui.info_label, duration=1000, closing=True)
                self.animate(QPoint(1109, 30), self.ui.icon_label, duration=1000, closing=True)

            self.updating_slot = False

        # set graph widgets infos
        self.students_goal_graphic.update_value(self.students_goal_percent_slot)
        self.profit_graphic.update_value(self.next_last_month_slot, self.last_month_slot, self.actual_month_slot)

        # set data view infos
        self.ui.data_label_students.setText(str(self.students_amount_slot))
        self.ui.data_label_profit.setText(str(self.actual_month_slot))
        self.ui.data_label_axies.setText(str(self.axie_amount_slot))

        if self.students_amount_slot == 0:
            self.ui.verticalLayout_15.setAlignment(Qt.AlignHCenter)
            self.ui.data_label_students.close()
            self.ui.add_home_btn.show()
        else:
            self.ui.verticalLayout_15.setAlignment(Qt.AlignRight)
            self.ui.data_label_students.show()
            self.ui.add_home_btn.close()

    def timer_handle(self):
        self.update_infos_timer = QTimer()
        self.update_infos_timer.start(900000)
        self.update_infos_timer.timeout.connect(lambda: self.load_home_info_thread_handle(update=True))

    def check_window_changed(self):

        actual_screen_value = self.active_screen_geometry
        screen_geometry = QDesktopWidget().screenGeometry(self)

        if self.isVisible() and screen_geometry.width() != actual_screen_value.width():
            state = self.isMaximized()

            if state:
                default = False
            else:
                default = True

            self.students_widget.set_max_height(default=default)
            self.active_screen_geometry = screen_geometry

    def initialization_receive(self, value):
        self.initialization_slot = value

    def updating_receive(self, value):
        self.updating_slot = value

    def after_add_popup_receive(self, value):
        self.add_popup_slot = True

    def students_amount_receive(self, value):
        self.students_amount_slot = value

    def students_goal_percent_receive(self, value):
        self.students_goal_percent_slot = value

    def actual_month_receive(self, value):
        self.actual_month_slot = value

    def last_month_receive(self, value):
        self.last_month_slot = value

    def next_last_month_receive(self, value):
        self.next_last_month_slot = value

    def axie_amount_receive(self, value):
        self.axie_amount_slot = value


class LoadHomeInfoWorker(QThread):
    # state signals
    initalization_signal = Signal(bool)
    after_add_popup_signal = Signal(bool)
    updating_signal = Signal(bool)
    message_signal = Signal(bool)

    # crud signals
    students_amount_signal = Signal(int)
    students_goal_percent_signal = Signal(int)
    actual_month_signal = Signal(int)
    last_month_signal = Signal(int)
    next_last_month_signal = Signal(int)
    axie_amount_signal = Signal(int)

    def __init__(self, initialization=False, after_add_popup=False, update=False):
        super(LoadHomeInfoWorker, self).__init__()
        self.initalization = initialization
        self.after_add_popup = after_add_popup
        self.update = update

        self.students_db_handle = Scholar()
        self.acc_db_handle = Account()

    def run(self) -> None:
        print('working')
        if self.update:
            self.updating_signal.emit(True)

        self.message_signal.emit(True)

        if self.update:
            # checar se dia trocou
            day_changed = self.check_day_change()

            # checar se ouve alteração no profit
            need_daily_update, daily_update_list = self.check_daily_profit()

            # checar se o mês trocou
            month_changed = self.check_month_changed()

            if month_changed:
                print('month changed')
                self.month_changed()
            elif day_changed:
                self.day_changed()
                print('day changed')
            elif need_daily_update:
                print('need daily update')
                self.need_daily_update(daily_update_list)

            self.update_time()

        # crud            
        amount_students = self.get_students_amount()
        daily_goal_percent = int(self.get_students_goal_percent())
        actual_month, last_month, next_last_month = self.get_months_values()
        axie_amount = self.get_axie_amount()

        self.students_amount_signal.emit(amount_students)
        self.students_goal_percent_signal.emit(daily_goal_percent)
        self.actual_month_signal.emit(actual_month)
        self.last_month_signal.emit(last_month)
        self.next_last_month_signal.emit(next_last_month)
        self.axie_amount_signal.emit(axie_amount)

        if self.initalization:
            self.initalization_signal.emit(True)

    def get_students_amount(self) -> int:
        amount_students = self.students_db_handle.get_scholar_amount(DefaultTools.session_handle)

        return amount_students

    def get_students_goal_percent(self) -> int:
        daily_goal, daily_profit = self.students_db_handle.get_daily_goal_and_profit(DefaultTools.session_handle)

        try:
            percent = (daily_profit / daily_goal) * 100
        except ZeroDivisionError:
            percent = 0

        return percent

    def get_months_values(self) -> int:
        actual_value, last_value, next_last_value = self.students_db_handle.get_months_values(
            DefaultTools.session_handle)

        return actual_value, last_value, next_last_value

    def get_axie_amount(self) -> int:
        return self.acc_db_handle.get_axies_amount(DefaultTools.session_handle)

    def check_day_change(self) -> bool:
        last_time_dict = self.students_db_handle.get_dict_last_time_checked(DefaultTools.session_handle)
        time_now = datetime.now(timezone.utc)

        for time_string in last_time_dict['last_time']:
            datetime_obj = datetime.strptime(time_string, '%Y-%m-%d %H:%M')

            if datetime_obj.day != time_now.day:
                return True

        return False

    def api_validator(self, ronin_account):
        """Check if api is down and return it and the retrieved data
        """
        user_api = FullData(ronin_account)

        if len(user_api.data) > 0:
            for k, v in user_api.data.items():
                if k == 'messages' and v == 'The API is unreachable, please contact the API provider':
                    return False, user_api.data

        return True, {'ronin_address': ronin_account,
                      'daily_updated': user_api.get_daily_slp(),
                      'yesterdaySLP': user_api.get_yesterday_slp()}

    def check_daily_profit(self):
        """Check if need update in the daily profit and return the needed update list
        """
        need_update = False
        students = self.students_db_handle.get_all_scholars(DefaultTools.session_handle)
        need_update_list = []

        for i in range(0, self.students_db_handle.get_scholar_amount(DefaultTools.session_handle)):
            done = False
            data = None

            while not done:
                done, data = self.api_validator(students[i].account.ronin_address)

            if students[i].daily_profit < data['daily_updated']:
                need_update = True
                need_update_list.append({'name': students[i].name,
                                         'value': data['daily_updated']})

        return need_update, need_update_list

    def check_month_changed(self) -> bool:
        """Check if month changed and return it
        """
        last_time_dict = self.students_db_handle.get_dict_last_time_checked(DefaultTools.session_handle)
        time_now = datetime.now(timezone.utc)

        for time_string in last_time_dict['last_time']:
            datetime_obj = datetime.strptime(time_string, '%Y-%m-%d %H:%M')

            # check year and month
            if datetime_obj.year < time_now.year or datetime_obj.month < time_now.month:
                return True

        return False

    def day_changed(self, month_changed=False):
        students = self.students_db_handle.get_all_scholars(DefaultTools.session_handle)

        for i in range(0, self.students_db_handle.get_scholar_amount(DefaultTools.session_handle)):
            done = False
            data = None
            need_sum = True if not month_changed else False

            while not done:

                done, data = self.api_validator(students[i].account.ronin_address)

                if students[i].daily_profit < data['yesterdaySLP']:
                    value = abs(students[i].daily_profit - data['yesterdaySLP']) + data['daily_updated']
                else:
                    value = data['daily_updated']

                if not need_sum:
                    value -= data['daily_updated']

                self.students_db_handle.update_month_profit(DefaultTools.session_handle,
                                                            students[i].name,
                                                            abs(value))

                self.students_db_handle.set_daily_profit(DefaultTools.session_handle, data['daily_updated'],
                                                         ronin=data['ronin_address'])

    def need_daily_update(self, list_update_needed):

        for i in range(0, len(list_update_needed)):
            name = list_update_needed[i]['name']
            value = list_update_needed[i]['value']
            student = self.students_db_handle.find_by_name(DefaultTools.session_handle, name)

            difference = student.daily_profit - value

            # update month
            self.students_db_handle.update_month_profit(DefaultTools.session_handle,
                                                        name,
                                                        abs(difference))

            # update daily
            self.students_db_handle.set_daily_profit(DefaultTools.session_handle,
                                                     value,
                                                     name_input=name)

    def month_changed(self):

        self.day_changed(month_changed=True)

        self.students_db_handle.set_month_changed(DefaultTools.session_handle)

        daily_dict = self.students_db_handle.get_dict_daily_profit(DefaultTools.session_handle)

        for i in range(0, len(daily_dict['name'])):
            self.students_db_handle.update_month_profit(DefaultTools.session_handle,
                                                        daily_dict['name'][i],
                                                        daily_dict['daily_profit'][i])

    def update_time(self):
        time_now = datetime.now(timezone.utc)
        formated_datetime = time_now.strftime('%Y-%m-%d %H:%M')

        self.students_db_handle.update_time_checked(DefaultTools.session_handle, formated_datetime)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
