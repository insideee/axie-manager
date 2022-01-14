from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import tools, api

class AddPopup(QFrame):
    
    def __init__(self, parent, pos_spawn, colorscheme):
        super(AddPopup, self).__init__(parent=parent)
            
        size = QSize(350, 300)
        
        self.colorscheme = colorscheme
        self.setObjectName('create_scholar_popup')
        
        # config
        self.setGeometry(QRect(pos_spawn, size))
        self.setMinimumSize(size)
        self.setMaximumSize(size)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setObjectName('main_layout')
        self.main_layout.setContentsMargins(5, 15, 15, 5)
        self.main_layout.setSpacing(0)
        
        self.exit_icon = tools.paint_image(image=':/img/img/exit_popup.svg', color=self.colorscheme['login']['main_color'],
                                          size=QSize(18, 18))
        self.exit_btn = QToolButton(self)
        self.exit_btn.setGeometry(325, 5, 20, 20)
        self.exit_btn.setStyleSheet(f"""background-color: {self.colorscheme['main colors']['widget_bg']};
                                        border: none;
                                        border-radius: 10px
                                    """)
        self.exit_btn.setIcon(self.exit_icon)
        self.exit_btn.setIconSize(QSize(18, 18))
        self.exit_btn.setCursor(Qt.PointingHandCursor)
        self.exit_btn.setMouseTracking(True)
        self.exit_btn.clicked.connect(self.exit_handle)

        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.WindowStaysOnTopHint | Qt.NoDropShadowWindowHint | Qt.Popup)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.form_frame_config()
        
    def form_frame_config(self):
        self.form_container = QFrame(self)
        self.form_container.setObjectName('form_container')
        self.form_container.setStyleSheet(f"""background-color: {self.colorscheme['main colors']['widget_bg']};
                                      border-radius: 10px
                                        """)
        self.main_layout.addWidget(self.form_container)
        
        self.form_frame_layout = QGridLayout(self.form_container)
        self.form_frame_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.form_frame_layout.setSpacing(0)
        self.form_frame_layout.setContentsMargins(0, 15, 0, 15)
        self.form_frame_layout.setVerticalSpacing(4)      
        
        self.create_form() 
        self.form_frame_layout.addWidget(self.create_acc_form, 0, 0)
        
        self.create_info_btn()
        self.form_frame_layout.addWidget(self.info_btn_container, 1, 0)
        
        self.exit_btn.raise_()
        
    def create_form(self):
        self.create_acc_form = QFrame()
        self.create_acc_form.setMinimumWidth(330)
        
        self.create_acc_form_layout = QGridLayout(self.create_acc_form)
        self.create_acc_form_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.create_acc_form_layout.setSpacing(0)
        self.create_acc_form_layout.setHorizontalSpacing(5)
        self.create_acc_form_layout.setContentsMargins(10, 0, 10, 0)
        
        title_style = f"""color: {self.colorscheme['login']['info_text']}
                                        """
        entry_style = f"""QLineEdit{{color: {self.colorscheme['login']['main_color']};
                                background-color: {self.colorscheme['main colors']['widget_bg']};
                                border: 1px solid {self.colorscheme['login']['info_text']};
                                border-radius: 7px}}
                                QLineEdit::focus{{border-bottom: 1px solid {self.colorscheme['login']['main_color']}}}
                                """
    
        self.ronin_entry_label = QLabel()
        self.ronin_entry_label.setObjectName('ronin_entry_label')
        self.ronin_entry_label.setText('Ronin address')
        self.ronin_entry_label.setStyleSheet(title_style)
        self.create_acc_form_layout.addWidget(self.ronin_entry_label, 0, 0, 1, -1)
        
        self.ronin_entry = QLineEdit()
        self.ronin_entry.setObjectName('ronin_entry')
        self.ronin_entry.setMaximumWidth(330)
        self.ronin_entry.setMinimumHeight(30)
        self.ronin_entry.setStyleSheet(entry_style)
        self.create_acc_form_layout.addWidget(self.ronin_entry, 1, 0, 1, -1)
        
        self.name_entry_label = QLabel()
        self.name_entry_label.setObjectName('name_entry_label')
        self.name_entry_label.setText('\nScholar name')
        self.name_entry_label.setStyleSheet(title_style)
        self.create_acc_form_layout.addWidget(self.name_entry_label, 2, 0, 1, -1)
        
        self.name_entry = QLineEdit()
        self.name_entry.setObjectName('name_entry')
        self.name_entry.setMaximumWidth(330)
        self.name_entry.setMinimumHeight(30)
        self.name_entry.setStyleSheet(entry_style)
        self.create_acc_form_layout.addWidget(self.name_entry, 3, 0, 1, -1)
        
        self.percent_label = QLabel()
        self.percent_label.setObjectName('percent_label')
        self.percent_label.setText('\nScholar gains %')
        self.percent_label.setStyleSheet(title_style)
        self.create_acc_form_layout.addWidget(self.percent_label, 4, 0, 1, -1)
        
        self.percent_slider_entry = QLineEdit()
        self.percent_slider_entry.setObjectName('percent_slider_entry')
        self.percent_slider_entry.setMaximumWidth(30)
        self.percent_slider_entry.setMinimumHeight(30)
        self.percent_slider_entry.setAlignment(Qt.AlignCenter)
        self.percent_slider_entry.setStyleSheet(entry_style)
        self.percent_slider_entry.setText('0')
        self.percent_slider_entry.textChanged.connect(self.change_slider_value)
        self.create_acc_form_layout.addWidget(self.percent_slider_entry, 5, 0, 1, 1)
        
        self.percent_slider = QSlider(Qt.Horizontal)
        self.percent_slider.setMinimum(0)
        self.percent_slider.setMaximum(100)
        self.percent_slider.setMinimumWidth(275)
        self.percent_slider.setMinimumHeight(20)
        self.percent_slider.setStyleSheet(f"""QSlider::groove:horizontal{{
                                                background: {self.colorscheme['login']['info_text']};
                                                border-radius: 1px;
                                                height: 5px;
                                                position: absolute;
                                                margin: 2px 0;
                                                left: 4px; right: 4px
                                            }}
                                            QSlider::handle:horizontal{{
                                                background: white;
                                                border: 1px solid {self.colorscheme['login']['info_text']};
                                                border-radius: 3px;
                                                width: 15px;
                                                margin: -5px 0;
                                            }}
                                            QSlider::add-page:horizontal {{
                                                background: {self.colorscheme['login']['info_text']};
                                            }}
                                            QSlider::sub-page:horizontal {{
                                            background: {self.colorscheme['login']['main_color']};
                                            }}
                                          """)
        self.percent_slider.valueChanged.connect(lambda: self.percent_slider_entry.setText(str(self.percent_slider.value())))
        self.create_acc_form_layout.addWidget(self.percent_slider, 5, 1, 1, 4)
        
        for font in [self.ronin_entry_label, self.ronin_entry,
                     self.name_entry_label, self.name_entry,
                     self.percent_label, self.percent_slider_entry]:
            tools.set_font(font,
                        10, ':/fonts/fonts/Montserrat-Medium.ttf',
                        bold=True)
            
    def create_info_btn(self):
        self.info_btn_container = QFrame()
        self.info_btn_container.setMinimumWidth(330)
        
        self.info_btn_layout = QGridLayout(self.info_btn_container)
        self.info_btn_layout.setAlignment(Qt.AlignCenter)
        self.info_btn_layout.setSpacing(0)
        self.info_btn_layout.setHorizontalSpacing(5)
        self.info_btn_layout.setContentsMargins(10, 0, 10, 0)
        
        self.info_label = QLabel()
        self.info_label.setObjectName('info_label_create_scholar')
        self.info_label.setMinimumSize(QSize(310, 30))
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet(f"""background-color: {self.colorscheme['main colors']['widget_bg']};
                                      color: {self.colorscheme['login']['second_color']}
                                                """)
        self.info_btn_layout.addWidget(self.info_label, 0, 0)
        
        self.create_btn = QPushButton()
        self.create_btn.setObjectName('create_btn')
        self.create_btn.setMinimumWidth(310)
        self.create_btn.setMinimumHeight(40)
        self.create_btn.setText('CREATE')
        self.create_btn.setStyleSheet(f"""QPushButton{{color: {self.colorscheme['main colors']['widget_bg']};
                                background-color: {self.colorscheme['login']['main_color']};
                                border: 1px solid {self.colorscheme['login']['info_text']};
                                border-radius: 7px}}
                                QPushButton::pressed{{background-color: {self.colorscheme['login']['click_btn']};}}
                                """)
        self.create_btn.setCursor(Qt.PointingHandCursor)
        self.create_btn.setFocus()
        self.info_btn_layout.addWidget(self.create_btn, 1, 0)
        self.create_btn.clicked.connect(self.create_request)
            
    def change_slider_value(self):
        try:
           self.percent_slider.setValue(int(self.percent_slider_entry.text()))
        except ValueError:
            self.percent_slider.setValue(0)
            
    def create_request(self):
        tools.init_loading_gif(self.info_label, ':/img/img/widget_loading.gif')
        
        if len(self.ronin_entry.text()) == 0 or \
            len(self.name_entry.text()) == 0:
                self.info_label.setText('All fields are required')
                return
        
        token = api.get_token(self)
        
        request = [{'endpoint': '/account',
                    'headers': {'Authorization': f'Bearer {token}'},
                    'params': None,
                    'json': {'ronin_address': self.ronin_entry.text(),
                             'player_name': self.name_entry.text(),
                             'scholar_earns_percent': self.percent_slider.value()},
                    'data': None,
                    'method': 'POST'}]
        self.request_thread = api.RequestThread(*request)
        self.request_thread.start()
        self.request_thread.data.connect(self.data_request_receiver)
        self.request_thread.finished.connect(self.request_handle)
    
    def data_request_receiver(self, response):
        print(response)
        self.response = response
        
    def request_handle(self):
        timer = QTimer()
        if type(self.response) == list and len(self.response) > 0:
            response = self.response[0]
        
            if response['status_code'] == 201:
                self.info_label.setStyleSheet(f"""color: {self.colorscheme['login']['main_color']}
                                                """)
                timer.singleShot(1500, lambda: self.close())
           
            self.info_label.setText(response['detail'])   
       
        else:
           self.info_label.setText('Error, try again.') 
    
    def exit_handle(self):
        self.close()
        