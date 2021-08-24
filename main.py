import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# gui file
from src.ui_main import Ui_MainWindow

# gui functions
from src.ui_functions import UIFunctions


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.uifuncions = UIFunctions()

        # config window
        self.uifuncions.config_window(config_widget=self, title='', width=1160, height=652, resizeble=True, minimum_size=True)

        # toggle button
        self.ui.btn_toggle.clicked.connect(lambda: self.uifuncions.toggle_menu(self.ui.menu_container, 120, True))

        # show gui
        self.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
