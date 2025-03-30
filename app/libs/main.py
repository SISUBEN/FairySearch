from app.libs.video_browser import VideoBrowser
from app.libs.expection import NoLoginError, VideoNotFoundError
from app.libs.dialog import Dialog
from app import QApplication, QWidget, logger, QPainter, QPixmap

# to avoid circular import
def onClickVideos(vid: int) -> None:
    try:
        videosBrower = VideoBrowser(vid)
        logger.debug(f"onClickVideos: {vid}")
        videosBrower.show()
    except VideoNotFoundError:
        from app.i18n import _
        dialog = Dialog()
        logger.error(f"Video ID:{vid} does not exist")
        dialog.standard(_("无法找到该视频"), _(f"视频【{vid}】不存在"))

from app.modules.ui_main import Ui_MainWindow, ItemWidget, PageWidget
from app.libs.profile import ProfileWindow
from app.database.videos import Videodb
from app.utils.time import TimeKeeper
from app.libs.setting import SettingWindow
from app.i18n import _

class MainWindow(
    QWidget,
    Ui_MainWindow,
):
    def __init__(self, token: str, app: QApplication) -> None:
        super().__init__()
        self.app = app
        self.videodb = Videodb()
        
        self.__token = token
        if self.__token is None:
            raise NoLoginError
        self.bg_image_path = ":/images/images/background.png"  # using QRC path
        self.def_cover_path = ":/covers/covers/default.png"  # using QRC path
        self.pages_data = self.getVideos()
        self.setupUi(self, self.pages_data)

        # bind click events
        self.prev_button.clicked.connect(self.showPrevPage)
        self.next_button.clicked.connect(self.showNextPage)
        self.page_number.editingFinished.connect(self.jump2Page)
        self.search_box.returnPressed.connect(lambda x: logger.debug(f"search_box: {x}"))
        self.user_profile_btn.clicked.connect(self.showUserProfile)
        self.setting_btn.clicked.connect(self.showSetting)
        self.updateButtons()
        
    @TimeKeeper.timer
    def getVideos(
        self, page_size: int = 9
    ) -> list:
        results = self.videodb.query_videos_all()
        videos = [
            {"cover": result[2], "title": result[1], "vid": result[0]}
            for result in results
        ]
        # Split videos into pages
        pages = [videos[i:i + page_size] for i in range(0, len(videos), page_size)]
        return pages

    def appendPage(self, *items_data: list) -> None:
        for data in items_data:
            self.pages_data.append(data)
            self.loadPage(len(self.pages_data) - 1)
            self.updateButtons()

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(f"{self.bg_image_path}")
        # pixmap = QPixmap(":/images/background.png")
        painter.drawPixmap(self.rect(), pixmap)

    def jump2Page(self) -> None:
        page_num = int(self.page_number.text())
        if page_num < 0 or page_num < len(self.pages_data) - 1:
            return
        self.current_page = page_num - 1
        self.loadPage(self.current_page)
        self.updateButtons()

    def showUserProfile(self) -> None:
        if self.__token:  # if user logged in
            self.profileWindow = ProfileWindow(self.__token)
            self.profileWindow.show()
        else:
            raise NoLoginError
    
    def showSetting(self) -> None:
        self.settingWindow = SettingWindow(self.app)
        self.settingWindow.show()

    # Lazy loading
    def loadPage(self, page_index: int) -> None:
        if page_index not in self.page_cache:
            if 0 <= page_index < len(self.pages_data):
                page = PageWidget(self.pages_data[page_index])
                self.stacked_widget.addWidget(page)
                self.page_cache[page_index] = page  # cecha page
        self.stacked_widget.setCurrentIndex(page_index)

    def showPrevPage(self) -> None:
        if self.current_page > 0:
            self.current_page -= 1
            self.page_number.setText(str(self.current_page + 1))
            self.loadPage(self.current_page)  # load prev page
            self.updateButtons()

    def showNextPage(self) -> None:
        if self.current_page < len(self.pages_data) - 1:
            self.current_page += 1
            self.page_number.setText(str(self.current_page + 1))
            self.loadPage(self.current_page)  # load next page
            self.updateButtons()

    def updateButtons(self) -> None:
        self.prev_button.setEnabled(self.current_page > 0)
        self.next_button.setEnabled(self.current_page < len(self.pages_data) - 1)