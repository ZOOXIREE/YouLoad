import sys

from download import *

from PyQt5 import uic
from PyQt5.QtWidgets import *

EXPANSION = ["               720p",
             "               360p",
             "               144p"
             ]
index = 0


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        uic.loadUi('beta-youtube-download.ui', self)

        self.hd = EXPANSION[0]

        self.pushButton.clicked.connect(self.clickOnDownload)

        self.comboBox.addItems(EXPANSION)

        self.comboBox.activated[str].connect(self.onActivated)

    def clickOnDownload(self):
        hd = self.hd.split()
        url = self.lineEdit.text()
        youtube = YouTube(url)

        video_streams = youtube.streams.filter(progressive=True, resolution=hd)

        if video_streams:
            video_stream = video_streams[0]
            video_duration = youtube.length
            video_size = video_stream.filesize
            video_size_mb = round(video_size / (1024 * 1024))

            self.lineEdit_3.setText(str(" " * 15 + str(video_duration) + " с"))
            self.lineEdit_4.setText(str(" " * 15 + str(video_size_mb) + " MB"))

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")

        if folder_path:
            main(url, hd, folder_path)
        else:
            pass

    def onActivated(self, text):
        self.hd = text
        index = EXPANSION.index(text)
        print(self.hd)
        print(index)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
