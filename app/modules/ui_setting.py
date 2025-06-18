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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)
from app.assets import resources_rc

class Ui_SettingWindow(object):
    def setupUi(self, SettingWindow):
        if not SettingWindow.objectName():
            SettingWindow.setObjectName(u"SettingWindow")
        SettingWindow.resize(1139, 732)
        SettingWindow.setStyleSheet(u"QWidget {\n"
"	background-color: url(:/images/images/background.png);\n"
"    width:100%;\n"
"    height:100%;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(SettingWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, 20, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title = QLabel(SettingWindow)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(20)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"/*QTabWidget*/\n"
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

        self.horizontalLayout.addWidget(self.title)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.tabWidget = QTabWidget(SettingWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        font1.setPointSize(12)
        self.tabWidget.setFont(font1)
        self.langSettingPage = QWidget()
        self.langSettingPage.setObjectName(u"langSettingPage")
        self.langSettingPage.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.langSettingPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.langVLayout = QVBoxLayout()
        self.langVLayout.setObjectName(u"langVLayout")

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

        self.verticalLayout_6.addLayout(self.devVLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.devSettinPage, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 40)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(SettingWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SettingWindow)
    # setupUi

    def retranslateUi(self, SettingWindow):
        SettingWindow.setWindowTitle(QCoreApplication.translate("SettingWindow", u"Form", None))
        self.title.setText(QCoreApplication.translate("SettingWindow", u"FairySearch - \u8bbe\u5b9a", None))
        self.tabWidget.setStyleSheet(QCoreApplication.translate("SettingWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.langSettingPage), QCoreApplication.translate("SettingWindow", u"\u8bed\u8a00", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.devSettinPage), QCoreApplication.translate("SettingWindow", u"\u5f00\u53d1\u8005\u8bbe\u5b9a", None))
    # retranslateUi

