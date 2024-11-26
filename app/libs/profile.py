from app.__init__ import *
from app.modules.Ui_profile import Ui_Profile
from app.utils.time import TimeKeeper
from app.database.queries import Database
from app.helper.widgetHelper import WidgetHelper
timekeeper = TimeKeeper() 
widget_helper = WidgetHelper()
db = Database()

class ProfileWindow(QWidget, Ui_Profile):
    def __init__(self, token: str) -> None:
        super().__init__()
        self.__name = db.userdb.query_username(token)
        self.__uid = db.userdb.query_uid(token)
        self.setupUi(self, self.__name, self.__uid)
        # disable zoom
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("Profile")
        # init search history
        # self.tableWidget.horizontalHeader
        # self.tableWidget.verticalHeaderItem
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["浏览时间", "标题", "时长"])
        self.tableWidget.setColumnHidden(3, True) # only for listener function
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # bind slot
        self.onSearchHistory()
        self.changeAvatar.clicked.connect(self.onChangeAvatar)
        # self.tableWidget.cellClicked.connect(self.onClickTitle)
        # self.tableWidget.cellDoubleClicked.connect(self.onClickTitle)
        

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/profile.png")
        painter.drawPixmap(self.rect(), pixmap)
        
    def onClickTitle(self, vid: int):
        logger.debug(f"to vid: {vid}")
    
    def addSearchHistory(self, title: str, duration: str, vid: str, time: int = timekeeper.get_timestamp()) -> None:
        """add search history to table
        
        Args:
            title (str): search history title
            duration (str): the duration of the video
            uuid (str): the video uid
            time (int, optional): browsing time. Defaults to timekeeper.get_timestamp().
        """
        # calc new row num
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

        # add time
        time_item = QTableWidgetItem(str(time))
        time_item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(row_position, 0, time_item)

        # add title
        # title_item = QTableWidgetItem(title)
        title_item = widget_helper.creatLink(title, color="black")
        title_item.clicked.connect(lambda _, v=vid: self.onClickTitle(v))
        # title_item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setCellWidget(row_position, 1, title_item)
        
        # add duration
        duration_item = QTableWidgetItem(str(duration))
        duration_item.setTextAlignment(Qt.AlignCenter)
        self.tableWidget.setItem(row_position, 2, duration_item)
        
        # add uuid
        vid_item = QTableWidgetItem(vid)
        vid_item.setTextAlignment(Qt.AlignCenter)
        vid_item.setFlags(vid_item.flags() & ~Qt.ItemIsEditable) # disable edit
        self.tableWidget.setItem(row_position, 3, vid_item) 
    
    @timekeeper.timer
    def onSearchHistory(self) -> None:
        results = db.searchHisdb.query_search_history_all(self.__uid)
        # TODO: lazy load
        for row in results:
            title, timestamp, duration, uuid, vid = row
            self.addSearchHistory(
                title=title,
                time=timekeeper.datetime(timestamp), 
                duration=duration, 
                vid=vid
            )
            logger.debug(f"record: {row} has been added")

    def onChangeAvatar(self) -> None:
        ...