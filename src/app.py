import sys
from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import QThread, QTimer, Signal
from sqlalchemy.sql.functions import next_value
from api import FullData, AccAxie
from model import DefaultTools, Account, Scholar

# gui file and gui functions
try:
    from ui.ui_main import Ui_MainWindow
    from functions import UIFunctions
    from custom_widgets import *
except ModuleNotFoundError:
    from src.ui.ui_main import Ui_MainWindow
    from src.functions import UIFunctions
    from src.custom_widgets import *


class MainWindow(QMainWindow, UIFunctions):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # worker variables
        self.load_info_worker = None        
        self.load_home_info_thread_handle(initialization=True)
        
        # slot initialization variables
        self.initialization_slot = False
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
        self.window_gui_configuration()

        # button configs
        self.btn_gui_configuration()

        # fonts configs
        self.fonts_gui_configuration()

        # drop shadow configs
        self.drop_shadow_gui_configuration()

        # home page graphics configuration
        self.graph_configurations()

        # work in progress
        self.set_work_in_progress_pages()

        # show gui
        self.show()

    def window_gui_configuration(self):
        # center and config window
        self.config_window(config_widget=self, title='', width=1200, height=680, resizable=True,
                           minimum_size=True)
        # remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def btn_gui_configuration(self):
        # toggle button
        self.ui.btn_toggle.clicked.connect(lambda: self.toggle_menu(self.ui.menu_container, 140, True))

        # title bar buttons
        self.ui.btn_exit.clicked.connect(lambda: sys.exit(1))
        #self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.ui.btn_minimize.clicked.connect(self.show_add_pop_up)
        self.ui.btn_expand.clicked.connect(lambda: self.min_and_max_window(self))

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

        #self.ui.btn_home.clicked.connect(self.print_sender)

    def fonts_gui_configuration(self):
        # title bar
        self.set_font(self.ui.title1_label, 12, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False, True)
        self.set_font(self.ui.title2_label, 12, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True, True)

        # menu
        menu_labels = [self.set_font(label, 12, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False, False) for label in
                       [self.ui.btn_home, self.ui.btn_profit, self.ui.btn_students, self.ui.btn_inventory,
                        self.ui.btn_mail, self.ui.btn_settings]]

        # home widgets
        # title
        home_widgets_labels = [self.set_font(label, 12, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False, True) for label in
                               [self.ui.title_students, self.ui.title_profit, self.ui.title_axies]]

        # data
        home_widgets_labels = [self.set_font(label, 40, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False, True) for label in
                               [self.ui.data_label_students, self.ui.data_label_profit, self.ui.data_label_axies]]

    def drop_shadow_gui_configuration(self):
        # shadow top bar
        self.set_drop_shadow(self.ui.top_bar)

        # shadow home widgets
        self.set_drop_shadow(self.ui.axies_widget, self.ui.profit_widget, self.ui.students_widget)

    def graph_configurations(self):
        self.students_goal_graphic = CircularProgress(200, 200, font_family='Saira')

        self.profit_graphic = BarGraph(250, 250, font_family='Saira')
        
        self.axies_graphic = HomeMarketFeature(200, 200)

        add_widget = [self.ui.graphics_layout.addWidget(widget) for widget in
                      [self.students_goal_graphic, self.profit_graphic, self.axies_graphic]]

    def set_work_in_progress_pages(self):

        work_pages = [self.ui.label_2, self.ui.label_3, self.ui.label_4, self.ui.label_5, self.ui.label_6]

        for v in work_pages:
            self.set_font(v, 25, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True, True)
            v.setText('Work in progress...')
    
    def show_add_pop_up(self):           
        # show
        self.pop_up.show()
        
    def load_home_info_thread_handle(self, initialization=False, after_add_popup=False, update=False) -> None:
        
        if initialization:
            self.load_info_worker = LoadHomeInfoWorker(initialization=True)
            
            self.load_info_worker.students_amount_signal.connect(self.students_amount_receive)
            self.load_info_worker.students_goal_percent_signal.connect(self.students_goal_percent_receive)
            self.load_info_worker.actual_month_signal.connect(self.actual_month_receive)
            self.load_info_worker.last_month_signal.connect(self.last_month_receive)
            self.load_info_worker.next_last_month_signal.connect(self.next_last_month_receive)
            self.load_info_worker.axie_amount_signal.connect(self.axie_amount_receive)
            self.load_info_worker.initalization_signal.connect(self.initialization_receive)
            
        elif after_add_popup:
            self.load_info_worker = LoadHomeInfoWorker(after_add_popup=True)
        elif update:
            self.load_info_worker = LoadHomeInfoWorker(update=True)
            
        self.load_info_worker.start()
        
        self.load_info_worker.finished.connect(self.home_info_setter)          
        
    def home_info_setter(self):
        print('setting')
        
        # set graph widgets infos
        self.students_goal_graphic.update_value(self.students_goal_percent_slot)
        self.profit_graphic.update_value(self.next_last_month_slot, self.last_month_slot, self.actual_month_slot)
        
        # set data view infos
        self.ui.data_label_students.setText(str(self.students_amount_slot))
        self.ui.data_label_profit.setText(str(self.actual_month_slot))
        self.ui.data_label_axies.setText(str(self.axie_amount_slot))
        
    def initialization_receive(self, value):
        self.initialization_slot = value
        
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
    #state signals
    initalization_signal = Signal(bool)
    after_add_popup_signal = Signal(bool)
    update_signal = Signal(bool)
    
    # crud signals
    students_amount_signal = Signal(int)
    students_goal_percent_signal = Signal(int)
    actual_month_signal  = Signal(int)
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
    
    """parametro para init if is initalization -> se for nao checar api e emitir
    signal it was first and worker again with api"""
    
    def run(self) -> None:
        print('working')
        
        # initialization -> just crud
        if self.initalization:
            print('initialization')
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
            
            self.initalization_signal.emit(True)
        
        """
        for todosscholars:
            
            while not api_up:
                use api e ve os return dados
                se != de api down:
                    api_up = true
                    
            check_daily
            check_las_day_hour, if +9am clear daily, 
                if new month clear actual month(check_daily) -> pass to last month and last to next-last
        """
    
    def get_students_amount(self) -> int:
        amount_students = self.students_db_handle.get_scholar_amount(DefaultTools.session_handle)
        
        return amount_students
    
    def get_students_goal_percent(self) -> int:
        daily_goal, daily_profit = self.students_db_handle.get_daily_goal_and_profit(DefaultTools.session_handle)
        
        percent = (daily_profit/daily_goal) * 100
        
        return percent
    
    def get_months_values(self) -> int:
        actual_value, last_value, next_last_value = self.students_db_handle.get_months_values(DefaultTools.session_handle)
        
        return actual_value, last_value, next_last_value      
    
    def get_axie_amount(self)  -> int:
        return self.acc_db_handle.get_axies_amount(DefaultTools.session_handle)
    

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
