import sys
from PySide6.QtCore import QTimer
from PySide6.QtGui import QMouseEvent, QMovie
from PySide6.QtWidgets import QLabel, QLineEdit, QMainWindow, QApplication

import api
from ui import Ui_App
from ui.app_style import stylesheet

class App(QMainWindow):

    def __init__(self) -> None:
        super(App, self).__init__()
        self.ui = Ui_App()
        self.ui.init_gui(self)

        # variables
        self.token = None
        self.response = None
        self.request_thread = None

        # login page config
        # link create and login btns to pages
        self.ui.login_page.ask_create_acc_btn.clicked.connect(self.link_login_btns_pages)
        self.ui.login_page.ask_have_acc_btn.clicked.connect(self.link_login_btns_pages)

        # login
        self.ui.login_page.login_btn.clicked.connect(self.login)

        # create
        self.ui.login_page.create_btn.clicked.connect(self.create_user)
        self.ui.login_page.create_password_entry.textChanged.connect(
            lambda: self.realtime_password_validator(entry=self.ui.login_page.create_password_entry,
                                                            info_entry=self.ui.login_page.create_password_entry_label))
        self.ui.login_page.create_repassword_entry.textChanged.connect(
            lambda: self.realtime_password_validator(entry=self.ui.login_page.create_repassword_entry,
                                                            info_entry=self.ui.login_page.create_repassword_entry_label))

    def mousePressEvent(self, event: QMouseEvent) -> None:

        # remove cursor when search lose focus
        focus_widget = QApplication.focusWidget()

        if hasattr(focus_widget, 'objectName'):
            if focus_widget.objectName() == 'search_entry':
                focus_widget.clearFocus()

        return super().mousePressEvent(event)

    def login(self):
        self.init_loading(qlabel=self.ui.login_page.info_label)
        self.ui.login_page.info_label.setStyleSheet(stylesheet['info_message_negative'])
        
        if len(self.ui.login_page.email_entry.text()) == 0 or \
                self.ui.login_page.password_entry.text() == 0:
                    
            self.ui.login_page.info_label.setText('All fields are required')
            return None

        request = [{'endpoint': '/login',
                    'headers': None,
                    'params': None,
                    'data': {'username': self.ui.login_page.email_entry.text(),
                               'password': self.ui.login_page.password_entry.text()},
                    'json': None,
                    'method': 'POST'}]
        
        self.request_thread_creator(self.login_handle, *request)
    
    def login_handle(self):
        timer = QTimer()
        if type(self.response) == list and len(self.response) > 0:
            response = self.response[0]
            
            if response['status_code'] == 200:
                self.ui.login_page.info_label.setStyleSheet(stylesheet['info_message_positive'])
                response['detail'] = 'Successfuly logged in'
                timer.singleShot(2000, lambda: self.goto_dash_reset_entries())
                self.token = response['access_token']
            
            elif response['status_code'] == 404:
                self.ui.login_page.info_label.setStyleSheet(stylesheet['info_message_negative'])
                
            self.ui.login_page.info_label.setText(response['detail'])
        
        else:
            self.ui.login_page.info_label.setStyleSheet(stylesheet['info_message_negative'])
            self.ui.login_page.info_label.setText('Error, try again.')

    def create_user(self):
        self.init_loading(qlabel=self.ui.login_page.create_info_label)
        self.ui.login_page.create_info_label.setStyleSheet(stylesheet['info_message_negative'])

        if len(self.ui.login_page.create_username_entry.text()) == 0 or \
                self.ui.login_page.create_email_entry.text() == 0 or \
                self.ui.login_page.create_password_entry.text() == 0:
            self.ui.login_page.create_info_label.setText('All fields are required')
            return

        request = [{'endpoint': '/users',
                    'headers': None,
                    'params': None,
                    'data': None,
                    'json': {'name': self.ui.login_page.create_username_entry.text(),
                            'email': self.ui.login_page.create_email_entry.text(),
                            'password': self.ui.login_page.create_password_entry.text()},
                    'method': 'POST'}]
        
        self.request_thread_creator(self.create_user_handle, *request)
              
    def create_user_handle(self):
        
        if type(self.response) == list and len(self.response) > 0:
            timer = QTimer()
            response = self.response[0]
            
            if response['status_code'] == 422:
                if type(response['detail']) == list:
                    for item in response['detail']:
                        response['detail'] = item['msg'].capitalize()

            if response['status_code'] == 201:
                self.ui.login_page.create_info_label.setStyleSheet(stylesheet['info_message_positive'])
                response['detail'] = 'Succesfully created. Please login'
                timer.singleShot(1500, lambda: self.goto_login_reset_entries(email=response['email']))

            timer.singleShot(
                1000, lambda: self.ui.login_page.create_info_label.setText(response['detail']))
        else:
            self.ui.login_page.create_info_label.setStyleSheet(stylesheet['info_message_negative'])
            self.ui.login_page.create_info_label.setText('Error, try again.')
    
    def request_thread_creator(self, connect_to, *args):
        self.request_thread = api.RequestThread(*args)
        self.request_thread.start()
        self.request_thread.data.connect(self.data_request_receiver)
        self.request_thread.finished.connect(connect_to)
    
    def data_request_receiver(self, data):
        self.response = data
        print(self.response)
        return
    
    def realtime_password_validator(self, entry: QLineEdit, info_entry: QLabel):
        if entry.objectName() == 'create_password_entry':
            if len(entry.text()) < 8:
                entry.setStyleSheet(stylesheet['login_entry_invalid'])
                info_entry.setStyleSheet(
                    stylesheet['login_info_entry_invalid'])
            else:
                entry.setStyleSheet(stylesheet['login_entry'])
                info_entry.setStyleSheet(stylesheet['login_info_entry'])

            if len(self.ui.login_page.create_repassword_entry.text()) > 0:
                self.ui.login_page.create_repassword_entry.setStyleSheet(stylesheet['login_entry_invalid'])
                self.ui.login_page.create_repassword_entry.setText('')
                self.ui.login_page.create_repassword_entry_label.setStyleSheet(stylesheet['login_info_entry_invalid'])
        else:
            if len(self.ui.login_page.create_password_entry.text()) < 8 or entry.text() != self.ui.login_page.create_password_entry.text():
                entry.setStyleSheet(stylesheet['login_entry_invalid'])
                info_entry.setStyleSheet(
                    stylesheet['login_info_entry_invalid'])
            else:
                entry.setStyleSheet(stylesheet['login_entry'])
                info_entry.setStyleSheet(stylesheet['login_info_entry'])

    def init_loading(self, qlabel: QLabel):
        self.loading_gif = QMovie(
            ':/img/img/small_loading.gif')
        self.loading_gif.start()
        qlabel.setText('')
        qlabel.setMovie(self.loading_gif)

    def link_login_btns_pages(self):

        if self.sender().objectName() == 'ask_create_acc_btn':
            self.goto_create_account_reset_entries()
        else:
            self.goto_login_reset_entries()

    def goto_create_account_reset_entries(self):
        self.ui.login_page.form_frame.setCurrentWidget(self.ui.login_page.create_form)
        self.ui.login_page.email_entry.setText('')
        self.ui.login_page.password_entry.setText('')
        self.ui.login_page.info_label.setText('')

    def goto_login_reset_entries(self, email: str = ''):

        self.ui.login_page.email_entry.setText(email)
        if len(email) > 0:
            self.ui.login_page.password_entry.setFocus()
        self.ui.login_page.form_frame.setCurrentWidget(
            self.ui.login_page.login_form)
        self.ui.login_page.form_frame.setCurrentWidget(self.ui.login_page.login_form)
        self.ui.login_page.create_info_label.setText('')
        self.ui.login_page.create_email_entry.setText('')
        self.ui.login_page.create_username_entry.setText('')
        self.ui.login_page.create_password_entry.setText('')
        self.ui.login_page.create_repassword_entry.setText('')

        # reset stylesheet
        self.ui.login_page.create_password_entry.setStyleSheet(stylesheet['login_entry'])
        self.ui.login_page.create_repassword_entry.setStyleSheet(stylesheet['login_entry'])
        self.ui.login_page.create_password_entry_label.setStyleSheet(stylesheet['login_info_entry'])
        self.ui.login_page.create_repassword_entry_label.setStyleSheet(stylesheet['login_info_entry'])

    def goto_dash_reset_entries(self):
        self.ui.main_pages.setCurrentWidget(self.ui.app_page)
        self.ui.login_page.email_entry.setText('')
        self.ui.login_page.password_entry.setText('')
        self.ui.login_page.info_label.setText('')


def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
