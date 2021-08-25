import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from functools import partial


class UIFunctions(QWidget):

    # for draggable reasons
    def __init__(self) -> None:
        super(UIFunctions, self).__init__()
        self.__press_pos = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.__press_pos = event.pos()  # remember starting position

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.__press_pos = None

    def mouseMoveEvent(self, event):
        if self.__press_pos:  # follow the mouse
            self.move(self.pos() + (event.pos() - self.__press_pos))

    @staticmethod
    def config_window(**kwargs) -> None:

        window = kwargs['config_widget'].window()
        window.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                window.size(),
                QtGui.QGuiApplication.primaryScreen().availableGeometry(),
            ),
        )

        window.setWindowTitle(kwargs['title'])
        app_icon = QIcon('./image/favicon2.ico')
        window.setWindowIcon(app_icon)

        for k, v in kwargs.items():
            if k == 'resizable':
                if not v:
                    window.setMinimumSize(QSize(kwargs['width'], kwargs['height']))
                    window.setMaximumSize(QSize(kwargs['width'], kwargs['height']))

            if k == 'minimum_size':
                if v:
                    window.setMinimumSize(QSize(kwargs['width'], kwargs['height']))

    @staticmethod
    def toggle_menu(ui_widget: QWidget, max_width: int, enable: bool) -> None:
        if enable:

            # get width
            width = ui_widget.width()
            max_extend = max_width
            standard = 52

            if width == 52:
                width_extend = max_extend
            else:
                width_extend = standard

            ui_widget.animation = QPropertyAnimation(ui_widget, b'minimumWidth')
            ui_widget.animation.setDuration(400)
            ui_widget.animation.setStartValue(width)
            ui_widget.animation.setEndValue(width_extend)
            ui_widget.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            ui_widget.animation.start()

    @staticmethod
    def link_pages(*args, **kwargs) -> None:
        try:

            for i in range(0, len(kwargs['list_btn'])):
                partial_func = partial(args[0].setCurrentWidget, kwargs['list_pages'][i])
                kwargs['list_btn'][i].clicked.connect(partial_func)

        except Exception as ex:
            print(f'Error: {ex}')
            sys.exit(1)

    @staticmethod
    def set_font(qwidget: QWidget, size: int, font_path: str, color: str, bold: bool) -> None:

        # add font to app database
        id = QtGui.QFontDatabase.addApplicationFont(f'{font_path}')
        font_name = QtGui.QFontDatabase.applicationFontFamilies(id)

        # get font name
        font = QFont(font_name[0])
        font.setPointSize(size)
        font.setBold(bold)
        # set color and font
        qwidget.setStyleSheet('color:' + f'{color}')
        qwidget.setFont(font)

    @staticmethod
    def min_and_max_window(main_window: QMainWindow):

        state = main_window.isMaximized()

        if state:
            main_window.showNormal()
        else:
            main_window.showMaximized()
