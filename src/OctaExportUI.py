# Form implementation generated from reading ui file './octaexportui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OctaExportUi(object):
    def setupUi(self, OctaExportUi):
        OctaExportUi.setObjectName("OctaExportUi")
        OctaExportUi.resize(864, 616)
        self.centralwidget = QtWidgets.QWidget(parent=OctaExportUi)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(parent=self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 131, 271))
        self.treeView.setObjectName("treeView")
        self.treeView_2 = QtWidgets.QTreeView(parent=self.centralwidget)
        self.treeView_2.setGeometry(QtCore.QRect(0, 270, 131, 281))
        self.treeView_2.setObjectName("treeView_2")
        self.listView = QtWidgets.QListView(parent=self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(130, 0, 661, 271))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 530, 80, 22))
        self.pushButton.setObjectName("pushButton")
        self.listView_2 = QtWidgets.QListView(parent=self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(130, 290, 661, 241))
        self.listView_2.setObjectName("listView_2")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 270, 80, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 530, 80, 22))
        self.pushButton_3.setObjectName("pushButton_3")
        OctaExportUi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=OctaExportUi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 864, 19))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(parent=self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuMode = QtWidgets.QMenu(parent=self.menubar)
        self.menuMode.setObjectName("menuMode")
        OctaExportUi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=OctaExportUi)
        self.statusbar.setObjectName("statusbar")
        OctaExportUi.setStatusBar(self.statusbar)
        self.actionOptions = QtGui.QAction(parent=OctaExportUi)
        self.actionOptions.setObjectName("actionOptions")
        self.actionExit = QtGui.QAction(parent=OctaExportUi)
        self.actionExit.setObjectName("actionExit")
        self.actionFLAC_to_MP3 = QtGui.QAction(parent=OctaExportUi)
        self.actionFLAC_to_MP3.setObjectName("actionFLAC_to_MP3")
        self.action44_1khz_WAV = QtGui.QAction(parent=OctaExportUi)
        self.action44_1khz_WAV.setObjectName("action44_1khz_WAV")
        self.actionFLAC_to_MP3_2 = QtGui.QAction(parent=OctaExportUi)
        self.actionFLAC_to_MP3_2.setObjectName("actionFLAC_to_MP3_2")
        self.action44_1kHz_WAV = QtGui.QAction(parent=OctaExportUi)
        self.action44_1kHz_WAV.setObjectName("action44_1kHz_WAV")
        self.menuMenu.addSeparator()
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menuMode.addAction(self.actionFLAC_to_MP3_2)
        self.menuMode.addAction(self.action44_1kHz_WAV)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())

        self.retranslateUi(OctaExportUi)
        QtCore.QMetaObject.connectSlotsByName(OctaExportUi)

    def retranslateUi(self, OctaExportUi):
        _translate = QtCore.QCoreApplication.translate
        OctaExportUi.setWindowTitle(_translate("OctaExportUi", "OctaExport"))
        self.pushButton.setText(_translate("OctaExportUi", "Convert"))
        self.pushButton_2.setText(_translate("OctaExportUi", "Add"))
        self.pushButton_3.setText(_translate("OctaExportUi", "Remove"))
        self.menuMenu.setTitle(_translate("OctaExportUi", "Menu"))
        self.menuMode.setTitle(_translate("OctaExportUi", "Mode"))
        self.actionOptions.setText(_translate("OctaExportUi", "Options"))
        self.actionExit.setText(_translate("OctaExportUi", "Exit"))
        self.actionFLAC_to_MP3.setText(_translate("OctaExportUi", "FLAC to MP3"))
        self.action44_1khz_WAV.setText(_translate("OctaExportUi", "44.1khz WAV"))
        self.actionFLAC_to_MP3_2.setText(_translate("OctaExportUi", "FLAC to MP3"))
        self.action44_1kHz_WAV.setText(_translate("OctaExportUi", "44.1kHz WAV"))
