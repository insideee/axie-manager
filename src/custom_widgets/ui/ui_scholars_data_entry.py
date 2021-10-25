# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_students_data_entrysgjrjcx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dataEntryCreator(object):
    def setupUi(self, dataEntryCreator):
        if not dataEntryCreator.objectName():
            dataEntryCreator.setObjectName(u"dataEntryCreator")
        dataEntryCreator.resize(843, 30)
        dataEntryCreator.setMinimumSize(QSize(250, 30))
        dataEntryCreator.setMaximumSize(QSize(16777215, 30))
        dataEntryCreator.setStyleSheet(u"QWidget{border: 0px;\n"
"border-bottom: 1px solid #61676D;\n"
"border-left: 1px solid #61676D;\n"
"border-right: 1px solid #61676D;\n"
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
        self.horizontalLayout_2.setContentsMargins(4, 0, 0, 0)
        self.nameData = QLabel(self.dataContainer)
        self.nameData.setObjectName(u"nameData")
        self.nameData.setMinimumSize(QSize(100, 0))
        self.nameData.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_2.addWidget(self.nameData)

        self.roninData = QLabel(self.dataContainer)
        self.roninData.setObjectName(u"roninData")
        self.roninData.setMinimumSize(QSize(100, 0))
        self.roninData.setMaximumSize(QSize(9999999, 16777215))

        self.horizontalLayout_2.addWidget(self.roninData)

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

        self.roninData.raise_()
        self.nameData.raise_()
        self.mmrData.raise_()
        self.rankData.raise_()

        self.horizontalLayout.addWidget(self.dataContainer, 0, Qt.AlignVCenter)

        self.slpDataContainer = QWidget(self.data)
        self.slpDataContainer.setObjectName(u"slpDataContainer")
        self.slpDataContainer.setMinimumSize(QSize(160, 0))
        self.slpDataContainer.setMaximumSize(QSize(400, 16777215))
        self.slpDataContainer.setStyleSheet(u"QWidget{border:0px}")
        self.horizontalLayout_3 = QHBoxLayout(self.slpDataContainer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 0, 1, 0)
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

        self.slpGoalData = QLabel(self.slpDataContainer)
        self.slpGoalData.setObjectName(u"slpGoalData")
        self.slpGoalData.setMinimumSize(QSize(30, 0))
        self.slpGoalData.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_3.addWidget(self.slpGoalData)

        self.slpTodayData = QLabel(self.slpDataContainer)
        self.slpTodayData.setObjectName(u"slpTodayData")
        self.slpTodayData.setMinimumSize(QSize(30, 0))
        self.slpTodayData.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_3.addWidget(self.slpTodayData)


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
        self.mmrData.setText(QCoreApplication.translate("dataEntryCreator", u"MMR", None))
        self.rankData.setText(QCoreApplication.translate("dataEntryCreator", u"Rank", None))
        self.totalSlpData.setText(QCoreApplication.translate("dataEntryCreator", u"Total SLP", None))
        self.averageData.setText(QCoreApplication.translate("dataEntryCreator", u"avg SLP", None))
        self.slpGoalData.setText(QCoreApplication.translate("dataEntryCreator", u"SLP Goal", None))
        self.slpTodayData.setText(QCoreApplication.translate("dataEntryCreator", u"SLP Today", None))
    # retranslateUi

