import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# gui file
from src.ui_main import Ui_MainWindow
# resource file
import src.resources_rc

# gui functions
from src.ui_functions import UIFunctions

class MainWindow(QMainWindow, UIFunctions):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # center and config window
        self.config_window(config_widget=self, title='', width=1200, height=680, resizeble=True,
                                      minimum_size=True)
        # remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # toggle button
        self.ui.btn_toggle.clicked.connect(lambda: self.toggle_menu(self.ui.menu_container, 120, True))

        # exit
        self.ui.btn_exit.clicked.connect(lambda: sys.exit(1))

        # link button -> pages
        self.link_pages(self.ui.pages_container,
                                   list_btn=[self.ui.btn_home, self.ui.btn_profit, self.ui.btn_students,
                                             self.ui.btn_inventory,
                                             self.ui.btn_mail, self.ui.btn_settings],
                                   list_pages=[self.ui.home_page, self.ui.profit_page, self.ui.students_page,
                                               self.ui.inventory_page,
                                               self.ui.mail_page, self.ui.settings_page])

        # set fonts family and colors
        self.set_font(self.ui.title1_label, 12, ':/font/fonts/Saira-Light.ttf', 'white')

        # show gui
        self.show()

        def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton:
                self.__press_pos = event.pos()  # remember starting position

        def mouseReleaseEvent(self, event):
            if event.button() == Qt.LeftButton:
                self.__press_pos = None

        def mouseMoveEvent(self, event):
            if self.__press_pos:  # follow the mouse
                self.move(self.pos() + (event.pos() - self.__press_pos))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
