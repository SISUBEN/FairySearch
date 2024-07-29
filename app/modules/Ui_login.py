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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from .assets import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1391, 651)
        Form.setMinimumSize(QSize(1391, 651))
        Form.setMaximumSize(QSize(1391, 651))
        Form.setFocusPolicy(Qt.NoFocus)
        Form.setAcceptDrops(False)
        Form.setStyleSheet(u"background-color: #061c3e;")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, -10, 801, 671))
        self.label_3.setPixmap(QPixmap(u":/images/images/login.png"))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(740, 30, 682, 591))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(640, 200))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(40)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: white;")
        self.label_4.setTextFormat(Qt.RichText)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.username = QLineEdit(self.layoutWidget)
        self.username.setObjectName(u"username")
        self.username.setStyleSheet(u"background-color: white;")

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
        self.label_2.setStyleSheet(u"color: white;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.password = QLineEdit(self.layoutWidget)
        self.password.setObjectName(u"password")
        self.password.setMaximumSize(QSize(500, 16777215))
        self.password.setStyleSheet(u"background-color: white;")
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
        self.login_btn.setStyleSheet(u"color: white;background-color:grey;")

        self.horizontalLayout_3.addWidget(self.login_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.register_2 = QPushButton(self.layoutWidget)
        self.register_2.setObjectName(u"register_2")
        self.register_2.setMaximumSize(QSize(640, 16777215))
        self.register_2.setStyleSheet(u"color: white;")

        self.verticalLayout_2.addWidget(self.register_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Login", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6b22\u8fce\u8bbf\u95eeH.D.D System", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d\uff1a", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6   \u7801\uff1a", None))
        self.password.setInputMask("")
        self.password.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"\u767b\u5165", None))
        self.register_2.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
    # retranslateUi

