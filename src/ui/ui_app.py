from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .style import Style
from resources import resource
from functions import UIFunctions


class Ui_App(object):
    def init_gui(self, app):
        app.setObjectName('app')

        # configs do app
        app.setWindowTitle('Axie Academy')
        app.resize(1200, 700)
        app.setMinimumSize(QSize(1200, 700))
        app.setMaximumSize(QSize(1200, 700))
        app.setWindowIcon(QIcon(QPixmap(':/img/img/logo.png')))

        # bg
        self.bg_frame = QFrame(app)
        self.bg_frame.setObjectName('bg_frame')
        self.bg_frame.setStyleSheet(Style.bg)

        self.bg_layout = QHBoxLayout(self.bg_frame)
        self.bg_layout.setObjectName('bg_layout')
        self.bg_layout.setContentsMargins(0, 0, 0, 0)
        self.bg_layout.setSpacing(0)

        # main frames
        self.nav_frame = QFrame(self.bg_frame)
        self.nav_frame.setObjectName('nav_frame')
        self.nav_frame.setMinimumWidth(220)
        self.nav_frame.setMaximumWidth(220)
        self.nav_frame.setStyleSheet(Style.nav_frame)
        self.bg_layout.addWidget(self.nav_frame)

        self.nav_layout = QVBoxLayout(self.nav_frame)
        self.nav_layout.setObjectName('nav_layout')
        self.nav_layout.setContentsMargins(0, 0, 5, 0)
        self.nav_layout.setSpacing(0)

        self.content_frame = QFrame(self.bg_frame)
        self.content_frame.setObjectName('content_frame')
        self.bg_layout.addWidget(self.content_frame)

        # user
        self.user_frame = QFrame(self.nav_frame)
        self.user_frame.setObjectName('user_frame')
        self.user_frame.setMaximumHeight(120)
        self.user_frame.setStyleSheet(Style.user_frame)
        self.nav_layout.addWidget(self.user_frame)

        # menu
        self.menu_frame = QFrame(self.nav_frame)
        self.menu_frame.setObjectName('menu_frame')
        self.menu_frame.setStyleSheet(Style.menu_frame)
        self.nav_layout.addWidget(self.menu_frame)

        self.menu_layout = QVBoxLayout(self.menu_frame)
        self.menu_layout.setAlignment(Qt.AlignTop | Qt.AlignRight)
        self.menu_layout.setSpacing(8)
        self.menu_layout.setContentsMargins(0, 20, 8, 0)

        # btns menu
        # temp
        btn_size = QSize(180, 40)

        self.btn_dash = QToolButton(self.menu_frame)
        self.btn_dash.setObjectName('btn_dash')
        self.btn_dash.setMinimumSize(btn_size)
        self.btn_dash.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn_dash.setText('   DASHBOARD')
        self.btn_dash.setStyleSheet(Style.btn_clicked)

        self.btn_reports = QToolButton(self.menu_frame)
        self.btn_reports.setObjectName('btn_reports')
        self.btn_reports.setMinimumSize(btn_size)
        self.btn_reports.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn_reports.setText('   REPORTS')
        self.btn_reports.setStyleSheet(Style.btn_default)

        self.btn_scholars = QToolButton(self.menu_frame)
        self.btn_scholars.setObjectName('btn_scholars')
        self.btn_scholars.setMinimumSize(btn_size)
        self.btn_scholars.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn_scholars.setText('   SCHOLARS')
        self.btn_scholars.setStyleSheet(Style.btn_default)

        self.btn_inventory = QToolButton(self.menu_frame)
        self.btn_inventory.setObjectName('btn_scholars')
        self.btn_inventory.setMinimumSize(btn_size)
        self.btn_inventory.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn_inventory.setText('   INVENTORY')
        self.btn_inventory.setStyleSheet(Style.btn_default)

        self.btn_settings = QToolButton(self.menu_frame)
        self.btn_settings.setObjectName('btn_settings')
        self.btn_settings.setMinimumSize(btn_size)
        self.btn_settings.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn_settings.setText('   SETTINGS')
        self.btn_settings.setStyleSheet(Style.btn_default)

        #paint
        new_image = QPixmap(':/img/img/dash_icon.svg')
        paint = QPainter(new_image)
        paint.setCompositionMode(QPainter.CompositionMode_SourceIn)
        paint.fillRect(new_image.rect(), '#F4F4F4')
        paint.end()

        icon = QIcon(new_image)     
        #icon.addFile(new_image, QSize(), QIcon.Normal, QIcon.Off)

        for btn in [self.btn_dash, self.btn_reports, self.btn_scholars, self.btn_inventory, self.btn_settings]:
            UIFunctions.set_font(btn,
                             10, ':/fonts/fonts/Montserrat-Medium.ttf',
                             bold=True)

            btn.setIcon(icon)
            btn.setIconSize(QSize(25, 25))
            btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            self.menu_layout.addWidget(btn)

        # version
        self.version_frame = QFrame(self.nav_frame)
        self.version_frame.setObjectName('version_frame')
        self.version_frame.setMaximumHeight(80)
        self.version_frame.setStyleSheet(Style.version_frame)
        self.nav_layout.addWidget(self.version_frame)

        self.version_layout = QVBoxLayout(self.version_frame)
        self.version_layout.setObjectName('version_layout')
        self.version_layout.setContentsMargins(0, 0, 0, 0)
        self.version_layout.setSpacing(0)

        self.version_label = QLabel(self.version_frame)
        self.version_label.setObjectName('version_label')
        self.version_label.setText('VERSION 1.0.1')
        self.version_label.setAlignment(Qt.AlignCenter)
        UIFunctions.set_font(self.version_label,
                             10, ':/fonts/fonts/Montserrat-Medium.ttf',
                             bold=True)
        self.version_layout.addWidget(self.version_label)

        app.setCentralWidget(self.bg_frame)
