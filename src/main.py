import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QTreeView, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon, QFileSystemModel
from PyQt6.QtCore import QDir, QStringListModel
from MainWindow import Ui_MainWindow
# TODO:
# Add / remove items from list
#   if folder: add all subitems
# Set ffmpeg command in Options
# Convert

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.directoryModel = QFileSystemModel()
        self.directoryModel.setRootPath(QDir.rootPath())
        self.destinationModel = QFileSystemModel()
        self.destinationModel.setRootPath(QDir.rootPath())
        self.files_to_convert = []

        path = QDir.rootPath()

        self.fileModel = QFileSystemModel()
        self.listModel = QStringListModel()
        self.listModel.setStringList(self.files_to_convert)

        self.treeView.setModel(self.directoryModel)
        self.treeView_2.setModel(self.destinationModel)
        self.treeView.setRootIndex(self.directoryModel.index(path))
        self.treeView_2.setRootIndex(self.destinationModel.index(path))

        self.treeView.clicked.connect(self.on_clicked)

        self.listView_2.setModel(self.fileModel)
        self.listView.setModel(self.listModel)

        #self.pushButton_2.clicked.connect(self.add_file(self.fileModel.index(path)))
        self.pushButton.clicked.connect(self.convert)


    def add_file(self, path):
        self.files_to_convert.append(path)

    def on_clicked(self, index):
        path = self.directoryModel.fileInfo(index).absoluteFilePath()
        self.listView_2.setRootIndex(self.fileModel.setRootPath(path))

    def convert(self):
        print("Converting!")
        for item in self.files_to_convert:
            # self.ffmpeg_command
            self.files_to_convert(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
