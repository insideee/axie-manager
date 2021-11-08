from PySide6.QtWidgets import QApplication, QFrame, QGridLayout, QHBoxLayout, QLabel, QVBoxLayout, QWidget
from .dash_items_analytics import CustomItem
import resource
import sys


class DashPage(QWidget):

    def __init__(self):
        super(DashPage, self).__init__()

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

        self.analytics_layout = QVBoxLayout(self.analytics_frame)    
        self.analytics_layout.setObjectName('analytics_layout')
        self.analytics_layout.setContentsMargins(0, 0, 0, 0)
        self.analytics_layout.setSpacing(0)

        self.items_frame = None
        self.items_layout = None
        self.analytics_title_label = None
        self.scholars_item = None
        self.m_profit_item = None
        self.axies_item = None
        self.graph_frame = None

        self.analytics_config()

        self.daily_frame = QFrame(self)
        self.daily_frame.setObjectName('daily_frame')
        self.daily_frame.setMaximumWidth(350)
        self.main_layout.addWidget(self.daily_frame)

    def analytics_config(self):
        self.items_frame = QFrame()
        self.items_frame.setObjectName('items_frame')
        self.items_frame.setMaximumHeight(240)
        self.analytics_layout.addWidget(self.items_frame)

        self.items_layout = QGridLayout(self.items_frame)   
        self.items_layout.setObjectName('items_layout')
        self.items_layout.setContentsMargins(0, 0, 0, 10)
        self.items_layout.setSpacing(10)

        self.analytics_title_label = QLabel(self.items_frame)
        self.analytics_title_label.setObjectName('analytics_t_label')
        self.analytics_title_label.setMaximumHeight(30)
        self.analytics_title_label.setText('Analytics')
        self.items_layout.addWidget(self.analytics_title_label, 0, 0)

        self.scholars_item = CustomItem(info='SCHOLARS', icon_path=':/img/img/teste.png',
                        btn_icon=':/img/img/down_arrow.png',
                        width= 145)
        self.items_layout.addWidget(
            self.scholars_item, 1, 0)

        self.m_profit_item = CustomItem(info='MONTHLY PROFIT', icon_path=':/img/img/reports_icon.svg',
                        btn_icon=':/img/img/down_arrow.png',
                        width= 145)
        self.items_layout.addWidget(
            self.m_profit_item, 1, 1)

        self.axies_item = CustomItem(info='AXIES', icon_path=':/img/img/inventory.svg',
                        btn_icon=':/img/img/down_arrow.png',
                        width= 145)
        self.items_layout.addWidget(
            self.axies_item, 1, 2)

        self.graph_frame = QFrame(self.analytics_frame)
        self.graph_frame.setObjectName('items_frame')
        self.analytics_layout.addWidget(self.graph_frame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DashPage()
    window.show()
    sys.exit(app.exec())
