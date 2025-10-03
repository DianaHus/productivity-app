from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QPushButton, QListWidgetItem, QCheckBox

class TodoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # main layout for this widget:
        layout = QVBoxLayout()
        self.setLayout(layout)

        # welcome label
        welcome_label = QLabel("LET'S DO SOME TASKS")
        layout.addWidget(welcome_label)

        add_task_layout = QHBoxLayout()
        layout.addLayout(add_task_layout)

        # task input 
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Write here a new task to do")
        add_task_layout.addWidget(self.task_input)

        # add button
        add_button = QPushButton("Add task")
        add_task_layout.addWidget(add_button)

        # task list
        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        # connections
        add_button.clicked.connect(self.add_task) # add task when button clicked
        self.task_input.returnPressed.connect(self.add_task) # add task when 'enter' pressed

    def add_task(self):
        # take input text
        task_text = self.task_input.text()
        # if not empty, add to todo list
        if task_text:
            task_widget = QWidget()
            task_layout = QHBoxLayout(task_widget)

            checkbox = QCheckBox()
            task_label = QLabel(task_text)
            delete_btn = QPushButton('x')
            delete_btn.setMaximumWidth(30) # little button
            delete_btn.clicked.connect(self.delete_task)

            # add everything to the widget
            task_layout.addWidget(checkbox)
            task_layout.addWidget(task_label)
            task_layout.addStretch()
            task_layout.addWidget(delete_btn)

            list_item = QListWidgetItem()
            list_item.setSizeHint(task_widget.sizeHint())

            self.task_list.addItem(list_item)
            self.task_list.setItemWidget(list_item, task_widget)

            self.task_input.clear()

    def delete_task(self):
        # get button that was clicked
        button = self.sender()
        if not button:
            return
        # find widget containing button
        task_widget = button.parent()
        # find corresponding QListWidgetItem
        for i in range(self.task_list.count()):
            item = self.task_list.item(i)
            if self.task_list.itemWidget(i) == task_widget:
                self.task_list.takeItem(i)
                break


