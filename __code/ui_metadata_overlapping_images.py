# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/j35/git/IPTS/python_notebooks/ui/ui_metadata_overlapping_images.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1147, 741)
        MainWindow.setMinimumSize(QtCore.QSize(0, 300))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pyqtgraph_widget = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pyqtgraph_widget.sizePolicy().hasHeightForWidth())
        self.pyqtgraph_widget.setSizePolicy(sizePolicy)
        self.pyqtgraph_widget.setObjectName("pyqtgraph_widget")
        self.horizontalLayout_7.addWidget(self.pyqtgraph_widget)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.previous_image_button = QtWidgets.QPushButton(self.widget)
        self.previous_image_button.setEnabled(False)
        self.previous_image_button.setObjectName("previous_image_button")
        self.horizontalLayout_8.addWidget(self.previous_image_button)
        self.file_slider = QtWidgets.QSlider(self.widget)
        self.file_slider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.file_slider.setOrientation(QtCore.Qt.Horizontal)
        self.file_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.file_slider.setObjectName("file_slider")
        self.horizontalLayout_8.addWidget(self.file_slider)
        self.image_slider_value = QtWidgets.QLabel(self.widget)
        self.image_slider_value.setMinimumSize(QtCore.QSize(30, 0))
        self.image_slider_value.setMaximumSize(QtCore.QSize(30, 16777215))
        self.image_slider_value.setBaseSize(QtCore.QSize(50, 0))
        self.image_slider_value.setObjectName("image_slider_value")
        self.horizontalLayout_8.addWidget(self.image_slider_value)
        self.next_image_button = QtWidgets.QPushButton(self.widget)
        self.next_image_button.setObjectName("next_image_button")
        self.horizontalLayout_8.addWidget(self.next_image_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.widget1)
        self.checkBox.setMaximumSize(QtCore.QSize(400, 16777215))
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_4.addWidget(self.checkBox)
        self.groupBox = QtWidgets.QGroupBox(self.widget1)
        self.groupBox.setEnabled(False)
        self.groupBox.setMinimumSize(QtCore.QSize(500, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(500, 16777215))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_5.addWidget(self.checkBox_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget1)
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setMinimumSize(QtCore.QSize(500, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setMinimumSize(QtCore.QSize(170, 0))
        self.label.setMaximumSize(QtCore.QSize(170, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setMinimumSize(QtCore.QSize(300, 0))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_4.addWidget(self.comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.verticalLayout_7.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.export_button = QtWidgets.QPushButton(self.centralwidget)
        self.export_button.setObjectName("export_button")
        self.horizontalLayout.addWidget(self.export_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1147, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport_Profile = QtWidgets.QAction(MainWindow)
        self.actionExport_Profile.setObjectName("actionExport_Profile")
        self.actionWater_Intake = QtWidgets.QAction(MainWindow)
        self.actionWater_Intake.setObjectName("actionWater_Intake")
        self.actionImportedFilesMetadata = QtWidgets.QAction(MainWindow)
        self.actionImportedFilesMetadata.setObjectName("actionImportedFilesMetadata")
        self.actionBy_Time_Stamp = QtWidgets.QAction(MainWindow)
        self.actionBy_Time_Stamp.setObjectName("actionBy_Time_Stamp")
        self.actionBy_File_Name = QtWidgets.QAction(MainWindow)
        self.actionBy_File_Name.setObjectName("actionBy_File_Name")
        self.actionDsc_files = QtWidgets.QAction(MainWindow)
        self.actionDsc_files.setObjectName("actionDsc_files")
        self.actionDsc = QtWidgets.QAction(MainWindow)
        self.actionDsc.setObjectName("actionDsc")
        self.actionWater_Intake_2 = QtWidgets.QAction(MainWindow)
        self.actionWater_Intake_2.setObjectName("actionWater_Intake_2")
        self.actionProfiles = QtWidgets.QAction(MainWindow)
        self.actionProfiles.setObjectName("actionProfiles")

        self.retranslateUi(MainWindow)
        self.export_button.clicked.connect(MainWindow.export_button_clicked)
        self.pushButton.clicked.connect(MainWindow.help_button_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Profile"))
        self.previous_image_button.setText(_translate("MainWindow", "Prev. Image"))
        self.image_slider_value.setText(_translate("MainWindow", "0"))
        self.next_image_button.setText(_translate("MainWindow", "Next Image"))
        self.checkBox.setText(_translate("MainWindow", "Scale"))
        self.label_2.setText(_translate("MainWindow", "Orientation:"))
        self.radioButton.setText(_translate("MainWindow", "horizontal"))
        self.radioButton_2.setText(_translate("MainWindow", "vertical"))
        self.label_3.setText(_translate("MainWindow", "Size:"))
        self.label_4.setText(_translate("MainWindow", "pixels  ="))
        self.label_5.setText(_translate("MainWindow", "Color:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "White"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Red"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Blue"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Green"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Black"))
        self.checkBox_2.setText(_translate("MainWindow", "Metadata   (Select in Metadata TAB)"))
        self.label.setText(_translate("MainWindow", "Select Metadata To Display"))
        self.label_6.setText(_translate("MainWindow", "Color:"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "White"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Red"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Blue"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Green"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Black"))
        self.pushButton.setText(_translate("MainWindow", "Help"))
        self.export_button.setText(_translate("MainWindow", "Export Images ..."))
        self.actionExport_Profile.setText(_translate("MainWindow", "Profiles ..."))
        self.actionWater_Intake.setText(_translate("MainWindow", "Water Intake ..."))
        self.actionImportedFilesMetadata.setText(_translate("MainWindow", "Imported Files and Metadata ..."))
        self.actionBy_Time_Stamp.setText(_translate("MainWindow", "by Time Stamp"))
        self.actionBy_File_Name.setText(_translate("MainWindow", "by File Name"))
        self.actionDsc_files.setText(_translate("MainWindow", "dsc files ..."))
        self.actionDsc.setText(_translate("MainWindow", "dsc ..."))
        self.actionWater_Intake_2.setText(_translate("MainWindow", "Water Intake ..."))
        self.actionProfiles.setText(_translate("MainWindow", "Profiles ..."))
