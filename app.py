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
    sql_columns = ("id", "project_id", "status", "`when`", "delegate_id", "title")
    columns_updatable = {"id": False, "project_id": False, "status": True, "`when`": True, "delegate_id": False, "title": True}

    def __init__(self):
        QMainWindow.__init__(self)
        pytask_ui.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Fill statuses filter
        self.filter_status.addItems(("(None)",) + self.valid_statuses)
        self.filter_status.currentTextChanged.connect(self.change_filter)
        # Fill date filter
        self.filter_date.addItems(("(None)",) + self.valid_dates)
        self.filter_date.currentIndexChanged.connect(self.change_filter)
        # Fill the table
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
        self.tableWidget.cellChanged.connect(self.cell_changed)
        self.tableWidget.itemSelectionChanged.connect(self.task_selected)
        # A combo with statuses
        self.statuses_combo = QComboBox()
        self.statuses_combo.addItems(self.valid_statuses)
        # Description field events
        self.task_project.currentIndexChanged.connect(self.task_field_changed)
        self.task_delegate.currentIndexChanged.connect(self.task_field_changed)
        self.task_description.textChanged.connect(self.task_field_changed)
        # Save the record
        self.save_record.clicked.connect(self.save_current_task)

    def change_filter(self, _=None):
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
        for m_id, m_title in m_rs:
            self.task_project.addItem(m_title, m_id)

    def update_tasks(self, recordset):
        self.tableWidget.setRowCount(len(recordset))
        i=0
        self.tableWidget.blockSignals(True)
        for m_row in recordset:
            m_font = QFont()
            m_color = QtCore.Qt.black
            if m_row[2] == "Done":
                m_font.setStrikeOut(True)
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
    
    def cell_changed(self, row, col):
        """
        Upon changing a cell, this function updates correspondent DB value
        """
        m_column = self.sql_columns[col]
        if not self.columns_updatable[m_column]:
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
        self.change_filter("whatever")

    def task_selected(self):
        m_row = self.tableWidget.currentIndex().row()
        m_id = int(self.tableWidget.item(m_row, 0).text())
        self.statusBar.showMessage(f"Record selected: {m_id}")
        self.task_description.setEnabled(True)
        m_sql = "SELECT description FROM tasks WHERE id=:id"
        m_description_value = self.connection.execute(m_sql, {"id": m_id}).fetchone()[0]
        self.task_description.setText(m_description_value)

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
        m_sets = ("project_id=:project_id", "description=:description")
        m_arguments = {
            "project_id": m_project_id,
            "description": m_description,
            "id": m_id
        }
        m_sql_prefix = "UPDATE tasks "
        m_sql_suffix = " WHERE id=:id"
        m_sql_body = " SET " + ", ".join(m_sets)
        self.connection.execute(m_sql_prefix + m_sql_body + m_sql_suffix, m_arguments)
        self.connection.commit()
        self.save_record.setText(">")
        self.change_filter()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PyTask()
    # window = uic.loadUi("helloword.ui")
    window.show()
    sys.exit(app.exec_())