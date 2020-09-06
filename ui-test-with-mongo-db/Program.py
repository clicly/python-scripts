import pymongo as pymongo
import pandas as pandas
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QTextEdit, QInputDialog, QFileDialog, \
    QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import pyqtSlot
from Objects import User as User, Weight as Weight, Visualisation as Visualization, Stats as Stats


class MongoConf:
    def __init__(self, client, database, collection):
        self.client = client
        self.database = database
        self.collection = collection


# ----------------------------------------------------------------------------------------------------


client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["fitness"]

user_collection = database["users"]
weight_collection = database["weights"]

user_config = MongoConf(client, database, user_collection)
weight_config = MongoConf(client, database, weight_collection)


# ----------------------------------------------------------------------------------------------------


class ChildWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ChildWindow, self).__init__(parent)
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.text_edit = QTextEdit()


# ----------------------------------------------------------------------------------------------------


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        # new window
        self.child_help_window = ChildWindow(self)
        self.init_help_ui()
        self.child_training_window = ChildWindow(self)
        self.init_training_ui()
        # windows specifications
        self.title = 'Fitness is FUN'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # show window
        self.show()
        # select username
        self.username = self.get_username()
        # start User interface
        self.init_main_ui()

    def init_main_ui(self):
        main_menu = self.menuBar()
        user_menu = main_menu.addMenu('User')

        training_menu = QAction('Training', self)
        training_menu.triggered.connect(self.show_training_window)
        main_menu.addAction(training_menu)

        weight_menu = main_menu.addMenu('Weight')
        visualization_menu = main_menu.addMenu('Visualization')
        stats_menu = main_menu.addMenu('Stats')
        help_menu = main_menu.addMenu('Help')

        # --------

        menu_item = QAction('Create User', self)
        menu_item.setStatusTip('Create User')
        menu_item.triggered.connect(self.create_user)
        user_menu.addAction(menu_item)

        menu_item = QAction('Read Users', self)
        menu_item.setStatusTip('Read Users')
        menu_item.triggered.connect(self.show_users)
        user_menu.addAction(menu_item)

        menu_item = QAction('Delete Users', self)
        menu_item.setStatusTip('Delete Users')
        menu_item.triggered.connect(self.delete_users)
        user_menu.addAction(menu_item)

        menu_item = QAction('Import Users', self)
        menu_item.setStatusTip('Import Users')
        menu_item.triggered.connect(self.import_users)
        user_menu.addAction(menu_item)

        menu_item = QAction('Create Weight', self)
        menu_item.setStatusTip('Create Weight')
        menu_item.triggered.connect(self.create_weight)
        weight_menu.addAction(menu_item)

        menu_item = QAction('Read Weights', self)
        menu_item.setStatusTip('Read Weights')
        menu_item.triggered.connect(self.show_weights)
        weight_menu.addAction(menu_item)

        menu_item = QAction('Delete Weights', self)
        menu_item.setStatusTip('Delete Weights')
        menu_item.triggered.connect(self.delete_weights)
        weight_menu.addAction(menu_item)

        menu_item = QAction('Import Weights', self)
        menu_item.setStatusTip('Import Weights')
        menu_item.triggered.connect(self.import_weights)
        weight_menu.addAction(menu_item)

        menu_item = QAction('Visualize Weight Count', self)
        menu_item.setStatusTip('Visualize Weight Count')
        menu_item.triggered.connect(self.visualize_weights_count)
        visualization_menu.addAction(menu_item)

        menu_item = QAction('Visualize Weight Date', self)
        menu_item.setStatusTip('Visualize Weight Date')
        menu_item.triggered.connect(self.visualize_weights_date)
        visualization_menu.addAction(menu_item)

        menu_item = QAction('Show Stats', self)
        menu_item.setStatusTip('Show Stats')
        menu_item.triggered.connect(self.show_stats)
        stats_menu.addAction(menu_item)

        menu_item = QAction('Test Databases', self)
        menu_item.setStatusTip('Test Databases')
        menu_item.triggered.connect(self.show_help_ui)
        help_menu.addAction(menu_item)

        exit_button = QAction('Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)
        help_menu.addAction(exit_button)

        # Standard Widget
        self.show_stats()

    # USERNAME

    def get_username(self):
        # input dialog
        username, ok_pressed = QInputDialog.getText(self, "Get text", "Wie heißen Sie?", QLineEdit.Normal, "")

        # answer
        if ok_pressed and username != '' and username.__eq__("Max"):
            return username
        elif not ok_pressed:
            return sys.exit(0)
        else:
            return self.get_username()

    # USERS

    # User.insert(user_config, User.User("Max", 24, "m", ["Bankdrücken", "Plank", "Liegestütze", "Bustpresse", "Latzug"]
    # User.delete_by_user_id(user_config, 1)
    # User.delete_by_username(user_config, "Max")

    def show_users(self):
        # use Database
        user_json = User.read_all_users(user_config)

        # create Table
        table_widget = QTableWidget()
        table_widget.setRowCount(User.get_collection_count(user_config, {}))
        table_widget.setColumnCount(5)

        # insert databaseitems into table
        i = 0
        for json in user_json:
            table_widget.setItem(i, 0, QTableWidgetItem(self.username))
            table_widget.setItem(i, 1, QTableWidgetItem(str(json["userid"])))
            table_widget.setItem(i, 2, QTableWidgetItem(str(json["age"])))
            table_widget.setItem(i, 3, QTableWidgetItem(str(json["sex"])))
            table_widget.setItem(i, 4, QTableWidgetItem(str(json["exercises"])))
            i += 1

        # table selection change
        table_widget.doubleClicked.connect(self.on_click_user_collection)

        # show on main window
        self.setCentralWidget(table_widget)

        # make sure that table_widget can be adressed in other methods
        self.tableMax_widget = table_widget

    @pyqtSlot()
    def on_click_user_collection(self):

        for currentQTableWidgetItem in self.table_widget.selectedItems():
            if currentQTableWidgetItem.column() == 1:
                choice = QMessageBox.question(self, 'Löschvorgang',
                                              "Möchten Sie diesen Eintrag löschen?",
                                              QMessageBox.Yes | QMessageBox.No)
                if choice == QMessageBox.Yes:
                    User.delete_by_user_id(user_config, float(currentQTableWidgetItem.text()))
                    self.show_users()

    def create_user(self):
        print("Create user")
        # TODO

    def delete_users(self):
        print("Delete user")
        # TODO

    def import_users(self):
        print("Delete user")
        # TODO

    # WEIGHTS

    def show_weights(self):
        # use database
        user = User.read_user_by_name(user_config, self.username)
        weight_json = Weight.find_by_user_id(weight_config, user["userid"])

        # create table
        table_widget = QTableWidget()
        table_widget.setRowCount(Weight.get_collection_count(weight_config, {"userid": user["userid"]}))
        table_widget.setColumnCount(5)

        # insert database items into table
        i = 0
        for json in weight_json:
            table_widget.setItem(i, 0, QTableWidgetItem(self.username))
            table_widget.setItem(i, 1, QTableWidgetItem(str(json["weightid"])))
            table_widget.setItem(i, 2, QTableWidgetItem(str(json["weight"])))
            table_widget.setItem(i, 3, QTableWidgetItem(str(json["date"])))
            table_widget.setItem(i, 4, QTableWidgetItem(str(json["error"])))
            i += 1

        # table selection change
        table_widget.doubleClicked.connect(self.on_click_weight_collection)

        # show on main window
        self.setCentralWidget(table_widget)

        # make sure that table_widget can be adressed in other methods
        self.table_widget = table_widget

    @pyqtSlot()
    def on_click_weight_collection(self):

        for currentQTableWidgetItem in self.table_widget.selectedItems():
            if currentQTableWidgetItem.column() == 1:
                choice = QMessageBox.question(self, 'Löschvorgang',
                                                    "Möchten Sie diesen Eintrag löschen?",
                                                    QMessageBox.Yes | QMessageBox.No)
                if choice == QMessageBox.Yes:
                    Weight.delete_by_weight_id(weight_config, float(currentQTableWidgetItem.text()))
                    self.show_weights()

            # else: TODO Update when other column

    def get_user_weight(self):
        userweight, ok_pressed = QInputDialog.getDouble(self, "Get double", "Wieviel wiegen Sie?", 80.0)
        if ok_pressed:
            return userweight

    def create_weight(self):
        # use database
        user = User.read_user_by_name(user_config, self.username)
        self.userweight = self.get_user_weight()
        Weight.insert_to_user(weight_config, user["userid"], Weight.Weight(user["userid"], float(self.userweight), "24.07.2019", float('NaN')))

        # reload weights
        self.show_weights()

    def delete_weights(self):
        user = User.read_user_by_name(user_config, self.username)
        choice = QMessageBox.question(self, 'Löschvorgang',
                                      "Möchten Sie alle Einträge löschen?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            Weight.delete_by_user_id(weight_config, user["userid"])
            self.show_weights()
        else:
            pass

    def import_weights(self):
        user = User.read_user_by_name(user_config, self.username)
        filename = QFileDialog.getOpenFileName()
        path = filename[0].__str__()
        csv = pandas.read_csv(path, delimiter=";", names=["date", "kg", "time", "error"])
        Weight.insert_csv_to_user(weight_config, user["userid"], csv)
        self.show_weights()

    # TODO export_weights

    # VISUALIZATION

    def visualize_weights_count(self):
        user = User.read_user_by_name(user_config, self.username)
        user_weight_collection = Weight.find_by_user_id(weight_config, user["userid"])

        weight_array = []
        for json in user_weight_collection:
            weight_array.append(json["weight"])

        Visualization.get_single_graph(weight_array)

    def visualize_weights_date(self):
        user = User.read_user_by_name(user_config, self.username)
        user_weight_collection = Weight.find_by_user_id(weight_config, user["userid"])

        date_array = []
        weight_array = []
        for json in user_weight_collection:
            date_array.append(json["date"])
            weight_array.append(json["weight"])

        Visualization.get_date_graph(date_array, weight_array, 30)

    # STATS

    def show_stats(self):
        user = User.read_user_by_name(user_config, self.username)
        user_weight_collection = Weight.find_by_user_id(weight_config, user["userid"])

        weight_array = []
        for json in user_weight_collection:
            weight_array.append(json["weight"])

        stats_string = Stats.get_stats(weight_array)

        text_widget = QTextEdit()
        text_widget.setReadOnly(1)
        text_widget.setText(stats_string)
        self.setCentralWidget(text_widget)

    # HELP

    def init_help_ui(self):
        self.child_help_window.text_edit.setReadOnly(1)
        self.child_help_window.setCentralWidget(self.child_help_window.text_edit)
        self.child_help_window.text_edit.setText(Weight.test_db(weight_config) + "\n" + User.test_db(user_config))

    def show_help_ui(self):
        if self.child_help_window.isHidden():
            self.child_help_window.show()

    # TRAINING

    def init_training_ui(self):
        main_menu = self.child_training_window.menuBar()
        user_menu = main_menu.addMenu('Excercises')
        stats_menu = main_menu.addMenu('Training')
        help_menu = main_menu.addMenu('Help')

    def show_training_window(self):
        if self.child_training_window.isHidden():
            self.child_training_window.show()


# ----------------------------------------------------------------------------------------------------


def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
