from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .app_style import stylesheet

class Login(QFrame):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setObjectName('login_main_layout')
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        # bg
        self.bg_frame = QFrame(self)
        self.bg_frame.setObjectName('bg_login_frame')
        self.bg_frame.setStyleSheet(stylesheet['login_bg'])
        self.main_layout.addWidget(self.bg_frame)

        self.bg_layout = QHBoxLayout(self.bg_frame)
        self.bg_layout.setObjectName('bg_login_layout')
        self.bg_layout.setContentsMargins(0, 0, 0, 0)
        self.bg_layout.setSpacing(0)
        
        # main frames
        self.form_frame = QStackedWidget(self.bg_frame)
        self.form_frame.setObjectName('form_frame')
        self.form_frame.setMaximumWidth(700)
        self.bg_layout.addWidget(self.form_frame)
        
        self.logo_frame = QFrame(self.bg_frame)
        self.logo_frame.setObjectName('logo_frame')
        self.logo_frame.setMinimumWidth(740)
        self.logo_frame.setStyleSheet(stylesheet['logo_login_frame'])
        self.bg_layout.addWidget(self.logo_frame)
        
        # init gui
        self.form_login_gui()
        
        self.form_frame.addWidget(self.login_form)
        self.form_frame.setCurrentWidget(self.login_form)
        
    def form_login_gui(self):
        self.login_form = QFrame(self.form_frame)
        self.login_form.setObjectName('login_form')
        
        self.login_form_layout = QVBoxLayout(self.login_form)
        self.login_form_layout.setObjectName('login_form_layout')
        self.login_form_layout.setAlignment(Qt.AlignCenter)
        self.login_form_layout.setContentsMargins(0, 0, 0, 0)
        self.login_form_layout.setSpacing(0)
        
        self.login_form_container = QFrame(self.login_form)
        self.login_form_container.setObjectName('login_form_container')
        self.login_form_layout.addWidget(self.login_form_container)
        
        self.login_container_layout = QGridLayout(self.login_form_container)
        self.login_container_layout.setObjectName('login_form_layout')
        self.login_container_layout.setContentsMargins(0, 0, 0, 0)
        self.login_container_layout.setSpacing(0)        
        
        self.welcome_label = QLabel(self.login_form_container)
        self.welcome_label.setObjectName('welcome_label')
        self.welcome_label.setText('Welcome to')
        self.welcome_label.setStyleSheet(stylesheet['login_title_text'])
        self.login_container_layout.addWidget(self.welcome_label, 0, 0)
        
        self.title_label = QLabel(self.login_form_container)
        self.title_label.setObjectName('title_label')
        self.title_label.setText('Axie Manager')
        self.title_label.setStyleSheet(stylesheet['login_title_text'])
        self.login_container_layout.addWidget(self.title_label, 1, 0)
        
        self.email_entry_label = QLabel(self.login_form_container)
        self.email_entry_label.setObjectName('email_entry_label')
        self.email_entry_label.setText('Email')
        self.email_entry_label.setStyleSheet(stylesheet['login_info_entry'])
        self.login_container_layout.addWidget(self.email_entry_label, 2, 0)
        
        self.email_entry = QLineEdit(self.login_form_container)
        self.email_entry.setObjectName('email_entry')
        self.email_entry.setMaximumWidth(300)
        self.email_entry.setMinimumHeight(30)
        self.email_entry.setStyleSheet(stylesheet['login_entry'])
        self.login_container_layout.addWidget(self.email_entry, 3, 0)
        
        self.password_entry_label = QLabel(self.login_form_container)
        self.password_entry_label.setObjectName('password_entry_label')
        self.password_entry_label.setText('Password')
        self.password_entry_label.setStyleSheet(stylesheet['login_info_entry'])
        self.login_container_layout.addWidget(self.password_entry_label, 4, 0)
        
        self.password_entry = QLineEdit(self.login_form_container)
        self.password_entry.setObjectName('password_entry')
        self.password_entry.setMaximumWidth(300)
        self.password_entry.setMinimumHeight(30)
        self.password_entry.setStyleSheet(stylesheet['login_entry'])
        self.login_container_layout.addWidget(self.password_entry, 5, 0)
        
        self.login_btn = QPushButton(self.login_form_container)
        self.login_btn.setObjectName('login_btn')
        self.login_btn.setMinimumWidth(300)
        self.login_btn.setMinimumHeight(30)
        self.login_btn.setText('LOGIN')
        self.login_btn.setStyleSheet(stylesheet['login_btn'])
        self.login_btn.setCursor(Qt.PointingHandCursor)
        self.login_container_layout.addWidget(self.login_btn, 6, 0)
        
