import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QTreeView, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon, QFileSystemModel
from PyQt6.QtCore import QDir, QStringListModel
from OctaExport import Ui_OctaExport
# TODO:
# Show items to convert in bottom list
# Set ffmpeg command in Options
# Make exit button work
# Convert
# Make sure it works on Windows / convert

class MainWindow(QMainWindow, Ui_OctaExport):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.directoryModel = QFileSystemModel()
        self.directoryModel.setRootPath(QDir.rootPath())
        self.destinationModel = QFileSystemModel()
        self.destinationModel.setRootPath(QDir.rootPath())
        self.files_to_convert = []
        self.list_focus = ""
        self.list_focus_2 = ""

        self.path = QDir.rootPath()

        self.fileModel = QFileSystemModel()
        self.listModel = QStringListModel()
        self.listModel.setStringList(self.files_to_convert)

        self.treeView.setModel(self.directoryModel)
        self.treeView_2.setModel(self.destinationModel)
        self.treeView.setRootIndex(self.directoryModel.index(self.path))
        self.treeView_2.setRootIndex(self.destinationModel.index(self.path))

        self.treeView.clicked.connect(self.on_clicked)
        self.treeView_2.clicked.connect(self.on_clicked_destination)
        self.listView.clicked.connect(self.on_clicked_list)
        self.listView_2.clicked.connect(self.on_clicked_list_2)

        self.listView.setModel(self.fileModel)
        self.listView_2.setModel(self.listModel)

        self.pushButton.clicked.connect(self.convert)
        self.pushButton_2.clicked.connect(self.add_file)
        self.pushButton_3.clicked.connect(self.remove_file)


    def add_file(self):
        if os.path.isdir(self.list_focus):
            for item in os.listdir(self.list_focus):
                print(item)
                if ".wav" in item:
                    print("is a wav file, adding")
                    self.files_to_convert.append(self.list_focus + f"/{item}")
        else:
            if ".wav" in self.list_focus:
                self.files_to_convert.append(self.list_focus)
        print(self.files_to_convert)

    def remove_file(self):
        self.files_to_convert.remove(self.list_2_focus)
        print(self.files_to_convert)

    def on_clicked_destination(self, index):
        self.destination = self.destinationModel.fileInfo(index).absoluteFilePath()

    def on_clicked(self, index):
        self.path = self.directoryModel.fileInfo(index).absoluteFilePath()
        self.listView.setRootIndex(self.fileModel.setRootPath(self.path))
        if self.list_focus == "":
            self.list_focus = self.path

    def on_clicked_list(self, index):
        self.list_focus = self.directoryModel.fileInfo(index).absoluteFilePath()

    def on_clicked_list_2(self, index):
        self.list_2_focus = self.directoryModel.fileInfo(index).absoluteFilePath()

    def convert(self):
        for item in self.files_to_convert:
            print(f"Converting {item}!")
            # self.ffmpeg_command
            self.files_to_convert.remove(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
