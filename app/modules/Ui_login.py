# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from .assets import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1279, 846)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 16777215))
        Form.setFocusPolicy(Qt.NoFocus)
        Form.setAcceptDrops(False)
        Form.setStyleSheet(u"QWidget#Form {\n"
        "	background-image: url(:/images/images/background.png)\n"
        "}")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(260, 120, 791, 641))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 150))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(40)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: white;")
        self.label_4.setTextFormat(Qt.RichText)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.username = QLineEdit(self.layoutWidget)
        self.username.setObjectName(u"username")
        self.username.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout.addWidget(self.username)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: white;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.password = QLineEdit(self.layoutWidget)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(526, 0))
        self.password.setMaximumSize(QSize(500, 16777215))
        self.password.setStyleSheet(u"QLineEdit {\n"
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
        self.password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.password)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.login_btn = QPushButton(self.layoutWidget)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(0, 0))
        self.login_btn.setMaximumSize(QSize(100, 50))
        font2 = QFont()
        font2.setPointSize(12)
        self.login_btn.setFont(font2)
        self.login_btn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.login_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.register_2 = QPushButton(self.layoutWidget)
        self.register_2.setObjectName(u"register_2")
        self.register_2.setMaximumSize(QSize(16777215, 16777215))
        self.register_2.setFont(font1)
        self.register_2.setStyleSheet(u"QPushButton#register_2 {\n"
"	color: #1a0dab;\n"
"	color: white;\n"
"	background-color:transparent;\n"
"}\n"
"QPushButton#register_2:pressed {\n"
"	color: #681DA8;\n"
"	background-color:transparent;\n"
"}\n"
"QPushButton#register_2:hover {\n"
"	text-decoration: underline;\n"
"	background-color:transparent;\n"
"}")

        self.horizontalLayout_4.addWidget(self.register_2)

        self.forget_password = QPushButton(self.layoutWidget)
        self.forget_password.setObjectName(u"forget_password")
        self.forget_password.setMaximumSize(QSize(16777215, 16777215))
        self.forget_password.setFont(font1)
        self.forget_password.setStyleSheet(u"QPushButton#forget_password {\n"
"	color: #1a0dab;\n"
"	color: white;\n"
"	background-color:transparent;\n"
"}\n"
"QPushButton#forget_password:pressed {\n"
"	color: #681DA8;\n"
"	background-color:transparent;\n"
"}\n"
"QPushButton#forget_password:hover {\n"
"	text-decoration: underline;\n"
"	background-color:transparent;\n"
"}")

        self.horizontalLayout_4.addWidget(self.forget_password)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Login", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6b22\u8fce\u8bbf\u95eeH.D.D System", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d\uff1a", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6    \u7801\uff1a", None))
        self.password.setInputMask("")
        self.password.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"\u767b\u5165", None))
        self.register_2.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.forget_password.setText(QCoreApplication.translate("Form", u"\u5fd8\u8bb0\u5bc6\u7801", None))
    # retranslateUi

