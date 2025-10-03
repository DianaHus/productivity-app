from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QPushButton, QListWidgetItem, QCheckBox, QStackedWidget
from PySide6.QtCore import Qt
from models.todo_widget import TodoWidget

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
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Navigation bar between the different views
        nav_layout = QHBoxLayout()

        # == Navigation Buttons ==
        self.todo_button = QPushButton("Task List")
        self.timer_button = QPushButton("Pomodoro Time")

        nav_layout.addWidget(self.todo_button)
        nav_layout.addWidget(self.timer_button)
        nav_layout.addStretch() # compress buttons on left
        
        main_layout.addLayout(nav_layout)

        # == Content Area ==
        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        self.todo_widget = TodoWidget()
        self.stacked_widget.addWidget(self.todo_widget)

        # for now placeholder for timer widget
        placeholder_timer = QWidget()
        self.stacked_widget.addWidget(placeholder_timer)

        # == connections ==
        self.todo_button.clicked.connect(self.show_todo)
        self.timer_button.clicked.connect(self.show_timer)

        # show todo list at start
        self.show_todo()

    def show_todo(self):
        """Show todo page/view"""
        self.stacked_widget.setCurrentWidget(self.todo_widget)
        # hilight active button
        self.todo_button.setStyleSheet("background-color: #e0e0e0;")
        self.timer_button.setStyleSheet("")

    def show_timer(self):
        """Show timer page"""
        self.stacked_widget.setCurrentIndex(1)  # Indice del placeholder timer
        # Evidenzia il bottone attivo
        self.timer_button.setStyleSheet("background-color: #e0e0e0;")
        self.todo_button.setStyleSheet("")