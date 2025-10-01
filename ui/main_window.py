from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout

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
