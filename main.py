import sys
from PySide2 import QtCore
from PySide2.QtWidgets import *

# gui file and gui functions
from src.ui_main import Ui_MainWindow
from src.functions import UIFunctions

# custom widgets
from src.custom_widgets import CircularProgress


class MainWindow(QMainWindow, UIFunctions):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
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

    def fonts_gui_configuration(self):
        # title bar
        self.set_font(self.ui.title1_label, 12, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False)
        self.set_font(self.ui.title2_label, 12, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True)

        # menu
        menu_labels = [self.set_font(label, 12, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False) for label in
                       [self.ui.btn_home, self.ui.btn_profit, self.ui.btn_students, self.ui.btn_inventory,
                        self.ui.btn_mail, self.ui.btn_settings]]

        # home widgets
        # title
        home_widgets_labels = [self.set_font(label, 12, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False) for label in
                               [self.ui.data_label_students, self.ui.title_students, self.ui.data_label_profit,
                                self.ui.title_profit, self.ui.data_label_axies, self.ui.title_axies]]

        # data
        home_widgets_labels = [self.set_font(label, 57, ':/font/fonts/Saira-Light.ttf', '#FFFFFF', False) for label in
                               [self.ui.data_label_students, self.ui.data_label_profit, self.ui.data_label_axies]]

    def drop_shadow_gui_configuration(self):
        # shadow top bar
        self.set_drop_shadow(self.ui.top_bar)

        # shadow home widgets
        self.set_drop_shadow(self.ui.axies_widget, self.ui.profit_widget, self.ui.students_widget)

    def graphics_configurations(self):
        self.students_goal_graphic = CircularProgress(200, 200, font_family='Saira')
        self.students_goal_graphic.set_value(90)

        self.axies_goal_graphic = CircularProgress(200, 200, font_family='Saira')
        self.axies_goal_graphic.set_value(20)

        self.profit_goal_graphic = CircularProgress(200, 200, font_family='Saira')
        self.profit_goal_graphic.set_value(20)

        add_widget = [self.ui.graphics_layout.addWidget(widget) for widget in
                      [self.students_goal_graphic, self.axies_goal_graphic, self.profit_goal_graphic]]


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
