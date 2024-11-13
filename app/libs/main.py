from app.libs.videoBrowser import VideoBrowser
# to avoid circular import
def onClickVideos(vid: int) -> None:
    videosBrower = VideoBrowser(vid)
    videosBrower.show()
    # logger.debug(f"onClickVideos: {vid}")

from app.modules.Ui_main import Ui_MainWindow, ItemWidget, PageWidget
from app.libs.profile import ProfileWindow
from app.libs.expection import NoLoginError
from app.database.queries import Database
from app.utils.time import TimeKeeper
from app.__init__ import *
# import pdb
db = Database
video_browser = VideoBrowser()



class MainWindow(
    QWidget,
    Ui_MainWindow,
):
    def __init__(self, token: str) -> None:
        super().__init__()
        self.__token = token
        self.bg_image_path = ":/images/images/background.png"  # using QRC path
        self.def_cover_path = ":/covers/covers/default.png"  # using QRC path
        # self.pages_data = [
        #     [
        #         {"cover": self.def_cover_path, "title": "Item 1"},
        #         {"cover": self.def_cover_path, "title": "Item 2"},
        #         {"cover": self.def_cover_path, "title": "Item 3"},
        #         {"cover": self.def_cover_path, "title": "Item 4"},
        #         {"cover": self.def_cover_path, "title": "Item 5"},
        #         {"cover": self.def_cover_path, "title": "Item 6"},
        #     ],
        # ]
        self.pages_data = self.get_videos()
        logger.debug(f"pages_data: {self.pages_data}, type: {type(self.pages_data)}")
        # pdb.set_trace()
        self.setupUi(self, self.pages_data)

        # bind button click events
        self.prev_button.clicked.connect(self.show_prev_page)
        self.next_button.clicked.connect(self.show_next_page)
        self.page_number.editingFinished.connect(self.jump_to_page)
        self.user_profile_btn.clicked.connect(self.show_user_profile)
        self.update_buttons()
        
    @TimeKeeper.timer
    def get_videos(
        self, page: int = 0, page_size: int = 6
    ) -> list:  # arg no implemented
        # TODO: get videos partly
        results = db.videodb.query_videos_all()
        # construct and return a list of dictionaries
        videos = [[{"cover": result[2], "title": result[1], "vid": result[0]} for result in results]]
        logger.debug(f"videos: {videos}")
        return videos

    def append_page(self, *items_data: list) -> None:
        for data in items_data:
            self.pages_data.append(data)
            self.load_page(len(self.pages_data) - 1)
            self.update_buttons()

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(f"{self.bg_image_path}")
        # pixmap = QPixmap(":/images/background.png")
        painter.drawPixmap(self.rect(), pixmap)

    def jump_to_page(self) -> None:
        page_num = int(self.page_number.text())
        if page_num < 0 or page_num < len(self.pages_data) - 1:
            return
        self.current_page = page_num - 1
        self.load_page(self.current_page)
        self.update_buttons()

    def show_user_profile(self) -> None:
        if self.__token:  # if user logged in
            self.profileWindow = ProfileWindow(self.__token)
            self.profileWindow.show()
        else:
            raise NoLoginError

    # Lazy loading
    def load_page(self, page_index: int) -> None:
        if page_index not in self.page_cache:
            if 0 <= page_index < len(self.pages_data):
                page = PageWidget(self.pages_data[page_index])
                self.stacked_widget.addWidget(page)
                self.page_cache[page_index] = page  # cecha page
        self.stacked_widget.setCurrentIndex(page_index)

    def show_prev_page(self) -> None:
        if self.current_page > 0:
            self.current_page -= 1
            self.page_number.setText(str(self.current_page + 1))
            self.load_page(self.current_page)  # load prev page
            self.update_buttons()

    def show_next_page(self) -> None:
        if self.current_page < len(self.pages_data) - 1:
            self.current_page += 1
            self.page_number.setText(str(self.current_page + 1))
            self.load_page(self.current_page)  # load next page
            self.update_buttons()

    def update_buttons(self) -> None:
        self.prev_button.setEnabled(self.current_page > 0)
        self.next_button.setEnabled(self.current_page < len(self.pages_data) - 1)
