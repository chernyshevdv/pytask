# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pytask.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(987, 785)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_tasks = QtWidgets.QWidget()
        self.tab_tasks.setObjectName("tab_tasks")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_tasks)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab_tasks)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.filter_status = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_status.sizePolicy().hasHeightForWidth())
        self.filter_status.setSizePolicy(sizePolicy)
        self.filter_status.setObjectName("filter_status")
        self.horizontalLayout_2.addWidget(self.filter_status)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.filter_project = QtWidgets.QComboBox(self.groupBox)
        self.filter_project.setObjectName("filter_project")
        self.horizontalLayout_2.addWidget(self.filter_project)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.filter_date = QtWidgets.QComboBox(self.groupBox)
        self.filter_date.setObjectName("filter_date")
        self.horizontalLayout_2.addWidget(self.filter_date)
        self.verticalLayout.addWidget(self.groupBox)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_tasks)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 4, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_tasks)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_task_form = QtWidgets.QWidget(self.groupBox_2)
        self.widget_task_form.setObjectName("widget_task_form")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_task_form)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_task_selector = QtWidgets.QWidget(self.widget_task_form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_task_selector.sizePolicy().hasHeightForWidth())
        self.widget_task_selector.setSizePolicy(sizePolicy)
        self.widget_task_selector.setObjectName("widget_task_selector")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_task_selector)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.save_record = QtWidgets.QPushButton(self.widget_task_selector)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_record.sizePolicy().hasHeightForWidth())
        self.save_record.setSizePolicy(sizePolicy)
        self.save_record.setMinimumSize(QtCore.QSize(10, 10))
        self.save_record.setMaximumSize(QtCore.QSize(40, 16777215))
        self.save_record.setBaseSize(QtCore.QSize(10, 10))
        self.save_record.setObjectName("save_record")
        self.horizontalLayout_5.addWidget(self.save_record)
        self.horizontalLayout_3.addWidget(self.widget_task_selector)
        self.widget_task_record = QtWidgets.QWidget(self.widget_task_form)
        self.widget_task_record.setObjectName("widget_task_record")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_task_record)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_task_combos = QtWidgets.QWidget(self.widget_task_record)
        self.widget_task_combos.setObjectName("widget_task_combos")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_task_combos)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.widget_task_combos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.task_project = QtWidgets.QComboBox(self.widget_task_combos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task_project.sizePolicy().hasHeightForWidth())
        self.task_project.setSizePolicy(sizePolicy)
        self.task_project.setObjectName("task_project")
        self.horizontalLayout_6.addWidget(self.task_project)
        self.label_4 = QtWidgets.QLabel(self.widget_task_combos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.task_delegate = QtWidgets.QComboBox(self.widget_task_combos)
        self.task_delegate.setObjectName("task_delegate")
        self.horizontalLayout_6.addWidget(self.task_delegate)
        self.verticalLayout_2.addWidget(self.widget_task_combos)
        self.label_5 = QtWidgets.QLabel(self.widget_task_record)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.task_description = QtWidgets.QTextEdit(self.widget_task_record)
        self.task_description.setObjectName("task_description")
        self.verticalLayout_2.addWidget(self.task_description)
        self.horizontalLayout_3.addWidget(self.widget_task_record)
        self.horizontalLayout_4.addWidget(self.widget_task_form)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab_tasks, "")
        self.tab_projects = QtWidgets.QWidget()
        self.tab_projects.setObjectName("tab_projects")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_projects)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.table_projects = QtWidgets.QTableWidget(self.tab_projects)
        self.table_projects.setAlternatingRowColors(True)
        self.table_projects.setRowCount(1)
        self.table_projects.setObjectName("table_projects")
        self.table_projects.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.table_projects.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_projects.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_projects.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_projects.setHorizontalHeaderItem(2, item)
        self.table_projects.horizontalHeader().setStretchLastSection(True)
        self.table_projects.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.table_projects)
        self.tabWidget.addTab(self.tab_projects, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 987, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName("actionSave")
        self.actionNew_2 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_2.setIcon(icon1)
        self.actionNew_2.setObjectName("actionNew_2")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon2)
        self.actionDelete.setObjectName("actionDelete")
        self.menuNew.addAction(self.actionNew_2)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuEdit.addAction(self.actionDelete)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNew_2)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addSeparator()
        self.label.setBuddy(self.filter_status)
        self.label_6.setBuddy(self.filter_project)
        self.label_2.setBuddy(self.filter_date)
        self.label_3.setBuddy(self.task_project)
        self.label_4.setBuddy(self.task_delegate)
        self.label_5.setBuddy(self.task_description)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.filter_status)
        MainWindow.setTabOrder(self.filter_status, self.filter_project)
        MainWindow.setTabOrder(self.filter_project, self.filter_date)
        MainWindow.setTabOrder(self.filter_date, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.save_record)
        MainWindow.setTabOrder(self.save_record, self.task_project)
        MainWindow.setTabOrder(self.task_project, self.task_delegate)
        MainWindow.setTabOrder(self.task_delegate, self.task_description)
        MainWindow.setTabOrder(self.task_description, self.table_projects)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Filters:"))
        self.label.setText(_translate("MainWindow", "status:"))
        self.label_6.setText(_translate("MainWindow", "project:"))
        self.label_2.setText(_translate("MainWindow", "date:"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "project"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "status"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "when"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "delegate"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "esimate"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "priority"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "title"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_2.setTitle(_translate("MainWindow", "Task details:"))
        self.save_record.setText(_translate("MainWindow", ">"))
        self.label_3.setText(_translate("MainWindow", "project:"))
        self.label_4.setText(_translate("MainWindow", "delegate:"))
        self.label_5.setText(_translate("MainWindow", "Description:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tasks), _translate("MainWindow", "Tasks"))
        item = self.table_projects.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.table_projects.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table_projects.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "title"))
        item = self.table_projects.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "success criteria"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_projects), _translate("MainWindow", "Projects"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionNew_2.setText(_translate("MainWindow", "New"))
        self.actionNew_2.setShortcut(_translate("MainWindow", "Ins"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Del"))
import myresource_rc
