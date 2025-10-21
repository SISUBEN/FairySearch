# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from ..assets import resources_rc

class Ui_Profile(object):
    def setupUi(self, Profile, username, uid):
        if not Profile.objectName():
            Profile.setObjectName(u"Profile")
        Profile.resize(1053, 601)
        Profile.setMinimumSize(QSize(1053, 601))
        Profile.setStyleSheet(u"QWidget#Profile {\n"
"	background-image: url(:/images/images/profile.png);\n"
"}")
        self.username = QLabel(Profile)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(140, 410, 151, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.username.setFont(font)
        self.username.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"\n"
"}")
        self.uid = QLabel(Profile)
        self.uid.setObjectName(u"uid")
        self.uid.setGeometry(QRect(80, 480, 211, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.uid.setFont(font1)
        self.uid.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"\n"
"}")
        self.username_3 = QLabel(Profile)
        self.username_3.setObjectName(u"username_3")
        self.username_3.setGeometry(QRect(360, 70, 151, 41))
        self.username_3.setFont(font)
        self.username_3.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"\n"
"}")
        self.changeAvatar = QPushButton(Profile)
        self.changeAvatar.setObjectName(u"changeAvatar")
        self.changeAvatar.setGeometry(QRect(80, 410, 41, 41))
        self.changeAvatar.setStyleSheet(u"QPushButton {\n"
"	background: transparent\n"
"}")
        self.tableWidget = QTableWidget(Profile)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(365, 121, 601, 341))
        self.verticalLayoutWidget = QWidget(Profile)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(360, 480, 161, 58))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.RecomImmediatelyBtn = QPushButton(self.verticalLayoutWidget)
        self.RecomImmediatelyBtn.setObjectName(u"RecomImmediatelyBtn")
        self.RecomImmediatelyBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border: 3px solid #262626;\n"
"    height: 50px;\n"
"    /*width: 500px;*/\n"
"    border-radius: 25px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #a6c100;\n"
"    color: black;\n"
"    border: 5px solid #a6c100;\n"
"}")

        self.verticalLayout.addWidget(self.RecomImmediatelyBtn)


        self.retranslateUi(Profile, username, uid)

        QMetaObject.connectSlotsByName(Profile)
    # setupUi

    def retranslateUi(self, Profile, username, uid):
        Profile.setWindowTitle(QCoreApplication.translate("Profile", u"Profile", None))
        self.username.setText(QCoreApplication.translate("Profile", f"{username}", None))
        self.uid.setText(QCoreApplication.translate("Profile", f"UID: {uid}", None))
        self.username_3.setText(QCoreApplication.translate("Profile", f"{username}", None))
        self.changeAvatar.setText("")
        self.RecomImmediatelyBtn.setText(QCoreApplication.translate("Profile", u"\u7acb\u5373\u63a8\u8350(Beta)", None))
    # retranslateUi

