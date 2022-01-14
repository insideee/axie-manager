from PySide6.QtCore import QPoint, QSize, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QCheckBox, QFrame, QHBoxLayout, QLabel, QToolButton, QVBoxLayout
from .data_widget import DataWidget
from .view_more_popup import MoreMenuPopup
from .view_more_btn import MoreMenuBtn
from .add_scholar_popup import AddPopup
import tools
import resource

# primeiro saber o total de widgets para saber o 
# tamanho da janela
# se for menos que o minimo dar resize na janela para sempre cada um ter 50 px
# evitar bug da animação
#
# para o max resize, criar uma tools para posicionar e no caso do resize
# reload no posicionar
#
# need to be 920, 540

class ScholarPage(QFrame):
    
    def __init__(self, colorscheme: str) -> None:
        super(ScholarPage, self).__init__()
        
        # configs
        self.setObjectName('scholar_page')
        self.setMinimumSize(QSize(920, 520))
        
        # properties             
        self.reset_style = """background-color: none;
                                border: none;
                                border-radius: 0px;
                            """
        self.colorscheme = colorscheme
        self.main_color = self.colorscheme['table_view']['main_color']
        self.hover_color = self.colorscheme['table_view']['hover_color']
        self.popup_hover_color = self.colorscheme['table_view']['popup_hover_color']
        self.widget_color = self.colorscheme['main colors']['widget_bg']
        self.popup = None
        self.view_more_menu_icon = tools.paint_image(image=':/img/img/more_menu.svg',
                                                    color=QColor(self.main_color),
                                                    size=QSize(25, 25))
        self.view_more_menu_icon_painted = tools.paint_image(image=':/img/img/more_menu.svg',
                                                            color=QColor(
                                                        self.hover_color),
                                                            size=QSize(25, 25))
        self.view_more_menu_exit_icon = tools.paint_image(image=':/img/img/exit_popup.svg',
                                                         color=QColor(
                                                        self.main_color),
                                                         size=QSize(18, 18))
        self.filter_btn_icon = tools.paint_image(':img/img/filter.svg', 
                                                       color=QColor(self.main_color), 
                                                       size=QSize(17, 17) )       
        
        # bottom container variables
        self.first_item_showing = 1 
        self.last_item_showing = 8
        self.total_items = 8
        self.left_icon = tools.paint_image(':img/img/left.svg', 
                                                       color=QColor(self.main_color), 
                                                       size=QSize(7, 12) )  
        self.right_icon = tools.paint_image(':img/img/right.svg', 
                                                       color=QColor(self.main_color), 
                                                       size=QSize(7, 12) )  
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setObjectName('main_layout')
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        self.header_data_frame = QFrame(self)
        self.header_data_frame.setObjectName('header_data_frame')
        self.header_data_frame.setMinimumSize(QSize(920, 90))
        self.header_data_frame.setStyleSheet(self.reset_style)
        self.main_layout.addWidget(self.header_data_frame)   
        
        
        self.data_view_frame = QFrame(self)
        self.data_view_frame.setObjectName('data_view_frame')
        self.data_view_frame.setMinimumSize(QSize(920, 400))
        self.data_view_frame.setStyleSheet(self.reset_style)
        self.main_layout.addWidget(self.data_view_frame)
        
        
        self.bottom_data_frame = QFrame(self)
        self.bottom_data_frame.setObjectName('bottom_data_frame')
        self.bottom_data_frame.setMinimumSize(QSize(920, 30))
        self.bottom_data_frame.setMaximumSize(QSize(920, 30))
        self.bottom_data_frame.setStyleSheet(self.reset_style)
        self.main_layout.addWidget(self.bottom_data_frame)
        
        self.header_data_config()
        self.data_view_config()
        self.bottom_config()
        
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
        
        self.table_header_config()
    
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
        self.add_btn.clicked.connect(self.add_scholar)
        self.header_btn_manage_layout.addWidget(self.add_btn)
        
    def table_header_config(self):
        self.header_title_layout = QHBoxLayout(self.header_title_frame)
        self.header_title_layout.setObjectName('header_title_layout')
        self.header_title_layout.setContentsMargins(0, 0, 0, 0)
        self.header_title_layout.setSpacing(0)
        
        # check
        self.select_frame = QFrame(self.header_title_frame)
        self.select_frame.setObjectName('select_frame')
        self.select_frame.setMinimumWidth(100)
        self.select_frame.setMaximumWidth(100)
        self.select_frame.setStyleSheet(self.reset_style)
        self.header_title_layout.addWidget(self.select_frame)
        
        self.check_box_select = QCheckBox(self.select_frame)
        self.check_box_select.setCursor(Qt.PointingHandCursor)
        self.check_box_select.setStyleSheet(f"""QCheckBox{{ background-color: none;
                                                    border: none;
                                                    border-radius: 5px;
                                        }}
                                        QCheckBox::indicator{{
                                                        background-color: none;
                                                        border: 2px solid {self.main_color};
                                                        width: 18;
                                                        height: 18;
                                                        border-radius: 4px;}}
                                        QCheckBox::indicator::checked{{
                                                            background-color: {self.main_color};
                                                            image: url(:/img/img/checked.svg)}}""")
        self.check_box_select.move(QPoint(0.24 * self.select_frame.width(), 0.4 * self.select_frame.height()))
        
        # titles
        self.titles_frame = QFrame(self.header_title_frame)
        self.titles_frame.setObjectName('titles_frame')
        self.titles_frame.setMinimumWidth(720)
        self.titles_frame.setStyleSheet(self.reset_style)
        self.header_title_layout.addWidget(self.titles_frame)
        
        size = QSize(144, 50)
        
        self.name_title_label = QLabel(self.titles_frame)
        self.name_title_label.setObjectName('name_title_label')
        self.name_title_label.setAlignment(Qt.AlignCenter)
        self.name_title_label.setMinimumSize(size)
        self.name_title_label.setMaximumSize(size)
        self.name_title_label.setText('name')
        self.name_title_label.move(0, 0)
        
        self.today_title_label = QLabel(self.titles_frame)
        self.today_title_label.setObjectName('today_title_label')
        self.today_title_label.setAlignment(Qt.AlignCenter)
        self.today_title_label.setMinimumSize(size)
        self.today_title_label.setMaximumSize(size)
        self.today_title_label.setText('today')
        self.today_title_label.move(0.2*self.titles_frame.width(), 0)
        
        self.yesterday_title_label = QLabel(self.titles_frame)
        self.yesterday_title_label.setObjectName('yesterday_title_label')
        self.yesterday_title_label.setAlignment(Qt.AlignCenter)
        self.yesterday_title_label.setMinimumSize(size)
        self.yesterday_title_label.setMaximumSize(size)
        self.yesterday_title_label.setText('yesterday')
        self.yesterday_title_label.move(0.4*self.titles_frame.width(), 0)
        
        self.total_title_label = QLabel(self.titles_frame)
        self.total_title_label.setObjectName('total_title_label')
        self.total_title_label.setAlignment(Qt.AlignCenter)
        self.total_title_label.setMinimumSize(size)
        self.total_title_label.setMaximumSize(size)
        self.total_title_label.setText('total')
        self.total_title_label.move(0.6*self.titles_frame.width(), 0)
        
        self.next_claim_title_label = QLabel(self.titles_frame)
        self.next_claim_title_label.setObjectName('next_claim_title_label')
        self.next_claim_title_label.setAlignment(Qt.AlignCenter)
        self.next_claim_title_label.setMinimumSize(size)
        self.next_claim_title_label.setMaximumSize(size)
        self.next_claim_title_label.setText('next claim')
        self.next_claim_title_label.move(0.8*self.titles_frame.width(), 0)
        
        # menu
        self.view_more_frame = QFrame(self.header_title_frame)
        self.view_more_frame.setObjectName('view_more_frame')
        self.view_more_frame.setMinimumWidth(100)
        self.view_more_frame.setMaximumWidth(100)
        self.view_more_frame.setStyleSheet(self.reset_style)
        self.header_title_layout.addWidget(self.view_more_frame)
        
        self.view_more_menu_btn = MoreMenuBtn(parent=self.view_more_frame,
                                                default_image=self.view_more_menu_icon,
                                                painted_image=self.view_more_menu_icon_painted)
        self.view_more_menu_btn.move(0.72*self.view_more_frame.width(),0.4*self.view_more_frame.height())
        
        self.view_more_menu_btn.clicked.connect(self.view_more_pressed)
        
    def view_more_pressed(self):
        global_pos = self.view_more_frame.mapToGlobal(QPoint(0, 0))
        move_to = global_pos - QPoint(15, 10)

        if self.popup == None:
            self.popup = MoreMenuPopup(pos_spawn=move_to,
                                       main_color=self.main_color,
                                       hover_color=self.popup_hover_color,
                                       widget_color=self.widget_color)
            for frame in [self.popup.bg_container, self.popup.exit_btn]:
                tools.set_drop_shadow(frame, blur=10, opacity=40)
            
            tools.set_font(target=self.popup.delete_btn,
                            size=9, font_name=':/fonts/fonts/Montserrat-Medium.ttf',
                            bold=False, index=1)
            
        else:
            self.popup.move(move_to)

        self.popup.show()
    
    def data_view_config(self):
        self.data_view_layout = QVBoxLayout(self.data_view_frame)
        self.data_view_layout.setObjectName('data_view_layout')
        self.data_view_layout.setContentsMargins(0, 0, 0, 0)
        self.data_view_layout.setSpacing(0)
        
        self.widget_list = []
        
        for i in range(0, 8):
            self.widget_list.append(DataWidget(obj_name=f'{i}', colorscheme=self.colorscheme))
            self.data_view_layout.addWidget(self.widget_list[i])  

    def bottom_config(self):
        self.bottom_data_layout = QHBoxLayout(self.bottom_data_frame)
        self.bottom_data_layout.setObjectName('bottom_data_layout')
        self.bottom_data_layout.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.bottom_data_layout.setContentsMargins(0, 0, 10, 0)
        self.bottom_data_layout.setSpacing(10)
        
        self.bottom_info_label = QLabel(self.bottom_data_frame)
        self.bottom_info_label.setObjectName('bottom_info_label')
        self.bottom_info_label.setAlignment(Qt.AlignCenter)
        self.bottom_info_label.setText(f'{self.first_item_showing}-{self.last_item_showing} of {self.total_items}')
        self.bottom_data_layout.addWidget(self.bottom_info_label)
        
        self.go_left_btn = QToolButton(self.bottom_data_frame)
        self.go_left_btn.setObjectName('go_left_btn')
        self.go_left_btn.setMinimumSize(30, 30)
        self.go_left_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.go_left_btn.setIcon(self.left_icon)
        self.go_left_btn.setIconSize(QSize(7, 12))
        self.go_left_btn.setCursor(Qt.PointingHandCursor)
        self.bottom_data_layout.addWidget(self.go_left_btn)
        
        self.go_right_btn = QToolButton(self.bottom_data_frame)
        self.go_right_btn.setObjectName('go_right_btn')
        self.go_right_btn.setMinimumSize(30, 30)
        self.go_right_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.go_right_btn.setIcon(self.right_icon)
        self.go_right_btn.setIconSize(QSize(7, 12))
        self.go_right_btn.setCursor(Qt.PointingHandCursor)
        self.bottom_data_layout.addWidget(self.go_right_btn)
        
    def add_scholar(self):
        global_pos = self.data_view_frame.mapToGlobal(QPoint(0, 0))
        move_to = global_pos + QPoint((self.data_view_frame.width() / 2) - 175, 0)
        self.add_popup = AddPopup(parent=self, pos_spawn=move_to, colorscheme=self.colorscheme)
        
        #shadow
        tools.set_drop_shadow(self.add_popup, blur=10, opacity=60)
        
        self.add_popup.show()
