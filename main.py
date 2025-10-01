import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow


def main():
    """Entry point of the application"""
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Productivity App")
    app.setApplicationVersion("1.0")
    
    # Create and show the main window
    window = MainWindow()
    window.show()
    
    # Start the event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
