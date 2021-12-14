from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .ui_app import App
from .ui_login import Login


class Ui_App(object):
    def init_gui(self, app):
        app.setObjectName('app')

        # configs do app
        app.setWindowTitle(' ')
        app.setMinimumSize(QSize(1200, 700))
        # app.setMaximumSize(QSize(1200, 700))
        app.setWindowIcon(QIcon(QPixmap(':/img/img/logo.png')))
        app.setGeometry(QStyle.alignedRect(
            Qt.LeftToRight,
            Qt.AlignCenter,
            app.size(),
            QGuiApplication.primaryScreen().availableGeometry(),
        ))

        self.main_pages = QStackedWidget(app)
        self.main_pages.setObjectName('main_pages')

        app.setCentralWidget(self.main_pages)

        self.login_page = Login()
        self.app_page = App()
        self.main_pages.addWidget(self.login_page)
        self.main_pages.addWidget(self.app_page)

        self.main_pages.setCurrentWidget(self.login_page)
