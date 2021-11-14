# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_scholars_data_entryspesYSX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

try:
        import resources.resources_rc
except ModuleNotFoundError:
        import src.resources.resources_rc

class Ui_dataEntryCreator(object):
    def setupUi(self, dataEntryCreator):
        if not dataEntryCreator.objectName():
            dataEntryCreator.setObjectName(u"dataEntryCreator")
        dataEntryCreator.resize(879, 30)
        dataEntryCreator.setMinimumSize(QSize(250, 30))
        dataEntryCreator.setMaximumSize(QSize(16777215, 30))
        dataEntryCreator.setMouseTracking(True)
        dataEntryCreator.setStyleSheet(u"QWidget{border: 0px;\n"
"border-bottom: 1px solid #61676D;\n"
"border-top-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;}\n"
"\n"
"QLabel{border: 0px}")
        self.verticalLayout = QVBoxLayout(dataEntryCreator)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.data = QWidget(dataEntryCreator)
        self.data.setObjectName(u"data")
        self.data.setMinimumSize(QSize(0, 30))
        self.data.setMaximumSize(QSize(16777215, 30))
        self.data.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.data)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 0, 2, 0)
        self.dataContainer = QWidget(self.data)
        self.dataContainer.setObjectName(u"dataContainer")
        self.dataContainer.setMinimumSize(QSize(350, 0))
        self.dataContainer.setStyleSheet(u"QWidget{border: 0px;}")
        self.horizontalLayout_2 = QHBoxLayout(self.dataContainer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 0, 0, 0)
        self.nameContainer = QWidget(self.dataContainer)
        self.nameContainer.setObjectName(u"nameContainer")
        self.nameContainer.setMinimumSize(QSize(100, 0))
        self.nameContainer.setMaximumSize(QSize(250, 16777215))
        self.horizontalLayout_6 = QHBoxLayout(self.nameContainer)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.nameEdit = QLineEdit(self.nameContainer)
        self.nameEdit.setObjectName(u"nameEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameEdit.sizePolicy().hasHeightForWidth())
        self.nameEdit.setSizePolicy(sizePolicy)
        self.nameEdit.setMinimumSize(QSize(100, 0))
        self.nameEdit.setMaximumSize(QSize(100, 20))
        self.nameEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid #737373;\n"
"color: #61676D;")

        self.horizontalLayout_6.addWidget(self.nameEdit)

        self.nameData = QLabel(self.nameContainer)
        self.nameData.setObjectName(u"nameData")
        self.nameData.setMinimumSize(QSize(100, 0))
        self.nameData.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_6.addWidget(self.nameData)


        self.horizontalLayout_2.addWidget(self.nameContainer, 0, Qt.AlignVCenter)

        self.roninContainer = QWidget(self.dataContainer)
        self.roninContainer.setObjectName(u"roninContainer")
        self.roninContainer.setMinimumSize(QSize(100, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.roninContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.roninData = QLabel(self.roninContainer)
        self.roninData.setObjectName(u"roninData")
        self.roninData.setMinimumSize(QSize(90, 0))
        self.roninData.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_4.addWidget(self.roninData)

        self.copyBtn = QToolButton(self.roninContainer)
        self.copyBtn.setObjectName(u"copyBtn")
        icon = QIcon()
        icon.addFile(u":/images/img/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.copyBtn.setIcon(icon)
        self.copyBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_4.addWidget(self.copyBtn)


        self.horizontalLayout_2.addWidget(self.roninContainer, 0, Qt.AlignLeft)

        self.mmrData = QLabel(self.dataContainer)
        self.mmrData.setObjectName(u"mmrData")
        self.mmrData.setMinimumSize(QSize(60, 0))
        self.mmrData.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.mmrData)

        self.rankData = QLabel(self.dataContainer)
        self.rankData.setObjectName(u"rankData")
        self.rankData.setMinimumSize(QSize(80, 0))
        self.rankData.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.rankData)


        self.horizontalLayout.addWidget(self.dataContainer, 0, Qt.AlignVCenter)

        self.slpDataContainer = QWidget(self.data)
        self.slpDataContainer.setObjectName(u"slpDataContainer")
        self.slpDataContainer.setMinimumSize(QSize(160, 0))
        self.slpDataContainer.setMaximumSize(QSize(400, 16777215))
        self.slpDataContainer.setStyleSheet(u"QWidget{border:0px}")
        self.horizontalLayout_3 = QHBoxLayout(self.slpDataContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 0, 1, 1)
        self.totalSlpData = QLabel(self.slpDataContainer)
        self.totalSlpData.setObjectName(u"totalSlpData")
        self.totalSlpData.setMinimumSize(QSize(80, 0))
        self.totalSlpData.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_3.addWidget(self.totalSlpData)

        self.averageData = QLabel(self.slpDataContainer)
        self.averageData.setObjectName(u"averageData")
        self.averageData.setMinimumSize(QSize(30, 0))
        self.averageData.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_3.addWidget(self.averageData)

        self.slpGoalContainer = QWidget(self.slpDataContainer)
        self.slpGoalContainer.setObjectName(u"slpGoalContainer")
        self.slpGoalContainer.setMinimumSize(QSize(30, 0))
        self.slpGoalContainer.setMaximumSize(QSize(90, 16777215))
        self.horizontalLayout_7 = QHBoxLayout(self.slpGoalContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.slpGoalEdit = QLineEdit(self.slpGoalContainer)
        self.slpGoalEdit.setObjectName(u"slpGoalEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slpGoalEdit.sizePolicy().hasHeightForWidth())
        self.slpGoalEdit.setSizePolicy(sizePolicy1)
        self.slpGoalEdit.setMinimumSize(QSize(30, 0))
        self.slpGoalEdit.setMaximumSize(QSize(90, 20))
        self.slpGoalEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border: 1px solid #737373;\n"
"color: #61676D;")

        self.horizontalLayout_7.addWidget(self.slpGoalEdit)

        self.slpGoalData = QLabel(self.slpGoalContainer)
        self.slpGoalData.setObjectName(u"slpGoalData")
        self.slpGoalData.setMinimumSize(QSize(30, 0))
        self.slpGoalData.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_7.addWidget(self.slpGoalData)


        self.horizontalLayout_3.addWidget(self.slpGoalContainer)

        self.btnContainer = QWidget(self.slpDataContainer)
        self.btnContainer.setObjectName(u"btnContainer")
        self.btnContainer.setMinimumSize(QSize(30, 0))
        self.btnContainer.setMaximumSize(QSize(90, 16777215))
        self.horizontalLayout_5 = QHBoxLayout(self.btnContainer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(4, 0, 1, 1)
        self.slpTodayData = QLabel(self.btnContainer)
        self.slpTodayData.setObjectName(u"slpTodayData")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slpTodayData.sizePolicy().hasHeightForWidth())
        self.slpTodayData.setSizePolicy(sizePolicy2)
        self.slpTodayData.setMinimumSize(QSize(0, 0))
        self.slpTodayData.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_5.addWidget(self.slpTodayData)

        self.editBtn = QToolButton(self.btnContainer)
        self.editBtn.setObjectName(u"editBtn")
        self.editBtn.setMinimumSize(QSize(21, 21))
        icon1 = QIcon()
        icon1.addFile(u":/images/img/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editBtn.setIcon(icon1)
        self.editBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.editBtn)

        self.delBtn = QToolButton(self.btnContainer)
        self.delBtn.setObjectName(u"delBtn")
        self.delBtn.setMinimumSize(QSize(21, 21))
        icon2 = QIcon()
        icon2.addFile(u":/images/img/del.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delBtn.setIcon(icon2)
        self.delBtn.setIconSize(QSize(18, 18))

        self.horizontalLayout_5.addWidget(self.delBtn)


        self.horizontalLayout_3.addWidget(self.btnContainer)


        self.horizontalLayout.addWidget(self.slpDataContainer, 0, Qt.AlignVCenter)

        self.slpDataContainer.raise_()
        self.dataContainer.raise_()

        self.verticalLayout.addWidget(self.data)


        self.retranslateUi(dataEntryCreator)

        QMetaObject.connectSlotsByName(dataEntryCreator)
    # setupUi

    def retranslateUi(self, dataEntryCreator):
        dataEntryCreator.setWindowTitle(QCoreApplication.translate("dataEntryCreator", u"Form", None))
        self.nameData.setText(QCoreApplication.translate("dataEntryCreator", u"Name", None))
        self.roninData.setText(QCoreApplication.translate("dataEntryCreator", u"Ronin", None))
        self.copyBtn.setText("")
        self.mmrData.setText(QCoreApplication.translate("dataEntryCreator", u"MMR", None))
        self.rankData.setText(QCoreApplication.translate("dataEntryCreator", u"Rank", None))
        self.totalSlpData.setText(QCoreApplication.translate("dataEntryCreator", u"Total SLP", None))
        self.averageData.setText(QCoreApplication.translate("dataEntryCreator", u"avg SLP", None))
        self.slpGoalData.setText(QCoreApplication.translate("dataEntryCreator", u"SLP Goal", None))
        self.slpTodayData.setText(QCoreApplication.translate("dataEntryCreator", u"0", None))
        self.editBtn.setText("")
        self.delBtn.setText(QCoreApplication.translate("dataEntryCreator", u"...", None))
    # retranslateUi

