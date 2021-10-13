import PySide2
from PySide2 import QtCore
from PySide2.QtGui import QMovie, QPaintEvent, QPainter, QColor, QPen, QFont
from PySide2.QtWidgets import QLabel, QMessageBox, QWidget, QGraphicsDropShadowEffect
from PySide2.QtCore import QAbstractAnimation, QPoint, QRect, QThread, QTimer, Qt, QSize, QPropertyAnimation, Signal
from datetime import datetime
import os

try:
    from custom_widgets.ui import Ui_main
    from functions import UIFunctions
    from api import FullData, AccAxie
    from model import DefaultTools, Account, Scholar
except ModuleNotFoundError:
    from src.custom_widgets.ui import Ui_main
    from src.functions import UIFunctions
    from src.api import FullData, AccAxie
    from src.model import DefaultTools, Account, Scholar

class AddPopUp(QWidget):
    
    close_signal = Signal(bool)
    
    def __init__(self, width=400, height=350) -> None:
        super(AddPopUp, self).__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.func = UIFunctions()

        #custom properties
        self.width = width
        self.height = height
        self.resizable = False
        self.minimum_size = True
        self.shadow_blur_radius = 5
        
        # worker variables
        self.worker = None

        # signal variables
        self.process_finished = False
        self.valid_entries = False
        self.commit_complete = False
        self.log = str()

        # shadow
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(self.shadow_blur_radius)
        self.shadow.setOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 90))
        self.ui.bg.setGraphicsEffect(self.shadow)

        # window configs
        self.func.config_window(config_widget=self, title='', width=self.width, height=self.height, resizable=self.resizable, 
                                minimum_size=self.minimum_size)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.Popup)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # fonts variables
        self.label_list = [self.ui.label, self.ui.label_2, self.ui.label_3, self.ui.label_4]
        self.entry_list = [self.ui.name_value, self.ui.ronin_value, self.ui.email_value, self.ui.daily_value]
        
        # btn
        self.ui.btn_add.clicked.connect(self.confirm_btn)        
         
    def showEvent(self, event) -> None:
        for label in self.label_list:
            self.func.set_font(label, 10, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True, True)
        
        for label in self.entry_list:
            self.func.set_font(label, 10, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', False, False)
        
        self.func.set_font(self.ui.btn_add, 10, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', False, False)
        
    def closeEvent(self, event) -> None:
        self.close_signal.emit(True)
    
    def confirm_btn(self) -> None:
        self.btn_animation() 
        
        self.ui.log_label.setGeometry(QRect(187, 0, 25, 25))  
        gif_dir = os.path.abspath(os.getcwd()) + '/src/img/loading.gif'
        self.movie = QMovie(gif_dir)
        self.ui.log_label.setMovie(self.movie)
        self.movie.start()
        
        # thread config    
        arg_list = [x.text() for x in self.entry_list]  
        self.worker = ValidatorThread(*arg_list)
        self.worker.start()
        
        self.worker.log_signal.connect(self.log_receive)
        self.worker.valid_entries_signal.connect(self.valid_entries_receive)
        self.worker.commit_signal.connect(self.commit_complete_receive)
        self.worker.finished.connect(self.evt_worker_finished)        
    
    def evt_worker_finished(self) -> None:
        
        self.movie.stop()
        self.ui.log_label.clear()
        self.ui.log_label.setGeometry(QRect(0, 0, 396, 25))
        self.ui.log_label.setAlignment(Qt.AlignCenter)
  
        if not self.valid_entries: 
            self.func.set_font(self.ui.log_label, 10, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True, True)
            self.ui.log_label.setText(f'{self.log}')
        
        else:
            if self.commit_complete:
                color = '#1aff1a'
            else:
                color = '#E64C3C'
            
            self.func.set_font(self.ui.log_label, 10, ':/font/fonts/Saira-Bold.ttf', color, True, True)
            self.ui.log_label.setText(f'{self.log}')
            if self.commit_complete:
                QTimer.singleShot(1500, lambda: self.close())
            
    def btn_animation(self):
        s_rect = QPoint(158, 12)
        e_rect = QPoint(158, 28)

        self.ui.btn_add.animation = QPropertyAnimation(self.ui.btn_add, b'pos')
        self.ui.btn_add.animation.setDuration(400)
        self.ui.btn_add.animation.setEndValue(e_rect)
        self.ui.btn_add.animation.setEasingCurve(QtCore.QEasingCurve.OutBounce)
        self.ui.btn_add.animation.start()
        
    def log_receive(self, value) -> None:
        self.log = value
        
    def valid_entries_receive(self, value) -> None:
        self.valid_entries = value
        
    def commit_complete_receive(self, value) -> None:
        self.commit_complete = value
         

class ValidatorThread(QThread):
    
    log_signal = Signal(str)
    valid_entries_signal = Signal(bool)
    commit_signal = Signal(bool)
    
    def __init__(self, *args) -> None:
        super(ValidatorThread, self).__init__()
        self.empty_fields = False
        self.log = 'default'
        
    
        self.name_value =  args[0]
        self.ronin_value = args[1]
        self.email_value = args[2]
        self.daily_value = args[3]
        
        self.entry_list = [self.name_value,
                            self.ronin_value,
                            self.email_value,
                            self.daily_value]
        
    def run(self) -> bool:
        entries_filled = False
        account_valid = False
        api_is_down = False
        account_in_use = False 
        scholar_exist = False
        
        entries_filled = self.entries_filled_validator()
        
        if entries_filled:
            account_valid = self.account_validator()
            
            if account_valid:
                account_in_use = self.account_in_use_validator()
                
                if not account_in_use:
                    api_is_down = self.api_validator()
                    
                    if not api_is_down:
                        scholar_exist = self.scholar_validator()
                        
                        if scholar_exist:
                            self.log = 'Scholar already registered.'
                    else:
                         self.log = 'Api is down, try again in a fell seconds.'                    
                else:
                    self.log = 'Ronin account already in use.'
            else:
                self.log = 'Invalid ronin account.'
        else:
            self.log = 'Please, fill all required fields.'
            
        if entries_filled and account_valid and not api_is_down and not account_in_use and not scholar_exist:
            self.valid_entries = True
        else:
            self.valid_entries = False
            
        self.validator_result_handle()
            
        self.log_signal.emit(self.log)        
        
    def validator_result_handle(self):
        
        if not self.valid_entries:
            
            self.valid_entries_signal.emit(False)
            
        else:
            
            self.valid_entries_signal.emit(True)
            
            time_now = datetime.now()
            formated_datetime = time_now.strftime('%Y-%m-%d %H:%M')
            
            try:
                daily_goal = int(self.daily_value)
            except ValueError:
                self.log = 'Daily goal need to be a number.'
                self.commit_signal.emit(False)
                return
            
            acc_api = AccAxie(self.ronin_value)
            user_api = FullData(self.ronin_value)
            axie_data = acc_api.get_axie_data_str()
            daily_profit = user_api.get_daily_slp()
            last_time = formated_datetime
            daily_profit_cached = daily_profit
            actual_month_profit = daily_profit
            last_month = 0
            next_to_last_month = 0
            new_account = Account(ronin_address=self.ronin_value, data=axie_data, 
                                  scholar=[Scholar(name=self.name_value, 
                                                   email=self.email_value, 
                                                   daily_goal=daily_goal, 
                                                   last_time_checked=last_time,
                                                   daily_profit=daily_profit,
                                                   daily_profit_cached=daily_profit_cached,
                                                   actual_month_profit=actual_month_profit,
                                                   last_month_profit=last_month,
                                                   next_to_last_month_profit=next_to_last_month)]
                                  )
        
            DefaultTools.session_handle.add(new_account)
            DefaultTools.session_handle.commit()
            self.commit_signal.emit(True)
            
            self.log = 'Done.'
        
    
    def entries_filled_validator(self) -> bool:
        """ check if all entries are filled
        """
        for i in self.entry_list:
            if i == '':
                return False
            
        return True
    
    def account_validator(self) -> bool:
        """ Check if account is valid
        """
        if len(self.ronin_value) == 40:
            acc_api = AccAxie(self.ronin_value)
            axie_in_account = acc_api.get_axie_data_dict()
            
            if len(axie_in_account) > 0:
                return True
        
        return False
    
    def api_validator(self) -> bool:
        """Check if api is down
        """
        user_api = FullData(self.ronin_value)
        
        if len(user_api.data) > 0:
            for k, v in user_api.data.items():
                if k == 'messages' and v == 'The API is unreachable, please contact the API provider':
                    return True
                
        return False
        
    def account_in_use_validator(self) -> bool:
        """ Check if account is already in use
        """   
        q = Account.find_by_address(DefaultTools.session_handle, self.ronin_value)
        
        if q == None:
            return False
        
        return True
    
    def scholar_validator(self) -> bool:
        """ Check if user exists
        """
        
        q = Scholar.find_by_name(DefaultTools.session_handle, self.name_value)
        
        if q == None:
            return False
        
        return True
