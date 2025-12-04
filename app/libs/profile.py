from app import (
    QWidget,
    QTableWidget,
    QPainter,
    QPixmap,
    logger,
    Qt,
    QTableWidgetItem,
)
from app.modules.ui_profile import Ui_Profile
from app.utils.time import TimeKeeper
from app.database.users import Userdb
from app.database.search_history import SearchHistorydb
from app.helper.widget import WidgetCreator
from app.i18n import _

class ProfileWindow(QWidget, Ui_Profile):
    def __init__(self, token: str) -> None:
        super().__init__()
        self.userdb = Userdb()
        self.searchHisdb = SearchHistorydb()
        self.widget_helper = WidgetCreator()
        self.timekeeper = TimeKeeper()
        
        self.__name = self.userdb.get_username(token)
        self.__uid = self.userdb.get(token)
        self.setupUi(self, self.__name, self.__uid)
        
        # disable zoom
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle(_("个人资料"))
        
        # init search history
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(
            [_("浏览时间"), _("标题"), _("时长")]
        )
        self.tableWidget.setColumnHidden(3, True)  # only for listener function
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        
        # bind slot
        self.onSearchHistory()
        self.changeAvatar.clicked.connect(self.onChangeAvatar)
        self.RecomImmediatelyBtn.clicked.connect(self.onClickRecomImme)
        # self.tableWidget.cellClicked.connect(self.onClickTitle)
        # self.tableWidget.cellDoubleClicked.connect(self.onClickTitle)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/profile.png")
        painter.drawPixmap(self.rect(), pixmap)

    def onClickTitle(self, vid: int):
        logger.debug(f"to vid: {vid}")
    
    def onClickRecomImme(self):
        from app.libs.dialog import Dialog
        self.dialog = Dialog()
        self.dialog.standard(
            title="⚠警告⚠",
            text="此功能透过填写一些与您相关\n的表单以向 FairyRecom 立即请求推荐的结果\n可能存在不准确的结果，您要继续吗？"
        )
        self.init_fairyrecom()
        import webbrowser
        webbrowser.open("http://localhost:8000/recom_form")
        
    def init_fairyrecom(self):
        import subprocess
        result = subprocess.Popen("python ../../FairyRecom/run_api.py", shell=True)
        if result.returncode != 0:
            logger.error("FairyRecom run_api.py failed")
            return
        logger.info("FairyRecom run_api.py success")

    def addSearchHistory(
        self,
        title: str,
        duration: str,
        vid: str,
        time: int = TimeKeeper.get_timestamp(),
    ) -> None:
        """add search history to table

        Args:
            title (str): search history title
            duration (str): the duration of the video
            uuid (str): the video uid
            time (int, optional): browsing time. Defaults to TimeKeeper.get_timestamp().
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
        title_item = self.widget_helper.creatLink(title, color="black")
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
        vid_item.setFlags(vid_item.flags() & ~Qt.ItemIsEditable)  # disable edit
        self.tableWidget.setItem(row_position, 3, vid_item)

    @TimeKeeper.timer
    def onSearchHistory(self) -> None:
        results = self.searchHisdb.query_all(self.__uid)
        # TODO: lazy load
        for row in results:
            title, timestamp, duration, uuid, vid = row
            self.addSearchHistory(
                title=title,
                time=self.timekeeper.datetime(timestamp),
                duration=duration,
                vid=vid,
            )
            logger.debug(f"record: {row} has been added")

    def onChangeAvatar(self) -> None: ...
