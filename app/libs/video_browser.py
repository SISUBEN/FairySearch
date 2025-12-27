import vlc
from PySide6.QtCore import QTimer
from PySide6.QtMultimedia import QMediaPlayer
from app import logger, QWidget, QPainter, QPixmap
from app.modules.ui_video_browser import Ui_VideoBrowser
from app.database.videos import Videodb
from app.assets.resource_manager import ResourceManager
from app.libs.dialog import Dialog
from app.libs.exception import VideoNotFoundError
from app.i18n import _

class VideoBrowser(QWidget, Ui_VideoBrowser):
    def __init__(self, vid: int, *args, **kwargs) -> None:
        super().__init__()
        self.res_manager = ResourceManager()
        self.dialog = Dialog()
        self.videodb = Videodb()
        
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.updateUi)
        self.closeEvent = self.closeEventWrapper

        self.is_liked = False
        self.is_favorited = False
        self.is_coined = False
        self.__title = self.videodb.query_title_by_vid(vid)[0][0] or None
        logger.debug(self.__title)
        self.__desc = self.videodb.query_desc_by_vid(vid)[0][0] or None
        logger.debug(
            f"Video Info:\n title: {self.__title}\n desc :{self.__desc}\n vid: {vid}"
        )
        if self.__title is None or self.__desc is None:
            self.dialog.standard(_("错误"), _("无法找到该视频"))
            raise VideoNotFoundError

        self.vid = vid
        self.is_paused = False

        # Create vlc media player
        self.instance = vlc.Instance()
        self.media = None
        self.media_player = self.instance.media_player_new()
        
        # Attach event manager to listen for playback end
        self.events = self.media_player.event_manager()
        self.events.event_attach(vlc.EventType.MediaPlayerEndReached, self.on_playback_finished)

        # logger.debug(f"title: {self.__title}")
        self.setWindowTitle(self.__title)
        self.video_frame.setAutoFillBackground(True)
        self.position_slider.setToolTip("Position")
        self.position_slider.setMaximum(1000)

        try:
            self.filename = self.res_manager.getVideoPath(vid=vid)
            if self.filename is None:
                raise VideoNotFoundError
        except TypeError:
            self.dialog.standard(_("错误"), _("vid无效"))
        self.media = self.instance.media_new(self.filename)
        try:
            self.media_player.set_media(self.media)
            self.media.parse()
            self.setWindowTitle(
                self.__title if len(self.__title) < 12 else self.__title[:12] + "..."
            )
            self.media_player.set_hwnd(int(self.video_frame.winId()))
            logger.debug(f"video_frame.winId(): {self.video_frame.winId()}")
            self.onPlay()
        except Exception as e:
            logger.debug(f"Error: {e}")
            self.dialog.standard(_("错误"), _("视频播放失败"))

        self.title.setText(self.__title)
        self.describe.setText(self.__desc)
        self.play_button.clicked.connect(self.onPlay)
        self.like.clicked.connect(self.onLike)
        self.coin.clicked.connect(self.onCoin)
        self.favorite.clicked.connect(self.onFavorite)
        self.position_slider.sliderMoved.connect(self.setPosition)
        self.volume_slider.valueChanged.connect(self.setVolume)

        self.volume_slider.setValue(50)
        self.media_player.audio_set_volume(50)

    def on_playback_finished(self, event):
        """Callback when video finishes playing"""
        logger.debug("Playback finished, submitting status...")
        self.submitStatus()
        # Optional: Reset UI state if needed, though updateUi handles some of it
        # self.timer.stop() 

    def changeBackground(self, path: str, widget: str):
        return (
            "%s {\n"
            "	background-image: url(%s);\n"
            "    background-position: centre centre;\n"
            "    background-repeat: no-repeat;\n"
            "	background-color:transparent;\n"
            "}" % (widget, path)
        )

    def onPlay(self):
        if self.media_player.is_playing():
            self.media_player.pause()
            self.play_button.setStyleSheet(
                self.changeBackground(":/icons/icons/play.svg", "QPushButton")
            )

            self.is_paused = True
            self.timer.stop()
            logger.debug("video paused")
        else:
            if self.media_player.play() == -1:
                return
            self.media_player.play()
            self.play_button.setStyleSheet(
                self.changeBackground(":/icons/icons/pause.svg", "QPushButton")
            )
            self.timer.start()
            self.is_paused = False
            logger.debug("video playing")

    def onLike(self):
        if not self.is_liked:
            self.is_liked = True
            self.like.setStyleSheet(
                self.changeBackground(":/icons/icons/liked.png", "QPushButton")
            )
            logger.debug("video liked")
        else:
            self.is_liked = False
            self.like.setStyleSheet(
                self.changeBackground(":/icons/icons/like.png", "QPushButton")
            )
            logger.debug("video unliked")

    def onCoin(self):
        if not self.is_coined:
            self.is_coined = True
            self.coin.setStyleSheet(
                self.changeBackground(":/icons/icons/coined.png", "QPushButton")
            )
            logger.debug("video coined")
        else:
            self.is_coined = False
            self.coin.setStyleSheet(
                self.changeBackground(":/icons/icons/coin.png", "QPushButton")
            )
            logger.debug("video uncoined")

    def onFavorite(self):
        if not self.is_favorited:
            self.is_favorited = True
            self.favorite.setStyleSheet(
                self.changeBackground(":/icons/icons/favorited.png", "QPushButton")
            )
            logger.debug("video favorited")
        else:
            self.is_favorited = False
            self.favorite.setStyleSheet(
                self.changeBackground(":/icons/icons/favorite.png", "QPushButton")
            )
            logger.debug("video unfavorited")

    def stop(self):
        self.media_player.stop()
        self.play_button.setText("Play")

    def updateUi(self):
        media_pos = int(self.media_player.get_position() * 1000)
        self.position_slider.setValue(media_pos)

        if not self.media_player.is_playing():
            self.timer.stop()
            if not self.is_paused:
                self.stop()

    def setPosition(self, position):
        pos = position / 1000.0
        self.media_player.set_position(pos)

    def setVolume(self, volume):
        self.media_player.audio_set_volume(volume)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/background.png")
        painter.drawPixmap(self.rect(), pixmap)

    def closeEvent(self, event):
        self.submitStatus()
        self.media_player.stop()
        self.timer.stop()
        self.media_player.set_media(QMediaPlayer.Media())
        event.accept()

    def closeEventWrapper(self, event):
        self.media_player.stop()
        self.timer.stop()
        event.accept()

    # def resizeEvent(self, event):
    # Update position_slider size and position
    # self.position_slider.setGeometry(40, self.height() - 100, self.width() - 80, 50)

    def submitStatus(self):
        logger.debug("submit status")
        self.videodb.update_interaction(
            self.vid, self.is_liked, self.is_coined, self.is_favorited
        )

    def __del__(self):
        try:
            self.media_player.stop()
            self.timer.stop()
        except RuntimeError:
            logger.warning("object PySide6.QtCore.QTimer already deleted")
        except (ImportError, AttributeError):
            logger.warning("VLC media player already deleted")
