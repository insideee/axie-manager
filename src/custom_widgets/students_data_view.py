from PySide2.QtWidgets import QWidget
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
        self.height_default = 587
        self.data_entry_info = []
        self.data_entry_widgets = []
        
        # font config
        self.font_configuration()
        
        self.data_entry_creator()
        
        for widget in self.data_entry_widgets:
            print(self.ui.roninLabel.width())
            print(widget.styleSheet() + ' 1', \
                '\n\n', widget.ui.data.styleSheet())
        
        self.show()
        
    def event(self, event: QtCore.QEvent) -> bool:
        
        if event.type() == QtCore.QEvent.Type.Resize:
            
            if self.width() == self.width_default:
                # mudar a quantidade que pode ser mostrada e dar reload
                pass
            elif self.width() > self.width_default:
                # mudar novamente e reaload
                pass
        return super().event(event)
    
    def font_configuration(self):
        
        #header widgets
        h_labels = [self.ui.nameLabel, self.ui.emailLabel, self.ui.roninLabel, self.ui.slpGoalLabel, self.ui.slpTodayLabel]
        
        font_config = [self.func.set_font(label, 11, ':/font/fonts/Saira-Bold.ttf', '#E64C3C', True, True) for label in h_labels]
     
    def shadow_configuration(self):
        self.func.set_drop_shadow(self)
        
    def data_entry_creator(self):
        
        self.get_data_info()
        
        for data_info in self.data_entry_info:
            self.data_entry_widget_creator(data_info)
            
        for widget in self.data_entry_widgets:
            self.ui.verticalLayout_3.addWidget(widget)
    
    def get_data_info(self):
        
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
        
        
        self.show()
        
    def font_configuration(self):
        data_labels = [self.ui.nameData, self.ui.emailData, self.ui.roninData, self.ui.slpGoalData, self.ui.slpTodayData]
        
        font_config = [self.func.set_font(label, 10, ':/font/fonts/Saira-Bold.ttf', '#F9F9F9', True, True) for label in data_labels]
        
        