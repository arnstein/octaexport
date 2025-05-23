import sys
import os
import time
from subprocess import Popen, PIPE, STDOUT
from pathlib import Path
from PyQt6.QtWidgets import QMainWindow, QApplication, QTreeView, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon, QFileSystemModel, QStandardItemModel, QStandardItem
from PyQt6.QtCore import QDir, QStringListModel
from OctaExportUI import Ui_OctaExportUi
# TODO:
# Fix removing items from bottom list
# Popup window when conversion is done
# Pyinstaller package with ffmpeg

class MainWindow(QMainWindow, Ui_OctaExportUi):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.directoryModel = QFileSystemModel()
        self.directoryModel.setRootPath(QDir.rootPath())
        self.destinationModel = QFileSystemModel()
        self.destinationModel.setRootPath(QDir.rootPath())
        self.files_to_convert = []
        self.directory_focus = ""
        self.target_list_focus = ""
        self.mode = "octa"

        self.path = QDir.rootPath()

        self.fileModel = QFileSystemModel()
        self.listModel = QStandardItemModel()

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

        self.pushButton.clicked.connect(self.convert_all)
        self.pushButton_2.clicked.connect(self.add_file)
        self.pushButton_3.clicked.connect(self.remove_file)
        self.actionExit.triggered.connect(self.on_clicked_exit)
        self.action44_1kHz_WAV.triggered.connect(self.on_clicked_octa)
        self.actionFLAC_to_MP3_2.triggered.connect(self.on_clicked_flac)


    def add_file(self):
        self.files_to_convert.append(self.directory_focus)
        self.listView_2.model().appendRow(QStandardItem(str(self.directory_focus)))
        print(self.files_to_convert)

    def remove_file(self):
        item = self.listView_2.model().itemFromIndex(self.target_list_focus).text()
        self.files_to_convert.remove(item)
        self.listView_2.setModel(self.listModel)
        for item in self.files_to_convert:
            self.listView_2.model().appendRow(QStandardItem(str(item)))
        self.listView_2.show()

    def on_clicked_destination(self, index):
        self.destination = self.destinationModel.fileInfo(index).absoluteFilePath()

    def on_clicked_exit(self):
        os.sys.exit()

    def on_clicked_octa(self):
        self.mode = "octa"

    def on_clicked_flac(self):
        self.mode = "flac"

    def on_clicked(self, index):
        self.path = self.directoryModel.fileInfo(index).absoluteFilePath()
        self.listView.setRootIndex(self.fileModel.setRootPath(self.path))
        if self.directory_focus == "":
            self.directory_focus = self.path

    def on_clicked_list(self, index):
        self.directory_focus = self.directoryModel.fileInfo(index).absoluteFilePath()

    def on_clicked_list_2(self, index):
        self.target_list_focus = index

    def convert_all(self):
        for item in self.files_to_convert:
            print(f"Iterating {item}", item)
            print(self.files_to_convert)
            if os.path.isdir(item):
                folder = Path(item)
                destination_folder = Path(self.destination)
                destination = Path.joinpath(destination_folder, folder.name)
                os.mkdir(destination)

                for f in os.listdir(item):
                    file = Path.joinpath(folder, f)
                    self.convert(file, destination)
            else:
                destination = Path(self.destination)
                source = Path(item)
                self.convert(source, destination)

        self.files_to_convert = []
        print("Conversion done!")


    def convert(self, source_path, destination_path):
        file_name = source_path.name
        output_file = Path.joinpath(destination_path, file_name)
        p = ""
        match self.mode:
            case "octa":
                if ".wav" in str(file_name):
                    print(f"Converting {file_name}")
                    p = Popen([
                        'ffmpeg',
                        '-i', source_path,
                        '-acodec', 'pcm_s16le',
                        '-ar', '44100',
                        output_file
                    ], stdout=PIPE, stdin=PIPE, stderr=PIPE)
            case "flac":
                if ".flac" in str(file_name):
                    print(f"Converting {file_name}")
                    p = Popen([
                        'ffmpeg',
                        '-i', source_path,
                        '-ab', '320k',
                        '-map_metadata', '0',
                        str(output_file).replace("flac", "mp3")
                    ], stdout=PIPE, stdin=PIPE, stderr=PIPE)

        return
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
