import sys
from PySide2 import QtCore
from PySide2.QtWidgets import *

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

        self.pop_up = None

        # window configs
        self.window_gui_configuration()

        # button configs
        self.btn_gui_configuration()

        # fonts configs
        self.fonts_gui_configuration()

        # drop shadow configs
        self.drop_shadow_gui_configuration()

        # home page graphics configuration
        self.graphics_configurations()

        # work in progress
        self.set_work_in_progress_pages()

        # show gui
        self.show()

    def window_gui_configuration(self):
        # center and config window
        self.config_window(config_widget=self, title='', width=1200, height=680, resizeble=True,
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
        self.ui.btn_minimize.clicked.connect(self.add_pop_up)
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
                               [self.ui.data_label_students, self.ui.title_students, self.ui.data_label_profit,
                                self.ui.title_profit, self.ui.data_label_axies, self.ui.title_axies]]

        # data
        home_widgets_labels = [self.set_font(label, 40, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False, True) for label in
                               [self.ui.data_label_students, self.ui.data_label_profit, self.ui.data_label_axies]]

    def drop_shadow_gui_configuration(self):
        # shadow top bar
        self.set_drop_shadow(self.ui.top_bar)

        # shadow home widgets
        self.set_drop_shadow(self.ui.axies_widget, self.ui.profit_widget, self.ui.students_widget)

    def graphics_configurations(self):
        self.students_goal_graphic = CircularProgress(200, 200, font_family='Saira')
        self.students_goal_graphic.set_value(79)

        self.profit_graphic = BarGraph(250, 250, font_family='Saira')
        self.profit_graphic.set_shadow(True)

        # temporary
        self.ui.data_label_profit.setText('2100')


        self.axies_graphic = HomeMarketFeature(200, 200)

        add_widget = [self.ui.graphics_layout.addWidget(widget) for widget in
                      [self.students_goal_graphic, self.profit_graphic, self.axies_graphic]]

    def set_work_in_progress_pages(self):

        work_pages = [self.ui.label_2, self.ui.label_3, self.ui.label_4, self.ui.label_5, self.ui.label_6]

        for v in work_pages:
            self.set_font(v, 25, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True, True)
            v.setText('Work in progress...')
    
    def add_pop_up(self):
        self.pop_up = AddPopUp()

        # config
        self.config_window(config_widget=self.pop_up, title='', width=400, height=300, resizeble=False, 
                            minimum_size=True)
        self.pop_up.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.pop_up.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # font config
        label_list = [self.pop_up.ui.label, self.pop_up.ui.label_2, self.pop_up.ui.label_3, self.pop_up.ui.label_4]
        entry_list = [self.pop_up.ui.entry_line, self.pop_up.ui.entry_line_2, self.pop_up.ui.entry_line_3, self.pop_up.ui.entry_line_4]
        
        for label in label_list:
            self.set_font(label, 10, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True, True)

        for label in entry_list:
            self.set_font(label, 10, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', False, False)

        self.set_font(self.pop_up.ui.add, 10, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', False, False)
        
        # show
        self.pop_up.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
