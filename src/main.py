import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QTreeView, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon, QFileSystemModel
from PyQt6.QtCore import QDir
from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.directoryModel = QFileSystemModel()
        self.directoryModel.setRootPath(QDir.rootPath())
        self.destinationModel = QFileSystemModel()
        self.destinationModel.setRootPath(QDir.rootPath())

        path = QDir.rootPath()

        self.fileModel = QFileSystemModel()

        self.treeView.setModel(self.directoryModel)
        self.treeView_2.setModel(self.destinationModel)
        self.treeView.setRootIndex(self.directoryModel.index(path))

        self.treeView.clicked.connect(self.on_clicked)

        self.listView_2.setModel(self.fileModel)

    def on_clicked(self, index):
        path = self.directoryModel.fileInfo(index).absoluteFilePath()
        self.listView_2.setRootIndex(self.fileModel.setRootPath(path))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
