from PySide6.QtWidgets import QFrame, QGridLayout, QHBoxLayout, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from .dash_widgets_analytics import CustomWidgets
from .dash_graph_analytics import GraphReports
from .dash_daily_analytics import DailyGoalWidget
import resource


class DashPage(QWidget):

    def __init__(self, colorscheme: dict):
        super(DashPage, self).__init__()
        
        self.colorscheme = colorscheme

        # config
        self.setObjectName('dash_page')

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setObjectName('main_layout')
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # main frames
        self.analytics_frame = QFrame(self)
        self.analytics_frame.setObjectName('analytics_frame')
        self.main_layout.addWidget(self.analytics_frame)

        self.analytics_config()
        
        self.graph_frame = QFrame()
        self.graph_frame.setObjectName('widgets_frame')
        self.analytics_layout.addWidget(self.graph_frame)
        
        self.graph_reports_config()

        self.daily_frame = QFrame(self)
        self.daily_frame.setObjectName('daily_frame')
        self.daily_frame.setMaximumWidth(350)
        self.daily_frame.setMinimumWidth(350)
        self.main_layout.addWidget(self.daily_frame)
        
        self.daily_frame_config()


    def analytics_config(self) -> None:
        self.analytics_layout = QVBoxLayout(self.analytics_frame)    
        self.analytics_layout.setObjectName('analytics_layout')
        self.analytics_layout.setContentsMargins(0, 0, 0, 0)
        self.analytics_layout.setSpacing(10)
        
        self.analytics_title_label = QLabel(self.analytics_frame)
        self.analytics_title_label.setObjectName('analytics_t_label')
        self.analytics_title_label.setMaximumHeight(30)
        self.analytics_title_label.setText('Analytics')
        self.analytics_layout.addWidget(self.analytics_title_label)
        
        self.widgets_frame = QFrame()
        self.widgets_frame.setObjectName('widgets_frame')
        self.widgets_frame.setMaximumHeight(250)
        self.analytics_layout.addWidget(self.widgets_frame)

        self.widgets_layout = QGridLayout(self.widgets_frame)   
        self.widgets_layout.setObjectName('widgets_layout')
        self.widgets_layout.setContentsMargins(0, 10, 0, 10)
        self.widgets_layout.setSpacing(30)

        self.scholars_widget = CustomWidgets(info='SCHOLARS', icon_path=':/img/img/user_test.svg',
                        btn_icon=':/img/img/down_arrow.svg',
                        width= 149)
        self.widgets_layout.addWidget(
            self.scholars_widget, 1, 0)

        self.m_profit_widget = CustomWidgets(info='MONTHLY PARTIAL', icon_path=':/img/img/reports_icon.svg',
                        btn_icon=':/img/img/down_arrow.svg',
                        width= 149)
        self.widgets_layout.addWidget(
            self.m_profit_widget, 1, 1)

        self.axies_widget = CustomWidgets(info='AXIES', icon_path=':/img/img/inventory.svg',
                        btn_icon=':/img/img/down_arrow.svg',
                        width= 149)
        self.widgets_layout.addWidget(
            self.axies_widget, 1, 2)

    def daily_frame_config(self):
        self.daily_layout = QVBoxLayout(self.daily_frame)
        self.daily_layout.setObjectName('daily_layout')
        self.daily_layout.setContentsMargins(10, 0, 10, 10)
        self.daily_layout.setSpacing(15)
        
        self.daily_w_title = QLabel(self.daily_frame)
        self.daily_w_title.setObjectName('daily_w_title')
        self.daily_w_title.setMaximumHeight(30)
        self.daily_w_title.setText('Reports')
        self.daily_layout.addWidget(self.daily_w_title)

        self.daily_graph_container = QFrame(self.daily_frame)
        self.daily_graph_container.setObjectName('daily_graph_container')
        self.daily_layout.addWidget(self.daily_graph_container)

        self.daily_graph_layout = QVBoxLayout(self.daily_graph_container)
        self.daily_graph_layout.setObjectName('self.daily_graph_layout')
        self.daily_graph_layout.setAlignment(Qt.AlignHCenter)
        self.daily_graph_layout.setContentsMargins(0, 0, 0, 20)
        self.daily_graph_layout.setSpacing(5)

        self.daily_title = QLabel(self.daily_frame)
        self.daily_title.setObjectName('daily_title')
        self.daily_title.setAlignment(Qt.AlignCenter)
        self.daily_title.setMaximumHeight(30)
        self.daily_title.setText('DAILY GOAL')
        self.daily_graph_layout.addWidget(self.daily_title)

        self.daily_label = QLabel(self.daily_frame)
        self.daily_label.setObjectName('daily_label')
        self.daily_label.setMaximumHeight(90)
        self.daily_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.daily_label.setText('The percentage value is based\n on the scholars goal.')
        self.daily_graph_layout.addWidget(self.daily_label)

        self.daily_widget = DailyGoalWidget(width=300, gradient_color_1=self.colorscheme['main colors']['third_color_gradient'], 
                                            gradient_color_2=self.colorscheme['main colors']['third_color'])
        self.daily_graph_layout.addWidget(self.daily_widget)

    def graph_reports_config(self):
        self.graph_layout = QVBoxLayout(self.graph_frame)
        self.graph_layout.setObjectName('graph_layout')
        self.graph_layout.setAlignment(Qt.AlignLeft)
        self.graph_layout.setContentsMargins(0, 0, 0, 0)
        self.graph_layout.setSpacing(10)
        
        self.graph_title = QLabel(self.graph_frame)
        self.graph_title.setObjectName('graph_title')
        self.graph_title.setMaximumHeight(30)
        self.graph_title.setText('Graph Reports')
        self.graph_layout.addWidget(self.graph_title)
        
        self.graph_container = QFrame(self.graph_frame)
        self.graph_container.setObjectName('graph_container')
        self.graph_layout.addWidget(self.graph_container)
        
        self.graph_container_layout = QVBoxLayout(self.graph_container)
        self.graph_container_layout.setObjectName('graph_container_layout')
        self.graph_container_layout.setContentsMargins(10, 10, 13, 10)
        self.graph_container_layout.setSpacing(10)
        
        
        self.graph = GraphReports(colorscheme=self.colorscheme)
        self.graph_container_layout.addWidget(self.graph)
