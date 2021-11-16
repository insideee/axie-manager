from PySide6.QtCore import QRect, QSize, Qt
from PySide6.QtWidgets import QFrame, QToolButton, QVBoxLayout
from functions import Functions as func


class MoreMenuPopup(QFrame):
    """Custom popup for the more menu button.
    """

    def __init__(self, pos_spawn, main_color: str, hover_color: str, widget_color: str):
        super(MoreMenuPopup, self).__init__()

        # properties
        self.exit_icon = func.paint_image(image=':/img/img/exit_popup.svg', color=main_color,
                                          size=QSize(18, 18))
        self.delete_icon = func.paint_image(image=':/img/img/Delete.svg', color='#D30000',
                                          size=QSize(12, 12))

        # config
        self.setGeometry(QRect(pos_spawn, QSize(120, 65)))
        self.setMinimumSize(QSize(120, 65))
        self.setMaximumSize(QSize(120, 65))

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setObjectName('main_layout')
        self.main_layout.setContentsMargins(5, 15, 15, 5)
        self.main_layout.setSpacing(0)

        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.WindowStaysOnTopHint | Qt.NoDropShadowWindowHint | Qt.Popup)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.bg_container = QFrame(self)
        self.bg_container.setObjectName('bg_container')
        self.bg_container.setStyleSheet(f"""background-color: {widget_color};
                        border: none;
                        border-radius: 10px""")
        self.main_layout.addWidget(self.bg_container)

        self.bg_layout = QVBoxLayout(self.bg_container)
        self.bg_layout.setObjectName('bg_layout')
        self.bg_layout.setContentsMargins(5, 5, 5, 5)
        self.bg_layout.setSpacing(5)
        self.bg_layout.setAlignment(Qt.AlignTop)

        self.exit_btn = QToolButton(self)
        self.exit_btn.setGeometry(90, 0, 20, 20)
        self.exit_btn.setStyleSheet(f"""background-color: {widget_color};
                                        border: none;
                                        border-radius: 10px
                                    """)
        self.exit_btn.setIcon(self.exit_icon)
        self.exit_btn.setIconSize(QSize(18, 18))
        self.exit_btn.setCursor(Qt.PointingHandCursor)
        self.exit_btn.setMouseTracking(True)

        self.exit_btn.clicked.connect(self.exit_btn_clicked_handle)

        self.delete_btn = QToolButton(self.bg_container)
        self.delete_btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.delete_btn.setObjectName('delete_btn')
        self.delete_btn.setIcon(self.delete_icon)
        self.delete_btn.setMinimumSize(QSize(90, 35))
        self.delete_btn.setIconSize(QSize(12, 12))
        self.delete_btn.setCursor(Qt.PointingHandCursor)
        self.delete_btn.setText('Delete')
        self.delete_btn.setStyleSheet(f"""QToolButton{{background-color: none;
                                            border: none;
                                            border-radius: 10px;
                                            padding-left: 15px;
                                            color: #D30000
                                        }}
                                        QToolButton::hover{{ 
                                            background-color: {hover_color}
                                        }}
                                    """)
        self.delete_btn.clicked.connect(self.delete_btn_clicked_handle)
        self.bg_layout.addWidget(self.delete_btn)

    def exit_btn_clicked_handle(self):
        self.close()

    def delete_btn_clicked_handle(self):
        pass
