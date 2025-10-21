from typing import Callable
from app.libs.video_browser import VideoBrowser
from app.libs.exception import NoLoginError, VideoNotFoundError
from app.libs.dialog import Dialog
from app.libs.search_window import SearchWindow
from app import QApplication, QWidget, logger, QPainter, QPixmap, QPushButton

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

from app.modules.ui_main import Ui_MainWindow, ItemWidget, PageWidget, QStackedWidget
from app.libs.profile import ProfileWindow
from app.libs.setting import SettingWindow
from app.database.videos import Videodb
from app.database.search import Searchdb
from app.database.db_config import Config, Default
from app.utils.time import TimeKeeper
from app import QGridLayout
from app.i18n import _
import trace


class MainWindow(
    QWidget,
    Ui_MainWindow,
):
    def __init__(self, token: str, app: QApplication) -> None:
        super().__init__()
        self.app = app
        self.videodb = Videodb()
        self.searchdb = Searchdb()
        self.search_result = []
        self.search_cache = []

        self.__token = token
        if self.__token is None:
            raise NoLoginError
        self.bg_image_path = ":/images/images/background.png"
        self.def_cover_path = ":/covers/covers/default.png"
        self.null_cover_path = ""
        self.pages_data = self.getVideos()
        self.setupUi(self, self.pages_data)

        self.user_profile_btn: QPushButton
        self.setting_btn: QPushButton
        # bind click events
        self.prev_button.clicked.connect(self.showPrevPage)
        self.next_button.clicked.connect(self.showNextPage)
        self.page_number.editingFinished.connect(self.jump2Page)
        self.search_box.returnPressed.connect(self.onSearch)
        self.user_profile_btn.clicked.connect(self.showUserProfile)
        self.setting_btn.clicked.connect(self.showSetting)
        self.updateButtons()

    def fillSpace(self) -> None:
        if self.search_results_widget.isVisible() and len(self.search_result) % 9 != 0:
            grid_layout: QGridLayout = self.search_results_widget.findChild(QGridLayout)
        elif (
            not self.search_results_widget.isVisible() and len(self.pages_data) % 9 != 0
        ):
            grid_layout: QGridLayout = self.stacked_widget.findChild(QGridLayout)
        if grid_layout.count() % 9 != 0:
            for i in range(9 - grid_layout.count() % 9):
                grid_layout.addWidget(ItemWidget(self.null_cover_path, "", self), i, 0)
        else:
            pass

    def onSearch(self) -> None:
        keyword = self.search_box.text()
        # [(video_id: int, video_title: str, video_tags: str, video_desc: str), ...]
        if len(keyword) > 0:
            self.search_result = self.searchdb.search(keyword)
            logger.debug(f"Search keyword: {keyword} result: {self.search_result}")
            if len(self.search_result) == 0:
                dialog = Dialog()
                logger.info(f"Keyword [{keyword}] No search result")
                dialog.standard(_("错误"), _(f"没有找到相关视频"))
            else:
                # Convert search results and open in new window
                converted_results = self.converter(self.search_result)
                search_window = SearchWindow(converted_results, keyword, self.app)
                search_window.show()
                
                # Clear search box
                self.search_box.clear()

    @TimeKeeper.timer
    def getVideos(self, page_size: int = 9) -> list:
        results = self.videodb.query_videos_all()
        videos = [
            {"cover": result[2], "title": result[1], "vid": result[0]}
            for result in results
        ]
        # Split videos into pages
        pages = [videos[i : i + page_size] for i in range(0, len(videos), page_size)]
        return pages

    def appendPage(self, *items_data: list) -> None:
        """deprecated function"""
        for data in items_data:
            self.pages_data.append(data)
            self.loadPage(len(self.pages_data) - 1)
            self.updateButtons()

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(self.bg_image_path)
        # pixmap = QPixmap(":/images/background.png")
        painter.drawPixmap(self.rect(), pixmap)

    def showUserProfile(self) -> None:
        if self.__token:  # if user logged in
            self.profileWindow = ProfileWindow(self.__token)
            self.profileWindow.show()
        else:
            raise NoLoginError

    def showSetting(self) -> None:
        self.settingWindow = SettingWindow(self.app)
        self.settingWindow.show()
        # from app.modules.ui_new_setting import NewSettingWindow

        # self.settingWindow = NewSettingWindow(self.app)
        # self.settingWindow.show()

    def jump2Page(self) -> None:
        loader: function = self.__getCurrentLoader()
        current_page_no = self.__getCurrentPageNo()
        page_data = self.__getCurrentData()
        try:
            page_num = int(self.page_number.text())
            if page_num < 1 or page_num > len(page_data):
                return
            target_page = page_num - 1
            
            # Update current page variable
            if self.content_container.currentIndex() == 1:
                self.search_box_current_page = target_page
            else:
                self.current_page = target_page
                
            loader(target_page)
            self.updateButtons()
        except ValueError:
            # Invalid input, ignore
            pass

    def __getCurrentBoxObj(self) -> QStackedWidget:
        return (
            self.search_results_widget
            if self.content_container.currentIndex() == 1
            else self.stacked_widget
        )

    def converter(self, data: list) -> list:
        # (1,'《崩坏：星穹铁道》遐蝶角色PV——「墓志铭」','崩坏：星穹铁道,崩坏星穹铁道,角色PV,米哈游,miHoYo', 'Honkai Star Rail')
        """
        Converts a list of data into a FSVF (FairSearch Video Format) list.
        Args:
            data (list): A list of tuples or lists where each element contains
                         at least 4 items. The expected structure of each
                         element is (vid, title, tags, desc, cover: Optional). Usually generated by search().
        Returns:
            list: A list of dict where each dictionary contains the keys:
                  - "vid": The vid of video (usually data[i][0])
                  - "title": The title of the video
                  - "cover": The cover path of the video
        """
        return [
            {
                "cover": result[4] if len(result) > 4 else Default.DEFAULT_COVER,
                "title": result[1],
                "vid": result[0],
            }
            for result in data
        ]

    def __getCurrentPageNo(self) -> int:
        return (
            self.search_box_current_page
            if self.content_container.currentIndex() == 1
            else self.current_page
        )

    def __getCurrentLoader(self) -> Callable:
        return (
            self.loadSearchPage
            if self.content_container.currentIndex() == 1
            else self.loadPage
        )

    def __getCurrentData(self) -> list:
        return (
            self.search_result
            if self.content_container.currentIndex() == 1
            else self.pages_data
        )

    # def loadSearchPage(self, page_index: int) -> None:
    #     if page_index not in self.search_cache:
    #         if 0 <= page_index < len(self.search_result):
    #             # import pdb;pdb.set_trace()
    #             logger.debug(self.search_result[page_index])
    #             page = PageWidget([self.search_result[page_index]])
    #             self.search_results_widget.addWidget(page)
    #             logger.debug(f"Page {page_index, self.search_cache} loaded")
    #             if page_index not in self.search_cache:
    #                 self.search_cache.append(page)
    #     self.search_results_widget.setCurrentIndex(page_index)

    def loadSearchPage(self, page_index: int) -> None:
        # Initialize search cache if needed
        if not hasattr(self, 'search_cache'):
            self.search_cache = {}
        
        # Check if page is already cached
        if page_index not in self.search_cache:
            if 0 <= page_index < len(self.search_result):
                # Create page with single search result item
                page = PageWidget([self.search_result[page_index]])
                self.search_results_widget.addWidget(page)
                self.search_cache[page_index] = self.search_results_widget.count() - 1
                logger.debug(f"Search page {page_index} loaded")
        
        # Set current page
        if page_index in self.search_cache:
            self.search_results_widget.setCurrentIndex(self.search_cache[page_index])
        
        # Update current page number
        self.search_box_current_page = page_index

    # Lazy loading
    def loadPage(self, page_index: int) -> None:
        if page_index not in self.page_cache:
            if 0 <= page_index < len(self.pages_data):
                logger.debug(self.pages_data[page_index])
                page = PageWidget(self.pages_data[page_index])
                self.stacked_widget.addWidget(page)
                self.page_cache[page_index] = page  # cecha page
        self.stacked_widget.setCurrentIndex(page_index)

    def showPrevPage(self) -> None:
        # import pdb;pdb.set_trace()
        loader: function = self.__getCurrentLoader()
        current_page_no = self.__getCurrentPageNo()
        if current_page_no > 0:
            current_page_no -= 1
            
            # Update current page variable
            if self.content_container.currentIndex() == 1:
                self.search_box_current_page = current_page_no
            else:
                self.current_page = current_page_no
                
            self.page_number.setText(str(current_page_no + 1))
            # self.loadPage(current_page_no)  # load prev page
            loader(current_page_no)
            self.updateButtons()

    def showNextPage(self) -> None:
        # import pdb
        # pdb.set_trace()
        current_page_no = self.__getCurrentPageNo()
        loader: function = self.__getCurrentLoader()
        page_data = self.__getCurrentData()
        if current_page_no < len(page_data) - 1:
            current_page_no += 1
            
            # Update current page variable
            if self.content_container.currentIndex() == 1:
                self.search_box_current_page = current_page_no
            else:
                self.current_page = current_page_no
                
            self.page_number.setText(str(current_page_no + 1))
            # self.loadPage(current_page_no)
            loader(current_page_no)
            self.updateButtons()

    def updateButtons(self) -> None:
        current_page_no = self.__getCurrentPageNo()
        page_data = self.__getCurrentData()
        self.prev_button.setEnabled(current_page_no > 0)
        self.next_button.setEnabled(current_page_no < len(page_data) - 1)

    