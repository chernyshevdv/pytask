import sqlite3
import sys
from PyQt5 import QtGui, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractScrollArea, QComboBox
from PyQt5.QtGui import QFont, QPalette, QStandardItemModel
from PyQt5.QtCore import Qt
import pytask_ui

class PyTask(QMainWindow, pytask_ui.Ui_MainWindow):
    connection = sqlite3.connect("pyqt.sqlite")
    valid_statuses = ("Backlog", "Estimate", "Selected for development", "WIP", "Done")
    valid_dates = ("today", "this week")
    sql_task_columns = ("id", "project_id", "status", "`when`", "delegate_id", "title")
    task_columns_updatable = {"id": False, "project_id": False, "status": True, "`when`": True, "delegate_id": False, "title": True}
    sql_project_columns = ("id", "title", "success_criteria")
    project_columns_updatable = {"id": False, "title": True, "success_criteria": True}

    def __init__(self):
        QMainWindow.__init__(self)
        pytask_ui.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Fill statuses filter
        self.filter_status.addItems(("(None)",) + self.valid_statuses)
        self.filter_status.currentTextChanged.connect(self.change_tasks_filter)
        # Fill date filter
        self.filter_date.addItems(("(None)",) + self.valid_dates)
        self.filter_date.currentIndexChanged.connect(self.change_tasks_filter)
        # Fill tasks table
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        m_header = self.tableWidget.horizontalHeader()
        m_header.setStretchLastSection(True)
        self.tableWidget.setHorizontalHeader(m_header)
        m_sql = """
        SELECT t.id, p.title as project, t.status, t.`when`, u.name, t.title
        FROM tasks t LEFT JOIN projects p ON t.project_id=p.id
        LEFT JOIN users u ON t.delegate_id=u.id
        """
        m_rs = self.connection.execute(m_sql).fetchall()
        self.update_tasks(m_rs)
        self.load_task_combos()
        # Change table event handlers
        self.tableWidget.cellDoubleClicked.connect(self.enter_change_mode)
        self.tableWidget.cellChanged.connect(self.task_cell_changed)
        self.tableWidget.itemSelectionChanged.connect(self.task_selected)
        # A combo with statuses
        self.statuses_combo = QComboBox()
        self.statuses_combo.addItems(self.valid_statuses)
        # Description field events
        self.task_project.currentIndexChanged.connect(self.task_field_changed)
        self.task_delegate.currentIndexChanged.connect(self.task_field_changed)
        self.task_description.textChanged.connect(self.task_field_changed)
        # Action handlers
        self.save_record.clicked.connect(self.save_current_task)
        self.actionSave.triggered.connect(self.save_current_task)
        self.actionNew_2.triggered.connect(self.new_record)
        self.actionDelete.triggered.connect(self.del_record)
        # load projects when switching to projects tab
        self.tabWidget.currentChanged.connect(self.tab_changed)
        # change project table signal slots
        self.table_projects.cellChanged.connect(self.project_cell_changed)

    def change_tasks_filter(self, _=None):
        """
        Changes filter when one of filter combo boxes changed.
        NB: don't use value (you don't know which control sent the signal), instead take values from self
        """
        m_sql = """
        SELECT t.id, p.title as project, t.status, t.`when`, u.name, t.title
        FROM tasks t LEFT JOIN projects p ON t.project_id=p.id
        LEFT JOIN users u ON t.delegate_id=u.id
        """
        m_conditions = []
        m_arguments = {}
        m_status_filter = self.filter_status.itemText(self.filter_status.currentIndex())
        if m_status_filter != "(None)":
            m_conditions.append("t.status=:status")
            m_arguments["status"] = m_status_filter

        m_date_filter = self.filter_date.itemText(self.filter_date.currentIndex())
        if m_date_filter != "(None)":
            m_conditions.append("t.`when`=:when")
            m_arguments["when"] = m_date_filter
        
        if len(m_conditions) > 0:
            m_where = "WHERE " + " AND ".join(m_conditions)
            m_sql += m_where
            
        m_rs = self.connection.execute(m_sql, m_arguments).fetchall()

        self.update_tasks(m_rs)

    def load_task_combos(self):
        """
        Loads data into comboboxes representing task reference data: project, delegate
        """
        # load projects
        m_rs = self.connection.execute("SELECT id, title FROM projects").fetchall()
        self.task_project.clear()
        self.task_project.addItem("(None)", None)
        for m_id, m_title in m_rs:
            self.task_project.addItem(m_title, m_id)
        # load delegates
        self.task_delegate.clear()
        self.task_delegate.addItem("(None)", None)
        m_rs = self.connection.execute("SELECT id, name FROM users ORDER BY name").fetchall()
        for m_id, m_title in m_rs:
            self.task_delegate.addItem(m_title, m_id)

    def update_tasks(self, recordset):
        self.tableWidget.setRowCount(len(recordset))
        i=0
        self.tableWidget.blockSignals(True)
        for m_row in recordset:
            m_font = QFont()
            m_color = QtCore.Qt.black
            if m_row[2] == "Done":
                m_font.setStrikeOut(True)
            elif m_row[4] is not None:
                m_color = QtCore.Qt.blue
            elif m_row[3] == "today":
                m_color = QtCore.Qt.darkGreen
            for m_col in range(len(m_row)):
                m_value = str(m_row[m_col])
                m_item = QTableWidgetItem(m_value)
                m_item.setFont(m_font)
                m_item.setForeground(m_color)
                self.tableWidget.setItem(i, m_col, m_item)
            i+=1
        self.tableWidget.blockSignals(False)
        self.tableWidget.resizeColumnsToContents()
    
    def enter_change_mode(self, row, column):
        if column == 3:  # status cell
            self.statuses_combo.setItemData(0, self.tableWidget.item(row, column))
            self.tableWidget.setCellWidget(row, column, self.statuses_combo)
    
    def task_cell_changed(self, row, col):
        """
        Upon changing a task table cell, this function updates correspondent DB value
        """
        m_column = self.sql_task_columns[col]
        if not self.task_columns_updatable[m_column]:
            self.statusBar.showMessage(f"Column {m_column} is not updateable.")
            return
        m_id = self.tableWidget.item(row, 0).text()
        m_new_value = self.tableWidget.item(row, col).text()
        m_sql_prefix = "UPDATE tasks "
        
        m_sql_set = f"SET {m_column}=:{m_column} "
        m_sql_suffix = "WHERE id=:id"
        m_params = {"id": m_id, m_column: m_new_value}
        self.connection.execute(m_sql_prefix + m_sql_set + m_sql_suffix, m_params)
        self.connection.commit()
        self.change_tasks_filter("whatever")
    
    def project_cell_changed(self, row, col):
        """
        Upon changing a project table cell, this function updates correspondent DB value
        """
        m_column = self.sql_project_columns[col]
        if not self.project_columns_updatable[m_column]:
            self.statusBar.showMessage(f"Project {m_column} is not updateable.")
            return
        m_id = self.table_projects.item(row, 0).text()
        m_new_value = self.table_projects.item(row, col).text()
        m_sql_prefix = "UPDATE projects "
        
        m_sql_set = f"SET {m_column}=:{m_column} "
        m_sql_suffix = "WHERE id=:id"
        m_params = {"id": m_id, m_column: m_new_value}
        self.connection.execute(m_sql_prefix + m_sql_set + m_sql_suffix, m_params)
        self.connection.commit()
        self.load_projects_table()


    def task_selected(self):
        self.save_record.setText('>')
        m_row = self.tableWidget.currentIndex().row()
        m_id = int(self.tableWidget.item(m_row, 0).text())
        self.statusBar.showMessage(f"Record selected: {m_id}")
        self.task_description.setEnabled(True)
        m_sql = "SELECT description, project_id, delegate_id FROM tasks WHERE id=:id"
        m_values = self.connection.execute(m_sql, {"id": m_id}).fetchone()
        m_description_value = m_values[0]
        self.task_description.setText(m_description_value)
        # set project value
        m_project_index = self.task_project.findData(m_values[1], role=Qt.UserRole)
        self.task_project.setCurrentIndex(m_project_index)
        # set delegate value
        m_delegate_index = self.task_delegate.findData(m_values[2], role=Qt.UserRole)
        self.task_delegate.setCurrentIndex(m_delegate_index)

    def task_description_changed(self):
        print("Description changed.")

    def task_field_changed(self, value=None):
        #m_item = self.task_project.model().itemFromIndex(self.task_project.currentIndex())
        # m_text = self.task_project.itemText(self.task_project.currentIndex())
        # m_data = self.task_project.itemData(self.task_project.currentIndex())
        # print(f"Project: {m_text}; data: {m_data}")
        self.save_record.setText("*")
    
    def save_current_task(self):
        if self.save_record.text() == ">":
            return
        m_row = self.tableWidget.currentIndex().row()
        m_id = int(self.tableWidget.item(m_row, 0).text())
        m_project_id = self.task_project.itemData(self.task_project.currentIndex())
        m_description = self.task_description.toPlainText()
        m_delegate_id = self.task_delegate.itemData(self.task_delegate.currentIndex())
        m_sets = ("project_id=:project_id", "description=:description", "delegate_id=:delegate_id")
        m_arguments = {
            "project_id": m_project_id,
            "description": m_description,
            "delegate_id": m_delegate_id,
            "id": m_id
        }
        m_sql_prefix = "UPDATE tasks "
        m_sql_suffix = " WHERE id=:id"
        m_sql_body = " SET " + ", ".join(m_sets)
        self.connection.execute(m_sql_prefix + m_sql_body + m_sql_suffix, m_arguments)
        self.connection.commit()
        self.save_record.setText(">")
        self.change_tasks_filter()
    
    def new_record(self):
        m_handlers = {0: self.new_task_record, 1: self.new_project_record}
        m_handlers[self.tabWidget.currentIndex()]()

    def new_task_record(self):
        self.connection.execute("INSERT INTO tasks (title) VALUES ('<new task>')")
        self.connection.commit()
        self.change_tasks_filter()
    
    def new_project_record(self):
        self.connection.execute("INSERT INTO projects (title) VALUES ('<new project>')")
        self.connection.commit()
        self.load_projects_table()
    
    def del_record(self):
        m_handler = {0: self.del_task, 1: self.del_project}
        m_handler[self.tabWidget.currentIndex()]()

    def del_project(self):
        m_row = self.table_projects.currentIndex().row()
        m_id = int(self.table_projects.item(m_row, 0).text())
        self.connection.execute("DELETE FROM projects WHERE id=:id", {"id": m_id})
        self.connection.commit()
        self.load_projects_table()

    def del_task(self):
        m_row = self.tableWidget.currentIndex().row()
        m_id = int(self.tableWidget.item(m_row, 0).text())
        self.connection.execute("DELETE FROM tasks WHERE id=:id", {"id": m_id})
        self.connection.commit()
        self.change_tasks_filter()
    
    def tab_changed(self, tab_num):
        m_handlers = {0: self.change_tasks_filter, 1: self.load_projects_table}
        m_handlers[tab_num]()
    
    def load_projects_table(self):
        m_sql = "SELECT id, title, success_criteria FROM projects"
        m_rs = self.connection.execute(m_sql).fetchall()
        # self.table_projects.clear()
        self.table_projects.setRowCount(len(m_rs))
        self.table_projects.blockSignals(True)
        for i, m_row in enumerate(m_rs):
            for j, m_value in enumerate(m_row):
                self.table_projects.setItem(i, j, QTableWidgetItem(str(m_value)))
        self.table_projects.resizeColumnsToContents()
        self.table_projects.blockSignals(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PyTask()
    # window = uic.loadUi("helloword.ui")
    window.show()
    sys.exit(app.exec_())