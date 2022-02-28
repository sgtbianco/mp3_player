import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from mp3_player import *
from pygame import *
import pathlib


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addButton.clicked.connect(self.add_song)
        self.ui.removeButton.clicked.connect(self.remove_song)
        self.ui.playButton.clicked.connect(self.play_song)
        self.ui.pauseButton.clicked.connect(self.pause_song)
        self.show()
        mixer.init()
        self.song_list = {}
        self.current_song = ""

    def add_song(self):
        file_filter = "mp3 file (*.mp3)"
        file = QFileDialog.getOpenFileName(self, 'Choose file', filter=file_filter)
        path = pathlib.PurePath(file[0])
        if not len(self.ui.playlist.findItems(path.name, QtCore.Qt.MatchExactly)) > 0:
            self.song_list[path.name] = path
            self.ui.playlist.addItem(path.name)

    def remove_song(self):
        if self.ui.playlist.currentItem():
            del self.song_list[self.ui.playlist.currentItem().text()]
            self.ui.playlist.takeItem(self.ui.playlist.currentRow())

    def play_song(self):
        if self.ui.playlist.currentItem():
            current_song = self.song_list[self.ui.playlist.currentItem().text()]  # make sure value not key
            mixer.music.load(current_song)
            mixer.music.play()

    def pause_song(self):
        if mixer.music.get_busy():
            mixer.music.pause()
            self.ui.pauseButton.setText("Unpause")
        else:
            mixer.music.unpause()
            self.ui.pauseButton.setText("Pause")


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())


