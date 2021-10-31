from PySide6 import QtWidgets, QtCore
import PySide6
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QApplication
from PySide6.QtCore import QMargins, QPoint, QRect, QSize, Qt
import sys


class InventoryPage(QWidget):
    
    def __init__(self) -> None:
        super(InventoryPage, self).__init__()
        
        # temp
        self.setMinimumSize(QSize(1131, 587))
        self.setStyleSheet('QWidget{background-color:  #303840;'
                           'border: 2px solid #FFFF00}')
        self.setGeometry(QtWidgets.QStyle.alignedRect(
                Qt.LeftToRight,
                Qt.AlignCenter,
                self.size(),
                QGuiApplication.primaryScreen().availableGeometry(),
            ),)
        self.setObjectName('InventoryContainer')
        
        self.default_size = QSize(1131, 587)
        
        self.h_layout_main = QHBoxLayout(self)        
        self.h_layout_main.setContentsMargins(0, 0, 0, 0)
        self.h_layout_main.setSpacing(0)
        
        self.items_frame = QWidget()
        self.items_frame.setObjectName('ItemsFrame')
        self.h_layout_main.addWidget(self.items_frame)
        self.h_layout_items = QHBoxLayout(self.items_frame)
        self.h_layout_items.setContentsMargins(QMargins(20, 60, 20, 60))
        
        self.info_frame = QWidget()
        self.info_frame.setObjectName('InfoFrame')
        self.info_frame.setMaximumWidth(310)
        self.h_layout_main.addWidget(self.info_frame)
        self.v_layout_info = QVBoxLayout(self.info_frame)
        self.v_layout_info.setContentsMargins(QMargins(20, 60, 20, 60))
        self.v_layout_info.setAlignment(Qt.AlignTop)
        
        self.items_container = QWidget()
        self.items_container.setStyleSheet('QWidget{background-color: #47525E;'
                                           'border: 0px;'
                                           'border-top-left-radius: 10px;'
                                           'border-bottom-right-radius: 10px}')
        self.h_layout_items.addWidget(self.items_container)
        
        self.info_container = QWidget()
        self.info_container.setMinimumSize(QSize(270, 467))
        self.info_container.setMaximumSize(QSize(270, 607))
        self.info_container.setStyleSheet('QWidget{background-color: #47525E;'
                                           'border: 0px;'
                                           'border-top-left-radius: 10px;'
                                           'border-bottom-right-radius: 10px}')        
        self.v_layout_info.addWidget(self.info_container)
        
        
        # config
        self.installEventFilter(self)
        
    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        
        if watched == self and event.type() == QtCore.QEvent.Type.Resize:
            
            if self.size().height() > 1000:
                item_margin = QMargins(20, 120, 20, 120)
                info_margin = QMargins(20, 120, 20, 60)
            else:
                item_margin = QMargins(20, 60, 20, 60)
                info_margin = QMargins(20, 60, 20, 60)
                
            self.h_layout_items.setContentsMargins(item_margin)
            self.v_layout_info.setContentsMargins(info_margin)
        
        return super().eventFilter(watched, event)
        
        
        
if __name__ == '__main__':
    a = QApplication(sys.argv)
    b = InventoryPage()
    b.show()
    sys.exit(a.exec_())