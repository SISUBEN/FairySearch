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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)
from .assets import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1338, 901)
        MainWindow.setStyleSheet(u"QWidget#mainWindow {\n"
"	background-image:url(:/images/images/background.png);\n"
"	background-size:cover;\n"
"}")
        self.verticalLayoutWidget_2 = QWidget(MainWindow)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(70, 110, 1221, 701))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_box = QLineEdit(self.verticalLayoutWidget_2)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setMinimumSize(QSize(240, 60))
        self.search_box.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout.addWidget(self.search_box)


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

        self.profile = QPushButton(MainWindow)
        self.profile.setObjectName(u"profile")
        self.profile.setEnabled(True)
        self.profile.setGeometry(QRect(1220, 20, 1091, 71))
        self.profile.setStyleSheet(u"QPushButton#profile {\n"
"	background: transparent;\n"
"	background-image: url(:/icons/icons/icons.png)\n"
"}")
        self.horizontalLayoutWidget = QWidget(MainWindow)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(70, 20, 1221, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalLayoutWidget_2 = QWidget(MainWindow)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(570, 830, 216, 61))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.prev_page_btn = QPushButton(self.horizontalLayoutWidget_2)
        self.prev_page_btn.setObjectName(u"prev_page_btn")
        self.prev_page_btn.setMaximumSize(QSize(60, 50))
        self.prev_page_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    width: 500px;\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6c100;\n"
"    color: black;\n"
"    border: 5px solid #a6c100;\n"
"}")

        self.horizontalLayout_4.addWidget(self.prev_page_btn)

        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(20, 16777215))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.page_num = QLineEdit(self.horizontalLayoutWidget_2)
        self.page_num.setObjectName(u"page_num")
        self.page_num.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_4.addWidget(self.page_num)

        self.label_3 = QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(20, 16777215))
        self.label_3.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.next_page_btn = QPushButton(self.horizontalLayoutWidget_2)
        self.next_page_btn.setObjectName(u"next_page_btn")
        self.next_page_btn.setMaximumSize(QSize(60, 50))
        self.next_page_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    width: 500px;\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6c100;\n"
"    color: black;\n"
"    border: 5px solid #a6c100;\n"
"}")

        self.horizontalLayout_4.addWidget(self.next_page_btn)


        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FairySearch", None))
        self.search_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u89c6\u9891", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.profile.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fairy Search Engine", None))
        self.prev_page_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u9875", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7b2c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u9875", None))
        self.next_page_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9875", None))
    # retranslateUi

