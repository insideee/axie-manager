import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

from functools import partial


class UIFunctions(QWidget):

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

    def btn_style_handle(self, *args, **kwargs) -> None:

        if type(kwargs['list_btn']) == list:
            try:
                for i in range(0, len(kwargs['list_btn'])):
                    kwargs['list_btn'][i].clicked.connect(self.btn_style_applyer)

            except IndexError as ex:
                print(ex)

    def btn_style_applyer(self):
        default_style = 'background-color: #1E2226; border-radius: 0px; padding-left: 15px; color: #FFFFFF;'
        clicked_style = 'background-color: #303840; border-left: 2px solid  #E64C3C; border-radius: 0px; padding-left: 15px; color: #FFFFFF;'

        sender = self.sender()

        if sender.objectName() == 'btn_settings':
            parent = self.sender().parent().parent()
        else:
            parent = self.sender().parent()

        for btn in parent.findChildren(QToolButton):
            if btn.objectName() != sender.objectName() and btn.objectName() != 'btn_toggle':
                btn.setStyleSheet(default_style)
            elif btn.objectName() != 'btn_toggle':
                btn.setStyleSheet(clicked_style)

    @staticmethod
    def set_font(qwidget: QWidget, size: int, font_path: str, color: str, bold: bool, change_color: bool) -> None:

        # add font to app database
        font_id = QtGui.QFontDatabase.addApplicationFont(f'{font_path}')
        font_name = QtGui.QFontDatabase.applicationFontFamilies(font_id)

        # get font name
        font = QFont(font_name[0])
        font.setPointSize(size)
        font.setBold(bold)
        # set color and font
        if change_color:
            qwidget.setStyleSheet('color:' + f'{color}')
        qwidget.setFont(font)

    @staticmethod
    def min_and_max_window(main_window: QMainWindow) -> None:

        state = main_window.isMaximized()

        if state:
            main_window.showNormal()
        else:
            main_window.showMaximized()

    @staticmethod
    def set_drop_shadow(*args: QWidget) -> None:

        for element in args:
            drop_shadow = QtWidgets.QGraphicsDropShadowEffect(element)
            drop_shadow.setBlurRadius(6)
            drop_shadow.setOffset(0)
            drop_shadow.setColor(QtGui.QColor(0, 0, 0, 90))
            element.setGraphicsEffect(drop_shadow)
