from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QHBoxLayout, QToolButton, QVBoxLayout, QWidget
from .data_widget import DataWidget
from functions import Functions
import resource

# primeiro saber o total de widgets para saber o 
# tamanho da janela
# se for menos que o minimo dar resize na janela para sempre cada um ter 50 px
# evitar bug da animação

# need to be 920, 540

class ScholarPage(QFrame):
    
    def __init__(self) -> None:
        super(ScholarPage, self).__init__()
        
        # configs
        self.setObjectName('scholar_page')
        self.setMinimumSize(QSize(920, 520))
        self.reset_style = """background-color: none;
                                border: none;
                                border-radius: 0px;
                            """
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setObjectName('main_layout')
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        self.header_data_frame = QFrame(self)
        self.header_data_frame.setObjectName('header_data_frame')
        self.header_data_frame.setMinimumSize(QSize(920, 90))
        self.header_data_frame.setMaximumSize(QSize(920, 90))
        self.header_data_frame.setStyleSheet(self.reset_style)
        self.main_layout.addWidget(self.header_data_frame)   
        
        self.filter_btn_icon = Functions.paint_image(':img/img/filter.svg', 
                                                       color=QColor('#8B83BA'), 
                                                       size=QSize(17, 17) )
        
        self.header_data_config()
        
        self.data_view_frame = QFrame(self)
        self.data_view_frame.setObjectName('data_view_frame')
        self.data_view_frame.setMinimumSize(QSize(920, 400))
        self.data_view_frame.setMaximumSize(QSize(920, 400))
        self.data_view_frame.setStyleSheet(self.reset_style)
        self.main_layout.addWidget(self.data_view_frame)
        
        self.data_view_config()
        
        self.bottom_data_frame = QFrame(self)
        self.bottom_data_frame.setObjectName('bottom_data_frame')
        self.bottom_data_frame.setMinimumSize(QSize(920, 40))
        self.bottom_data_frame.setMaximumSize(QSize(920, 40))
        self.bottom_data_frame.setStyleSheet(self.reset_style)
        self.main_layout.addWidget(self.bottom_data_frame)
        
    def header_data_config(self):
        # main layout
        self.header_data_layout = QVBoxLayout(self.header_data_frame)
        self.header_data_layout.setObjectName('header_data_layout')
        self.header_data_layout.setContentsMargins(0, 0, 0, 0)
        self.header_data_layout.setSpacing(0)
        
        # btns container
        self.header_btn_frame = QFrame(self.header_data_frame)
        self.header_btn_frame.setObjectName('header_btn_frame')
        self.header_data_layout.addWidget(self.header_btn_frame)
        
        self.header_btn_layout = QHBoxLayout(self.header_btn_frame)
        self.header_btn_layout.setObjectName('header_btn_layout')
        self.header_btn_layout.setContentsMargins(0, 0, 0, 0)
        self.header_btn_layout.setSpacing(0)
        
        # filter btn container
        self.header_btn_filter_frame = QFrame(self.header_btn_frame)
        self.header_btn_filter_frame.setObjectName('header_btn_filter_frame')
        self.header_btn_layout.addWidget(self.header_btn_filter_frame)
        
        self.header_btn_filter_layout = QVBoxLayout(self.header_btn_filter_frame)
        self.header_btn_filter_layout.setObjectName('header_btn_filter_layout')
        self.header_btn_filter_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.header_btn_filter_layout.setContentsMargins(10, 0, 0, 0)
        self.header_btn_filter_layout.setSpacing(0)
        
        # manage btn container
        self.header_btn_manage_frame = QFrame(self.header_btn_frame)
        self.header_btn_manage_frame.setObjectName('header_btn_manage_frame')
        self.header_btn_layout.addWidget(self.header_btn_manage_frame)
        
        self.header_btn_manage_layout = QVBoxLayout(self.header_btn_manage_frame)
        self.header_btn_manage_layout.setObjectName('header_btn_manage_layout')
        self.header_btn_manage_layout.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.header_btn_manage_layout.setContentsMargins(0, 0, 10, 0)
        self.header_btn_manage_layout.setSpacing(0)
        
        self.header_btns_config()
        
        # table header container
        self.header_title_frame = QFrame(self.header_data_frame)
        self.header_title_frame.setObjectName('header_title_frame')
        self.header_title_frame.setMinimumHeight(50)
        self.header_data_layout.addWidget(self.header_title_frame)
    
    def header_btns_config(self):
        # filter
        self.filter_btn = QToolButton(self.header_data_frame)    
        self.filter_btn.setObjectName('filter_btn')
        self.filter_btn.setMinimumSize(70, 30)
        self.filter_btn.setMaximumSize(70, 30)
        self.filter_btn.setCursor(Qt.PointingHandCursor)
        self.filter_btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.filter_btn.setIcon(self.filter_btn_icon)
        self.filter_btn.setIconSize(QSize(17, 17))
        self.filter_btn.setText('Filter')
        self.header_btn_filter_layout.addWidget(self.filter_btn)
        
        # add
        self.add_btn = QToolButton(self.header_data_frame)    
        self.add_btn.setObjectName('add_btn')
        self.add_btn.setMinimumSize(70, 30)
        self.add_btn.setMaximumSize(70, 30)
        self.add_btn.setCursor(Qt.PointingHandCursor)
        self.add_btn.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.add_btn.setText('ADD')
        self.header_btn_manage_layout.addWidget(self.add_btn)
        
    def data_view_config(self):
        self.data_view_layout = QVBoxLayout(self.data_view_frame)
        self.data_view_layout.setObjectName('data_view_layout')
        self.data_view_layout.setContentsMargins(0, 0, 0, 0)
        self.data_view_layout.setSpacing(0)
        
        self.widget_list = []
        
        for i in range(0, 8):
            self.widget_list.append(DataWidget(obj_name=f'{i}'))
            self.data_view_layout.addWidget(self.widget_list[i])  


        