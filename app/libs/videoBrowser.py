from app.__init__ import *
from app.modules.Ui_videoBroswer import Ui_VideoBroswer
from app.database.queries import Database
import vlc

db = Database
class VideoBrowser(QWidget, Ui_VideoBroswer):
    def __init__(self, vid: int, *args, **kwargs) -> None:
        super().__init__()
        self.setupUi(self)
        self.title = db.videodb.query_title_by_vid(vid)
        self.vid = vid
        self.is_paused = False
    
        # Create vlc media player
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        
        self.setWindowTitle(self.title)
        self.video.setAutoFillBackground(True)
        
        self.play.clicked.connect(self.onPlay)
        self.like.clicked.connect(self.onLike)
        self.coin.clicked.connect(self.onCoin)
        self.favorite.clicked.connect(self.onFavorite)
        self.positionslider.sliderMoved.connect(self.setPosition)
        self.volume.valueChanged.connect(self.setVolume)
        
    def changeBackground(self, path: str, widget: str):
        return (u"%s {\n"
        "	background-image: url(%s);\n"
        "    background-position: centre centre;\n"
        "    background-repeat: no-repeat;\n"
        "	background-color:transparent;\n"
        "}" % (widget, path))
    
    def onPlay(self):
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            
            # self.play.setStyleSheet()
            self.is_paused = True
            self.timer.stop()
        else:
            if self.mediaplayer.play() == -1:
                self.open_file()
                return
            self.mediaplayer.play()
            self.playbutton.setText("Pause")
            self.timer.start()
            self.is_paused = False
    
    def onLike(self):
        ...
        
    def onCoin(self):
        ...

    def onFavorite(self):
        ...
        
    def updateUi(self):
        media_pos = int(self.mediaplayer.get_position() * 1000)
        self.positionslider.setValue(media_pos)

        if not self.mediaplayer.is_playing():
            self.timer.stop()
            if not self.is_paused:
                self.stop()
        
    def setPosition(self, position):
        pos = position / 1000.0
        self.mediaplayer.set_position(pos)
    
    def setVolume(self, volume):
        self.mediaplayer.audio_set_volume(volume)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(":/images/images/background.png")
        painter.drawPixmap(self.rect(), pixmap)