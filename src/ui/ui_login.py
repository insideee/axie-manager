from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .app_style import stylesheet
import tools

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
        self.form_create_acc_gui()
        
        self.form_frame.addWidget(self.login_form)
        self.form_frame.addWidget(self.create_form)
        
        self.ask_create_acc_btn.clicked.connect(lambda: self.form_frame.setCurrentWidget(self.create_form))
        self.ask_have_acc_btn.clicked.connect(lambda: self.form_frame.setCurrentWidget(self.login_form))
        
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
        self.login_container_layout.setVerticalSpacing(4)
        
        self.create_title_login()
        
        self.login_container_layout.addWidget(self.title_container, 0, 0)

        self.create_login_entries()
        
        self.login_container_layout.addWidget(self.login_entries_container, 1, 0)
        
        self.create_login_btns()
        
        self.login_container_layout.addWidget(self.btns_container, 2, 0)
        
    def create_title_login(self):
        
        self.title_container = QWidget()
        self.title_container.setMaximumWidth(300)
        self.title_container.setMinimumHeight(100)
        
        self.title_container_layout = QGridLayout(self.title_container)
        self.title_container_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.title_container_layout.setSpacing(0)
        self.title_container_layout.setContentsMargins(0, 0, 0, 0)
        
        self.welcome_label = QLabel()
        self.welcome_label.setObjectName('welcome_label')
        self.welcome_label.setText('Welcome to')
        self.welcome_label.setStyleSheet(stylesheet['login_title_text'])
        self.title_container_layout.addWidget(self.welcome_label, 0, 0)
        
        tools.set_font(self.welcome_label,
                        12, ':/fonts/fonts/Montserrat-Medium.ttf',
                        bold=True)
        
        self.title_label = QLabel()
        self.title_label.setObjectName('title_label')
        self.title_label.setText('AXIE ACADEMY')
        self.title_label.setStyleSheet(stylesheet['login_title_text'])
        self.title_container_layout.addWidget(self.title_label, 1, 0)
        
        tools.set_font(self.title_label,
                        25, ':/fonts/fonts/Montserrat-SemiBold.ttf',
                        bold=True)
        
    def create_login_entries(self):
        
        self.login_entries_container = QWidget()
        self.login_entries_container.setMaximumWidth(300)
        
        self.entries_container_layout = QGridLayout(self.login_entries_container)
        self.entries_container_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.entries_container_layout.setSpacing(0)
        self.entries_container_layout.setContentsMargins(0, 0, 0, 0)
        
        self.email_entry_label = QLabel()
        self.email_entry_label.setObjectName('email_entry_label')
        self.email_entry_label.setText('Email')
        self.email_entry_label.setStyleSheet(stylesheet['login_info_entry'])
        self.entries_container_layout.addWidget(self.email_entry_label, 0, 0)
        
        self.email_entry = QLineEdit()
        self.email_entry.setObjectName('email_entry')
        self.email_entry.setMaximumWidth(300)
        self.email_entry.setMinimumHeight(30)
        self.email_entry.setStyleSheet(stylesheet['login_entry'])
        self.entries_container_layout.addWidget(self.email_entry, 1, 0)
        
        self.password_entry_label = QLabel()
        self.password_entry_label.setObjectName('password_entry_label')
        self.password_entry_label.setText('\nPassword')
        self.password_entry_label.setStyleSheet(stylesheet['login_info_entry'])
        self.entries_container_layout.addWidget(self.password_entry_label, 2, 0)
        
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setObjectName('password_entry')
        self.password_entry.setMaximumWidth(300)
        self.password_entry.setMinimumHeight(30)
        self.password_entry.setStyleSheet(stylesheet['login_entry'])
        self.entries_container_layout.addWidget(self.password_entry, 3, 0)
        
        for label in [self.email_entry_label, self.email_entry, self.password_entry, self.password_entry_label]:
            tools.set_font(label,
                        10, ':/fonts/fonts/Montserrat-Medium.ttf',
                        bold=True)
     
    def create_login_btns(self):
        
        self.btns_container = QWidget()
        
        self.btns_container_layout = QGridLayout(self.btns_container)
        self.btns_container_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.btns_container_layout.setSpacing(5)
        self.btns_container_layout.setRowMinimumHeight(0, 40)
        self.btns_container_layout.setContentsMargins(0, 0, 0, 0)
        
        # rememberme / forget password        
        self.remember_btn = QRadioButton()
        self.remember_btn.setText('Remember me')
        self.remember_btn.setStyleSheet(stylesheet['rememberme_btn'])
        self.btns_container_layout.addWidget(self.remember_btn, 0, 0, alignment=Qt.AlignLeft | Qt.AlignTop)
        
        self.forgot_pass = QPushButton()
        self.forgot_pass.setText('Forgot Password?')
        self.forgot_pass.setCursor(Qt.PointingHandCursor)
        self.forgot_pass.setStyleSheet(stylesheet['forgot_btn'])
        self.btns_container_layout.addWidget(self.forgot_pass, 0, 0, alignment=Qt.AlignRight | Qt.AlignTop)
        
        # login btn
        self.login_btn = QPushButton(self.login_form_container)
        self.login_btn.setObjectName('login_btn')
        self.login_btn.setMinimumWidth(300)
        self.login_btn.setMinimumHeight(40)
        self.login_btn.setText('LOGIN')
        self.login_btn.setStyleSheet(stylesheet['login_btn'])
        self.login_btn.setCursor(Qt.PointingHandCursor)
        self.login_btn.setFocus()
        self.btns_container_layout.addWidget(self.login_btn, 1, 0)
        
        # create acc
        self.create_acc_container = QWidget()
        self.create_acc_container.setObjectName('create_acc_container')
        
        self.create_acc_layout = QHBoxLayout(self.create_acc_container)
        self.create_acc_layout.setObjectName('create_acc_layout')
        self.create_acc_layout.setContentsMargins(0, 0, 0, 0)
        self.create_acc_layout.setAlignment(Qt.AlignHCenter)
        self.create_acc_layout.setSpacing(3)
        
        self.ask_create_acc_label = QLabel(self.create_acc_container)
        self.ask_create_acc_label.setObjectName('ask_create_acc_label')
        self.ask_create_acc_label.setText("Don't have a account?")
        self.ask_create_acc_label.setStyleSheet(stylesheet['login_question_label'])
        self.create_acc_layout.addWidget(self.ask_create_acc_label)
        
        self.ask_create_acc_btn = QPushButton(self.create_acc_container)
        self.ask_create_acc_btn.setObjectName('ask_create_acc_btn')
        self.ask_create_acc_btn.setCursor(Qt.PointingHandCursor)
        self.ask_create_acc_btn.setMaximumWidth(50)
        self.ask_create_acc_btn.setText('Signup')
        self.ask_create_acc_btn.setStyleSheet(stylesheet['login_question_btn'])
        self.create_acc_layout.addWidget(self.ask_create_acc_btn)
        
        self.btns_container_layout.addWidget(self.create_acc_container, 2, 0)
        
        for label in [self.remember_btn, self.forgot_pass, self.ask_create_acc_label, self.ask_create_acc_btn, self.login_btn]:
            tools.set_font(label,
                        10, ':/fonts/fonts/Montserrat-Medium.ttf',
                        bold=True)
        
    def form_create_acc_gui(self):
        self.create_form = QFrame(self.form_frame)
        self.create_form.setObjectName('create_form')
        
        self.create_form_layout = QVBoxLayout(self.create_form)
        self.create_form_layout.setObjectName('create_form_layout')
        self.create_form_layout.setAlignment(Qt.AlignCenter)
        self.create_form_layout.setContentsMargins(0, 0, 0, 0)
        self.create_form_layout.setSpacing(0)
        
        self.create_form_container = QFrame(self.create_form)
        self.create_form_container.setObjectName('create_form_container')
        self.create_form_layout.addWidget(self.create_form_container)
        
        self.create_container_layout = QGridLayout(self.create_form_container)
        self.create_container_layout.setObjectName('create_form_layout')
        self.create_container_layout.setContentsMargins(0, 0, 0, 0)
        self.create_container_layout.setSpacing(0)
        self.create_container_layout.setVerticalSpacing(4)
        
        self.create_acc_title()        
        self.create_container_layout.addWidget(self.create_title_container, 0, 0)
        
        self.create_acc_entries()
        self.create_container_layout.addWidget(self.create_entries_container, 1, 0)
        
        self.create_acc_btns()
        self.create_container_layout.addWidget(self.create_btns_container, 2, 0)
        
    def create_acc_title(self):
        
        self.create_title_container = QWidget()
        self.create_title_container.setMaximumWidth(300)
        self.create_title_container.setMinimumWidth(300)
        self.create_title_container.setMinimumHeight(100)
        
        self.create_title_container_layout = QGridLayout(self.create_title_container)
        self.create_title_container_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.create_title_container_layout.setSpacing(0)
        self.create_title_container_layout.setContentsMargins(0, 0, 0, 0)
        
        self.create_label = QLabel()
        self.create_label.setObjectName('create_label')
        self.create_label.setText('Create a')
        self.create_label.setStyleSheet(stylesheet['login_title_text'])
        self.create_title_container_layout.addWidget(self.create_label, 0, 0)
        
        tools.set_font(self.create_label,
                        12, ':/fonts/fonts/Montserrat-Medium.ttf',
                        bold=True)
        
        self.create_title_label = QLabel()
        self.create_title_label.setObjectName('create_title_label')
        self.create_title_label.setText('ACCOUNT')
        self.create_title_label.setStyleSheet(stylesheet['login_title_text'])
        self.create_title_container_layout.addWidget(self.create_title_label, 1, 0)
        
        tools.set_font(self.create_title_label,
                        25, ':/fonts/fonts/Montserrat-SemiBold.ttf',
                        bold=True)
        
    def create_acc_entries(self):
        
        self.create_entries_container = QWidget()
        self.create_entries_container.setMaximumWidth(300)
        
        self.create_entry_container_layout = QGridLayout(self.create_entries_container)
        self.create_entry_container_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.create_entry_container_layout.setSpacing(0)
        self.create_entry_container_layout.setContentsMargins(0, 0, 0, 0)
        
        self.create_username_entry_label = QLabel()
        self.create_username_entry_label.setObjectName('create_username_entry_label')
        self.create_username_entry_label.setText('Username')
        self.create_username_entry_label.setStyleSheet(stylesheet['login_info_entry'])
        self.create_entry_container_layout.addWidget(self.create_username_entry_label, 0, 0)
        
        self.create_username_entry = QLineEdit()
        self.create_username_entry.setObjectName('create_username_entry')
        self.create_username_entry.setMaximumWidth(300)
        self.create_username_entry.setMinimumHeight(30)
        self.create_username_entry.setStyleSheet(stylesheet['login_entry'])
        self.create_entry_container_layout.addWidget(self.create_username_entry, 1, 0)
        
        self.create_email_entry_label = QLabel()
        self.create_email_entry_label.setObjectName('create_email_entry_label')
        self.create_email_entry_label.setText('\nEmail')
        self.create_email_entry_label.setStyleSheet(stylesheet['login_info_entry'])
        self.create_entry_container_layout.addWidget(self.create_email_entry_label, 2, 0)
        
        self.create_email_entry = QLineEdit()
        self.create_email_entry.setObjectName('create_email_entry')
        self.create_email_entry.setMaximumWidth(300)
        self.create_email_entry.setMinimumHeight(30)
        self.create_email_entry.setStyleSheet(stylesheet['login_entry'])
        self.create_entry_container_layout.addWidget(self.create_email_entry, 3, 0)
        
        self.create_password_entry_label = QLabel()
        self.create_password_entry_label.setObjectName('create_password_entry_label')
        self.create_password_entry_label.setText('\nPassword')
        self.create_password_entry_label.setStyleSheet(stylesheet['login_info_entry'])
        self.create_entry_container_layout.addWidget(self.create_password_entry_label, 4, 0)
        
        self.create_password_entry = QLineEdit()
        self.create_password_entry.setEchoMode(QLineEdit.Password)
        self.create_password_entry.setObjectName('create_password_entry')
        self.create_password_entry.setMaximumWidth(300)
        self.create_password_entry.setMinimumHeight(30)
        self.create_password_entry.setStyleSheet(stylesheet['login_entry'])
        self.create_entry_container_layout.addWidget(self.create_password_entry, 5, 0)
        
        self.create_repassword_entry_label = QLabel()
        self.create_repassword_entry_label.setObjectName('create_repassword_entry_label')
        self.create_repassword_entry_label.setText('\nRetype Password')
        self.create_repassword_entry_label.setStyleSheet(stylesheet['login_info_entry'])
        self.create_entry_container_layout.addWidget(self.create_repassword_entry_label, 6, 0)
        
        self.create_repassword_entry = QLineEdit()
        self.create_repassword_entry.setEchoMode(QLineEdit.Password)
        self.create_repassword_entry.setObjectName('create_repassword_entry')
        self.create_repassword_entry.setMaximumWidth(300)
        self.create_repassword_entry.setMinimumHeight(30)
        self.create_repassword_entry.setStyleSheet(stylesheet['login_entry'])
        self.create_entry_container_layout.addWidget(self.create_repassword_entry, 7, 0)
        
        for label in [self.create_username_entry_label, self.create_username_entry, self.create_email_entry_label, 
                      self.create_email_entry, self.create_password_entry, self.create_password_entry_label,
                      self.create_repassword_entry, self.create_repassword_entry_label]:
            tools.set_font(label,
                        10, ':/fonts/fonts/Montserrat-Medium.ttf',
                        bold=True)
    
    def create_acc_btns(self):
        
        self.create_btns_container = QWidget()
        
        self.create_btns_container_layout = QGridLayout(self.create_btns_container)
        self.create_btns_container_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.create_btns_container_layout.setSpacing(5)
        self.create_btns_container_layout.setRowMinimumHeight(0, 70)
        self.create_btns_container_layout.setContentsMargins(0, 0, 0, 0)
        
        # create btn
        self.create_btn = QPushButton()
        self.create_btn.setObjectName('create_btn')
        self.create_btn.setMinimumWidth(300)
        self.create_btn.setMinimumHeight(40)
        self.create_btn.setText('CREATE')
        self.create_btn.setStyleSheet(stylesheet['login_btn'])
        self.create_btn.setCursor(Qt.PointingHandCursor)
        self.create_btn.setFocus()
        self.create_btns_container_layout.addWidget(self.create_btn, 0, 0, alignment=Qt.AlignBottom)
        
        # login acc
        self.have_acc_container = QWidget()
        self.have_acc_container.setObjectName('have_acc_container')
        
        self.have_acc_layout = QHBoxLayout(self.have_acc_container)
        self.have_acc_layout.setObjectName('have_acc_layout')
        self.have_acc_layout.setContentsMargins(0, 0, 0, 0)
        self.have_acc_layout.setAlignment(Qt.AlignHCenter)
        self.have_acc_layout.setSpacing(3)
        
        self.ask_have_acc_label = QLabel(self.have_acc_container)
        self.ask_have_acc_label.setObjectName('ask_have_acc_label')
        self.ask_have_acc_label.setText('Already have a account?')
        self.ask_have_acc_label.setStyleSheet(stylesheet['login_question_label'])
        self.have_acc_layout.addWidget(self.ask_have_acc_label)
        
        self.ask_have_acc_btn = QPushButton(self.have_acc_container)
        self.ask_have_acc_btn.setObjectName('ask_have_acc_btn')
        self.ask_have_acc_btn.setCursor(Qt.PointingHandCursor)
        self.ask_have_acc_btn.setMaximumWidth(50)
        self.ask_have_acc_btn.setText('Login')
        self.ask_have_acc_btn.setStyleSheet(stylesheet['login_question_btn'])
        self.have_acc_layout.addWidget(self.ask_have_acc_btn)
        
        self.create_btns_container_layout.addWidget(self.have_acc_container, 1, 0)
        
        for label in [self.ask_have_acc_label, self.ask_have_acc_btn, self.create_btn]:
            tools.set_font(label,
                        10, ':/fonts/fonts/Montserrat-Medium.ttf',
                        bold=True)