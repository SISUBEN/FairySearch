# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'videoBrowser.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)
from app.assets import resources_rc

class Ui_VideoBrowser(object):
    def setupUi(self, VideoBrowser):
        if not VideoBrowser.objectName():
            VideoBrowser.setObjectName(u"VideoBrowser")
        VideoBrowser.resize(925, 688)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VideoBrowser.sizePolicy().hasHeightForWidth())
        VideoBrowser.setSizePolicy(sizePolicy)
        VideoBrowser.setStyleSheet(u"QWidget #VideoBrowser {\n"
"	border-image: url(:/images/images/background.png);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(VideoBrowser)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, 20, 40, 20)
        self.video_frame = QFrame(VideoBrowser)
        self.video_frame.setObjectName(u"video_frame")
        sizePolicy.setHeightForWidth(self.video_frame.sizePolicy().hasHeightForWidth())
        self.video_frame.setSizePolicy(sizePolicy)
        self.video_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.video_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.video_frame)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.position_slider = QSlider(VideoBrowser)
        self.position_slider.setObjectName(u"position_slider")
        self.position_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_3.addWidget(self.position_slider)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.play_button = QPushButton(VideoBrowser)
        self.play_button.setObjectName(u"play_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy1)
        self.play_button.setMinimumSize(QSize(60, 60))
        self.play_button.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/icons/play.svg);\n"
"    background-position: centre centre;\n"
"    background-repeat: no-repeat;\n"
"	background-color:transparent;\n"
"}")

        self.horizontalLayout.addWidget(self.play_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.volume_slider = QSlider(VideoBrowser)
        self.volume_slider.setObjectName(u"volume_slider")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.volume_slider.sizePolicy().hasHeightForWidth())
        self.volume_slider.setSizePolicy(sizePolicy2)
        self.volume_slider.setMinimumSize(QSize(0, 0))
        self.volume_slider.setMaximumSize(QSize(100, 16777215))
        self.volume_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.volume_slider)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title = QLabel(VideoBrowser)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")

        self.verticalLayout_2.addWidget(self.title)

        self.describe = QLabel(VideoBrowser)
        self.describe.setObjectName(u"describe")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(12)
        self.describe.setFont(font1)
        self.describe.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"}")

        self.verticalLayout_2.addWidget(self.describe)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.like = QPushButton(VideoBrowser)
        self.like.setObjectName(u"like")
        self.like.setMinimumSize(QSize(30, 30))
        self.like.setMaximumSize(QSize(30, 30))
        self.like.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/icons/like.png);\n"
"	background-color:transparent;\n"
"    background-position: top left;\n"
"    background-repeat: no-repeat;\n"
"}")

        self.horizontalLayout_2.addWidget(self.like)

        self.coin = QPushButton(VideoBrowser)
        self.coin.setObjectName(u"coin")
        self.coin.setMinimumSize(QSize(30, 30))
        self.coin.setMaximumSize(QSize(30, 30))
        self.coin.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/icons/coin.png);\n"
"	background-color:transparent;\n"
"    background-position: top left;\n"
"    background-repeat: no-repeat;\n"
"}")

        self.horizontalLayout_2.addWidget(self.coin)

        self.favorite = QPushButton(VideoBrowser)
        self.favorite.setObjectName(u"favorite")
        self.favorite.setMinimumSize(QSize(30, 30))
        self.favorite.setMaximumSize(QSize(30, 30))
        self.favorite.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icons/icons/favorite.png);\n"
"	background-color:transparent;\n"
"    background-position: top left;\n"
"    background-repeat: no-repeat;\n"
"}")

        self.horizontalLayout_2.addWidget(self.favorite)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.retranslateUi(VideoBrowser)

        QMetaObject.connectSlotsByName(VideoBrowser)
    # setupUi

    def retranslateUi(self, VideoBrowser):
        VideoBrowser.setWindowTitle(QCoreApplication.translate("VideoBrowser", u"Form", None))
#if QT_CONFIG(whatsthis)
        self.position_slider.setWhatsThis(QCoreApplication.translate("VideoBrowser", u"\u8c03\u6574\u89c6\u9891\u4f4d\u7f6e", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.play_button.setWhatsThis(QCoreApplication.translate("VideoBrowser", u"\u64ad\u653e/\u6682\u505c", None))
#endif // QT_CONFIG(whatsthis)
        self.play_button.setText("")
#if QT_CONFIG(whatsthis)
        self.volume_slider.setWhatsThis(QCoreApplication.translate("VideoBrowser", u"\u58f0\u91cf", None))
#endif // QT_CONFIG(whatsthis)
        self.title.setText(QCoreApplication.translate("VideoBrowser", u"Title", None))
        self.describe.setText(QCoreApplication.translate("VideoBrowser", u"desc", None))
#if QT_CONFIG(whatsthis)
        self.like.setWhatsThis(QCoreApplication.translate("VideoBrowser", u"\u70b9\u8d5e", None))
#endif // QT_CONFIG(whatsthis)
        self.like.setText("")
#if QT_CONFIG(whatsthis)
        self.coin.setWhatsThis(QCoreApplication.translate("VideoBrowser", u"\u6295\u5e01", None))
#endif // QT_CONFIG(whatsthis)
        self.coin.setText("")
#if QT_CONFIG(whatsthis)
        self.favorite.setWhatsThis(QCoreApplication.translate("VideoBrowser", u"\u6536\u85cf", None))
#endif // QT_CONFIG(whatsthis)
        self.favorite.setText("")
    # retranslateUi

