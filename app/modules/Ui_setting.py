# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)
from app.assets import resources_rc

class Ui_SettingWindow(object):
    def setupUi(self, SettingWindow):
        if not SettingWindow.objectName():
            SettingWindow.setObjectName(u"SettingWindow")
        SettingWindow.resize(1139, 701)
        SettingWindow.setStyleSheet(u"QWidget {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.987, y2:1, stop:0.159686 rgba(10, 10, 10, 255), stop:0.465969 rgba(43, 42, 40, 255), stop:1 rgba(108, 108, 108, 255))\n"
"    width:100%;\n"
"    height:100%;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(SettingWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(SettingWindow)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"/*QTabWidget*/\n"
"QTabWidget::pane{\n"
"border:none;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"     left: 5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"     background: gray;\n"
"     /*border: 2px solid #C4C4C3;*/\n"
"     border-bottom-color: #C2C7CB;\n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     min-width: 60px;\n"
"     padding: 2px;\n"
" }\n"
"\n"
"QTabBar::tab:selected{\n"
"    background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #626262,stop:1 #545454);\n"
"}\n"
"\n"
"QTabBar::tab:!selected{\n"
"    margin-top:5px;\n"
"}\n"
"/*\u56db\u4e2a\u4e0b\u5c5e\u754c\u9762*/\n"
"#tab,#tab_2,#tab_3,#tab_4{\n"
"    background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #626262,stop:1 #545454);\n"
"    border-radius:6px;\n"
"}")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(SettingWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(12)
        self.tabWidget.setFont(font1)
        self.tabWidget.setStyleSheet(u"/*QTabWidget*/\n"
"QTabWidget::pane{\n"
"border:none;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"     left: 5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"     background: gray;\n"
"     /*border: 2px solid #C4C4C3;*/\n"
"     border-bottom-color: #C2C7CB;\n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     min-width: 60px;\n"
"     padding: 2px;\n"
" }\n"
"\n"
"QTabBar::tab:selected{\n"
"    background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #626262,stop:1 #545454);\n"
"}\n"
"\n"
"QTabBar::tab:!selected{\n"
"    margin-top:5px;\n"
"}\n"
"/*\u56db\u4e2a\u4e0b\u5c5e\u754c\u9762*/\n"
"/*#tabWidget > QWidget*/\n"
"QWidget #devSettingPage #langSettingPage  {\n"
"	border:1px solid gray;\n"
"}")
        self.langSettingPage = QWidget()
        self.langSettingPage.setObjectName(u"langSettingPage")
        self.langSettingPage.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.langSettingPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.langVLayout = QVBoxLayout()
        self.langVLayout.setObjectName(u"langVLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.langSettingPage)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))
        self.label.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei"])
        font2.setPointSize(11)
        self.label.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label)

        self.langComboBox = QComboBox(self.langSettingPage)
        self.langComboBox.setObjectName(u"langComboBox")
        self.langComboBox.setMinimumSize(QSize(500, 0))
        self.langComboBox.setMaximumSize(QSize(400, 20))

        self.horizontalLayout_2.addWidget(self.langComboBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.langVLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.langVLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.langSettingPage, "")
        self.devSettinPage = QWidget()
        self.devSettinPage.setObjectName(u"devSettinPage")
        self.verticalLayout_6 = QVBoxLayout(self.devSettinPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.devVLayout = QVBoxLayout()
        self.devVLayout.setObjectName(u"devVLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.devSettinPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setMaximumSize(QSize(150, 16777215))
        self.label_3.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.langComboBox_2 = QComboBox(self.devSettinPage)
        self.langComboBox_2.setObjectName(u"langComboBox_2")
        self.langComboBox_2.setMinimumSize(QSize(500, 0))
        self.langComboBox_2.setMaximumSize(QSize(400, 20))

        self.horizontalLayout_3.addWidget(self.langComboBox_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.devVLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addLayout(self.devVLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.devSettinPage, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(SettingWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingWindow)
    # setupUi

    def retranslateUi(self, SettingWindow):
        SettingWindow.setWindowTitle(QCoreApplication.translate("SettingWindow", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("SettingWindow", u"FairySearch - \u8bbe\u5b9a", None))
        self.label.setText(QCoreApplication.translate("SettingWindow", u"\u754c\u9762\u8bed\u8a00\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.langSettingPage), QCoreApplication.translate("SettingWindow", u"\u8bed\u8a00", None))
        self.label_3.setText(QCoreApplication.translate("SettingWindow", u"\u65e5\u5fd7\u7b49\u7ea7\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.devSettinPage), QCoreApplication.translate("SettingWindow", u"\u5f00\u53d1\u8005\u8bbe\u5b9a", None))
    # retranslateUi

