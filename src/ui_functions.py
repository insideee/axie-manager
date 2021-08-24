import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from screeninfo import get_monitors


class UIFunctions:

    def __init__(self) -> None:
        pass

    @staticmethod
    def config_window(**kwargs) -> None:

        try:
            screen_width, screen_height = 0, 0

            for monitor in get_monitors():
                if monitor.width > screen_width and monitor.height > screen_height:
                    screen_width = monitor.width
                    screen_height = monitor.height

            x_cords = int(screen_width / 2 - kwargs['width'] / 2)
            y_cords = int(screen_height / 2 - kwargs['height'] / 2)

            kwargs['config_widget'].setWindowTitle(kwargs['title'])
            kwargs['config_widget'].setGeometry(x_cords, y_cords, kwargs['width'], kwargs['height'])
            # disabled self.setToolTip(tooltip)
            app_icon = QIcon('./image/favicon2.ico')
            kwargs['config_widget'].setWindowIcon(app_icon)

        except Exception as ex:
            print(f'Error: {ex}')
            sys.exit(1)

        for k, v in kwargs.items():
            if k == 'resizable':
                if not v:
                    kwargs['config_widget'].setMinimumSize(QSize(kwargs['width'], kwargs['height']))
                    kwargs['config_widget'].setMaximumSize(QSize(kwargs['width'], kwargs['height']))

            if k == 'minimum_size':
                if v:
                    kwargs['config_widget'].setMinimumSize(QSize(kwargs['width'], kwargs['height']))

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







