from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QPushButton, QListWidgetItem, QCheckBox
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window title
        self.setWindowTitle("Diana's Productivity App 🚀")

        # Window dimensions
        self.setGeometry(100, 100, 600, 400)

        # Central widget creation (mandatory)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Let's create a vertical layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        # label to the layout
        welcome_label = QLabel("Welcome to my productivity app :)")
        layout.addWidget(welcome_label)

        # Task input:
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Write here a new task to do")
        layout.addWidget(self.task_input)
        # add button
        add_button = QPushButton("Add task")
        layout.addWidget(add_button)
        self.task_list = QListWidget()
        layout.addWidget(self.task_list)
        # add to the list when button clicked
        add_button.clicked.connect(self.add_task)
        # add to the list when 'Enter' button pressed
        self.task_input.returnPressed.connect(self.add_task)


    def add_task(self):
        # take input text
        task_text = self.task_input.text()
        # if not empty, add to list
        if task_text:
            task_widget = QWidget()
            task_layout = QHBoxLayout(task_widget)
            # checkbox
            checkbox = QCheckBox()

            task_label = QLabel(task_text)

            delete_btn = QPushButton("x")
            delete_btn.setMaximumWidth(30) # smally

            # add everything to the widget
            task_layout.addWidget(checkbox)
            task_layout.addWidget(task_label)
            task_layout.addStretch() # elastic space
            task_layout.addWidget(delete_btn)

            list_item = QListWidgetItem()
            list_item.setSizeHint(task_widget.sizeHint())

            self.task_list.addItem(list_item)
            self.task_list.setItemWidget(list_item, task_widget)

            self.task_input.clear()
