# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_add_pop_upfdnnPp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(400, 300)
        self.verticalLayout = QVBoxLayout(main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.bg = QWidget(main)
        self.bg.setObjectName(u"bg")
        self.bg.setMinimumSize(QSize(0, 0))
        self.bg.setStyleSheet(u"QWidget{background-color:  #303840;\n"
"border-radius: 10px;}")
        self.verticalLayout_2 = QVBoxLayout(self.bg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.entrys = QWidget(self.bg)
        self.entrys.setObjectName(u"entrys")
        self.verticalLayout_3 = QVBoxLayout(self.entrys)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.entry_nome = QWidget(self.entrys)
        self.entry_nome.setObjectName(u"entry_nome")
        self.verticalLayout_5 = QVBoxLayout(self.entry_nome)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.entry_nome)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.entry_line = QLineEdit(self.entry_nome)
        self.entry_line.setObjectName(u"entry_line")
        self.entry_line.setMinimumSize(QSize(0, 20))
        self.entry_line.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid #737373;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.entry_line)


        self.verticalLayout_3.addWidget(self.entry_nome)

        self.entry_ronin = QWidget(self.entrys)
        self.entry_ronin.setObjectName(u"entry_ronin")
        self.verticalLayout_6 = QVBoxLayout(self.entry_ronin)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.entry_ronin)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.entry_line_2 = QLineEdit(self.entry_ronin)
        self.entry_line_2.setObjectName(u"entry_line_2")
        self.entry_line_2.setMinimumSize(QSize(0, 20))
        self.entry_line_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid #737373;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_6.addWidget(self.entry_line_2)


        self.verticalLayout_3.addWidget(self.entry_ronin)

        self.entry_email = QWidget(self.entrys)
        self.entry_email.setObjectName(u"entry_email")
        self.verticalLayout_7 = QVBoxLayout(self.entry_email)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.entry_email)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.entry_line_3 = QLineEdit(self.entry_email)
        self.entry_line_3.setObjectName(u"entry_line_3")
        self.entry_line_3.setMinimumSize(QSize(0, 20))
        self.entry_line_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid #737373;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_7.addWidget(self.entry_line_3)


        self.verticalLayout_3.addWidget(self.entry_email)

        self.entry_daily = QWidget(self.entrys)
        self.entry_daily.setObjectName(u"entry_daily")
        self.verticalLayout_8 = QVBoxLayout(self.entry_daily)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.entry_daily)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 20))

        self.verticalLayout_8.addWidget(self.label_4)

        self.entry_line_4 = QLineEdit(self.entry_daily)
        self.entry_line_4.setObjectName(u"entry_line_4")
        self.entry_line_4.setMinimumSize(QSize(0, 20))
        self.entry_line_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid #737373;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.entry_line_4)


        self.verticalLayout_3.addWidget(self.entry_daily)


        self.verticalLayout_2.addWidget(self.entrys)

        self.button = QWidget(self.bg)
        self.button.setObjectName(u"button")
        self.button.setMinimumSize(QSize(0, 50))
        self.button.setMaximumSize(QSize(16777215, 50))
        self.verticalLayout_4 = QVBoxLayout(self.button)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.add = QPushButton(self.button)
        self.add.setObjectName(u"add")
        self.add.setMinimumSize(QSize(80, 25))
        self.add.setMaximumSize(QSize(16777215, 16777215))
        self.add.setStyleSheet(u"QPushButton{background-color: #737373;\n"
"border-radius: 5px}")

        self.verticalLayout_4.addWidget(self.add, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.button)


        self.verticalLayout.addWidget(self.bg)


        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"Form", None))
        self.label.setText(QCoreApplication.translate("main", u"Name:", None))
        self.entry_line.setInputMask("")
        self.label_2.setText(QCoreApplication.translate("main", u"Ronin Address:", None))
        self.entry_line_2.setInputMask("")
        self.label_3.setText(QCoreApplication.translate("main", u"Email:", None))
        self.entry_line_3.setInputMask("")
        self.label_4.setText(QCoreApplication.translate("main", u"Daily SLP goal:", None))
        self.entry_line_4.setInputMask("")
        self.add.setText(QCoreApplication.translate("main", u"Confirm", None))
    # retranslateUi

