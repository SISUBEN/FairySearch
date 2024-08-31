# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1341, 873)
        mainWindow.setStyleSheet(u"QWidget#mainWindow {\n"
"	background-image: url(:/images/images/background.png);\n"
"	background-size:cover;\n"
"}")
        self.verticalLayoutWidget_2 = QWidget(mainWindow)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(70, 110, 1221, 701))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(240, 60))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(13, 13, 13);\n"
"    /*color: rgb(41, 41, 41);*/\n"
"	color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    width: 500px;\n"
"    border-radius: 25px;\n"
"	padding: 0 10%;\n"
"}\n"
"QLineEdit::placeholderText {\n"
"    font-size: 16px;\n"
"}")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(self.verticalLayoutWidget_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget {  \n"
"    background-color:#0f2033;\n"
"    border-top: 2px solid #C2C7CB;  \n"
"} \n"
"QTabWidget::pane { /* The tab widget frame */  \n"
"    border-top: 0px solid #C2C7CB;  \n"
"} \n"
" /* Style the tab using the tab sub-control. Note that \n"
"    it reads QTabBar _not_ QTabWidget */  \n"
"QTabBar::tab {  \n"
"    background-color:#0f2033;\n"
"    border: 1px solid #4973b4;  \n"
"    min-width: 100px; \n"
"    min-height:22px;\n"
"    padding: 0px  2px; \n"
"    color: rgb(255, 255, 255);\n"
"    margin-left: 1px;\n"
"    font: 75 12pt \" Microsoft YaHei \";\n"
"}  \n"
"  \n"
"QTabBar::tab:selected, QTabBar::tab:hover {  \n"
"    background-color: rgb(42,87,147);\n"
"    margin-top: 0px;\n"
"    \n"
"}  \n"
"  \n"
"QTabBar::tab:selected {  \n"
"    \n"
"    background-image: url(:/Images/Tab_Hover.png);\n"
"    \n"
"} \n"
"  \n"
"QTabBar::tab:!selected {  \n"
"    margin-top: 0px; /* make non-selected tabs look smaller */  \n"
"}  ")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-1, -1, 1221, 601))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1219, 599))
        self.gridLayoutWidget_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(-10, -10, 1231, 601))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.scrollArea_2 = QScrollArea(self.tab_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(-1, -1, 1221, 601))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1219, 599))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-1, -1, 1221, 601))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.profile = QPushButton(mainWindow)
        self.profile.setObjectName(u"profile")
        self.profile.setEnabled(True)
        self.profile.setGeometry(QRect(1220, 30, 1091, 71))
        self.profile.setStyleSheet(u"QPushButton#profile {\n"
"	background: transparent;\n"
"	background-image: url(:/icons/icons/icons.png)\n"
"}")

        self.retranslateUi(mainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"FairySearch", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("mainWindow", u"\u641c\u7d22\u89c6\u9891", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("mainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("mainWindow", u"Tab 2", None))
        self.profile.setText("")
    # retranslateUi

