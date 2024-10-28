from app.__init__ import *
from app.modules.Ui_profile import Ui_Profile
from app.utils.time import TimeKeeper
from app.database.queries import Database
from app.libs.status import Status
from app.helper.widgetHelper import WidgetHelper
status = Status()
timekeeper = TimeKeeper() 
widget_helper = WidgetHelper()
db = Database

LOGIN = status.get_login()
LOGIN_UID = status.get_login_uid()

class ProfileWindow(QWidget, Ui_Profile):
    def __init__(self) -> None:
        super().__init__()
        logger.info(f"login user uid:{LOGIN_UID}")
        self.setupUi(self, LOGIN, LOGIN_UID)
        # disable zoom
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("Profile")
        # init search history
        # self.tableWidget.horizontalHeader
        # self.tableWidget.verticalHeaderItem
        self.tableWidget.setRowCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["浏览时间", "标题", "时长"])
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # bind slot
        self.onSearchHistory()
        self.changeAvatar.clicked.connect(self.onChangeAvatar)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/profile.png")
        painter.drawPixmap(self.rect(), pixmap)
    
    def addSearchHistory(self, title: str, time: int, duration: str) -> None:
        # rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(0)
        link = widget_helper.creatLink(content=title, target=self.onSearchHistory)
        # self.tableWidget.setItem(time, link, duration)
        formatted_time = timekeeper.datetime(time)
        self.tableWidget.setItem(0, 1, QTableWidgetItem(formatted_time))
        self.tableWidget.setCellWidget(0, 2, link)
        self.tableWidget.setItem(0, 3, QTableWidgetItem(duration))
    
    @timekeeper.timer
    def onSearchHistory(self) -> None:
        results = db.searchHisdb.query_search_history_all(LOGIN_UID)
        for row in results:
            title, timestamp, duration = row
            self.addSearchHistory(title, timestamp, duration)
            logger.debug(f"record: {row} has been added")

    def onChangeAvatar(self) -> None:
        ...