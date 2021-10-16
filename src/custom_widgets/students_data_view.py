from PySide2.QtWidgets import QDesktopWidget, QWidget
from PySide2 import QtCore, QtGui


try:
    from custom_widgets.ui import Ui_dataViewWidget, Ui_dataEntryCreator
    from functions import UIFunctions
    from model import Scholar, Account, DefaultTools

except ModuleNotFoundError:
    from src.custom_widgets.ui import Ui_dataViewWidget, Ui_dataEntryCreator
    from src.functions import UIFunctions
    from src.model import Scholar, Account, DefaultTools
    
class StudentsDataView(QWidget):
    
    def __init__(self,) -> None:
        super(StudentsDataView, self).__init__()
        self.ui = Ui_dataViewWidget()
        self.ui.setupUi(self)
        self.func = UIFunctions()
        
        # properties
        self.width_default = 1131
        self.height_default = 540
        self.data_entry_info = []
        self.data_entry_widgets = []
        
        #variables 
        self.actual_percent_screen = None
        
        # font config
        self.font_configuration()
        
        self.data_entry_creator()
        
        
        self.show()
        
        # pages variables
        self.current_page = 1
        self.goto_page = 0
        self.receivers_count = 0
        self.show_widgets_each_page(1)
        
    def get_height(self) -> int:
        
        try:
            app_height = self.get_app_height()
        except AttributeError:
            app_height = 540
        
        default_percent = (self.height_default/680)
        
        height = default_percent * app_height
        
        return(int(height))
    
    def get_app_height(self) -> int:
        parent = self
        
        for i in range(0, 101):
            parent = parent.parent()
            
            try:
                name = parent.objectName()
            except AttributeError:
                break
            
            if parent.objectName() == 'MainWindow':
                break
            
        try:
            app_height = parent.height()
        except AttributeError:
            app_height = 680
        
        return app_height
    
    def get_number_pages(self, max_widgets) -> int:
        
        pages = len(self.data_entry_widgets) / max_widgets
        
        if type(pages) == float:
            dif = abs(pages - int(pages))
            
            if 0 < dif < 1: 
                pages += 1
                
        if int(pages) > 1:
            
            was_blocked = self.ui.rigthBtn.signalsBlocked()
            
            self.ui.rigthBtn.blockSignals(was_blocked)
            
            if self.receivers_count == 0:
                self.ui.leftBtn.clicked.connect(self.previus_page)
                self.ui.rigthBtn.clicked.connect(self.next_page)
                self.receivers_count += 1
                   
        return int(pages)
    
    def next_page(self):
        print('go_next')
        
        height = self.get_height()
        max_widgets = self.get_max_widgets(height)
        number_pages = self.get_number_pages(max_widgets)
        
        
        
        if self.current_page < number_pages:
            self.goto_page = self.current_page + 1
            self.show_widgets_each_page(self.goto_page)
        
    def previus_page(self):
        print('go_back')
        
        height = self.get_height()
        max_widgets = self.get_max_widgets(height)
        number_pages = self.get_number_pages(max_widgets)

        if self.current_page > 1:
            self.goto_page = self.current_page - 1
            self.show_widgets_each_page(self.goto_page)
        
    def event(self, event: QtCore.QEvent) -> bool:
        
        if event.type() == QtCore.QEvent.Type.Resize:
            try:
                app_height = self.get_app_height()
            except AttributeError:
                app_height = 680
                
            app_default_height = 680
        
            if app_height == app_default_height:
                self.set_max_height(default=True)
            elif app_height > app_default_height:
                self.set_max_height(default=False)
            
                
        return super().event(event)
    
    def set_max_height(self, default) -> int:
        
        if default:
            height=self.height_default
        else:
            height = self.get_height()
            
        self.setMaximumHeight(height)
    
    def show_widgets_each_page(self, goto_page):
        
        height = self.get_height()
        max_widgets = self.get_max_widgets(height)
        number_pages = self.get_number_pages(max_widgets)
        total_widget = len(self.data_entry_widgets)
        
        print(f'height: {height}, max:{max_widgets}, number_pages: {number_pages}, total_widgets: {total_widget}')
        
        if number_pages != 1:
            start_index = []
            
            for i in range(0, number_pages):
                start_index.append(max_widgets * i)
                
            if goto_page == number_pages:
                end_index = total_widget
            else:
                end_index = start_index[goto_page]
            
            #close all
            start_place = QtCore.QPoint(0, 0)
            end_place = QtCore.QPoint(3000, 0)
            duration = 450
            
            for widget in self.data_entry_widgets:
                pass
                if widget.isVisible():
                    self.ui.verticalLayout_3.addWidget(widget)
                    self.fade_in(start_place, end_place, duration, widget)
                    start_place.setY(start_place.y()+30)
                    end_place.setY(end_place.y()+30)
                    #duration += 20
                
            
            start_place = QtCore.QPoint(-1000, 0)
            end_place = QtCore.QPoint(0, 0)
            duration = 250
            
            for widget in self.data_entry_widgets[start_index[goto_page-1]:end_index]:
                
                self.ui.verticalLayout_3.addWidget(widget)
                self.fade_in(start_place, end_place, duration, widget)
                start_place.setY(start_place.y()+30)
                end_place.setY(end_place.y()+30)
                #duration += 20
        else:
            
            for widget in self.data_entry_widgets:
                self.ui.verticalLayout_3.addWidget(widget)
                
        self.ui.indiceLabel.setText(f'{goto_page}')
        self.current_page = goto_page
     
    def fade_in(self, start_point, end_point,  duration, widget,):
        if not widget.isVisible():
            widget.show()       
        
        widget.animation = QtCore.QPropertyAnimation(widget, b'pos')
        widget.animation.setDuration(duration)
        widget.animation.setStartValue(start_point)
        widget.animation.setEndValue(end_point)
        widget.animation.setEasingCurve(QtCore.QEasingCurve.InQuad)
        widget.animation.start(QtCore.QAbstractAnimation.DeleteWhenStopped)
        
    def get_max_widgets(self, height) -> int:
        
        max_widgets = (height/30) - 2
        
        return int(max_widgets)
    
    def font_configuration(self):
        
        #header widgets
        h_labels = [self.ui.nameLabel, self.ui.emailLabel, self.ui.roninLabel, self.ui.slpGoalLabel, self.ui.slpTodayLabel]
        
        font_config = [self.func.set_font(label, 11, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True, True) for label in h_labels]
        
        self.func.set_font(self.ui.indiceLabel, 9, ':/font/fonts/Saira-Bold.ttf', '#7A8289', True, True)
     
    def shadow_configuration(self):
        self.func.set_drop_shadow(self)
        
    def data_entry_creator(self):
        
        # get data
        self.get_data_info()
        
        # make widget with the data
        for data_info in self.data_entry_info:
            self.data_entry_widget_creator(data_info)
    
    def get_data_info(self):\
        
        for i in range(0, 40):
            self.data_entry_info.append({'name': 'asd',
                                            'ronin': 'asd',
                                            'email': 'asd',
                                            'daily_goal': 'asd',
                                            'today_profit': 'asd'})
        
        
        return
        
        students_list = Scholar.get_all_scholars(DefaultTools.session_handle)
        
        for student in students_list:
            
            self.data_entry_info.append({'name': student.name,
                                        'ronin': student.account.ronin_address,
                                        'email': student.email,
                                        'daily_goal': str(student.daily_goal),
                                        'today_profit': str(student.daily_profit)})
    
    def data_entry_widget_creator(self, dict_info):
        widget = dataEntryCreator(dict_info=dict_info)
        
        self.data_entry_widgets.append(widget)
        
class dataEntryCreator(QWidget):
    
    def __init__(self, dict_info: dict) -> None:
        super(dataEntryCreator, self).__init__()
        self.ui = Ui_dataEntryCreator()
        self.ui.setupUi(self)
        self.func = UIFunctions()
        
        # set info
        self.ui.nameData.setText(dict_info['name'])
        self.ui.roninData.setText(dict_info['ronin'])
        self.ui.emailData.setText(dict_info['email'])
        self.ui.slpGoalData.setText(dict_info['daily_goal'])
        self.ui.slpTodayData.setText(dict_info['today_profit'])
        
        # font config
        self.font_configuration()
        
    def font_configuration(self):
        data_labels = [self.ui.nameData, self.ui.emailData, self.ui.roninData, self.ui.slpGoalData, self.ui.slpTodayData]
        
        font_config = [self.func.set_font(label, 10, ':/font/fonts/Saira-Bold.ttf', '#F9F9F9', True, True) for label in data_labels]
        
        