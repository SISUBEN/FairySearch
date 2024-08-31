import sys
from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QFileDialog, QVBoxLayout
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

class VideoPlayer(QWidget):
    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)
        self.media_player = QMediaPlayer(self)
        self.video_widget = QVideoWidget(self)
        self.audio_output = QAudioOutput(self)

        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setVideoOutput(self.video_widget)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.video_widget)
        self.setLayout(self.layout)

        self.video_widget.setMinimumSize(160, 90)

    def load_video(self, file_path):
        self.media_player.setSource(QUrl.fromLocalFile(file_path))
        self.media_player.play()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)
        self.video_players = []
        for i in range(4):
            row = []
            for j in range(4):
                player = VideoPlayer(self)
                self.grid_layout.addWidget(player, i, j)
                row.append(player)
            self.video_players.append(row)

        self.load_button = QPushButton("Load Videos")
        self.load_button.clicked.connect(self.load_videos)
        self.grid_layout.addWidget(self.load_button, 4, 0, 1, 4, alignment=Qt.AlignCenter)

    def load_videos(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Videos (*.mp4 *.avi *.mkv)")

        if file_dialog.exec():
            file_paths = file_dialog.selectedFiles()
            index = 0
            for i in range(4):
                for j in range(4):
                    if index < len(file_paths):
                        self.video_players[i][j].load_video(file_paths[index])
                        index += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())