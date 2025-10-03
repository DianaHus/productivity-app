from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QTimer, Qt

class TimerWidget(QWidget):
    def __init__(self, minutes = 25):
        super().__init__()
        self.default_seconds = minutes * 60
        self.seconds_left = self.default_seconds
        self.is_running = False

        self.setup_ui()
        self.setup_timer()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # time display
        self.timer_label = QLabel(self.format_time(self.seconds_left))
        self.timer_label.setStyleSheet("font-size: 48px;")
        self.timer_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.timer_label)

        # buttons
        buttons_layout = QHBoxLayout()
        layout.addLayout(buttons_layout)

        self.start_pause_button = QPushButton("Let's go!")
        self.reset_button = QPushButton("Reset")

        buttons_layout.addWidget(self.start_pause_button)
        buttons_layout.addWidget(self.reset_button)

        # buttons connections
        self.start_pause_button.clicked.connect(self.start_pause)
        self.reset_button.clicked.connect(self.reset_timer)

    def setup_timer(self):
        self.timer = QTimer()
        self.timer.setInterval(1000) # 1 sec
        self.timer.timeout.connect(self.update_time)

    def format_time(self, seconds):
        mins = seconds // 60
        secs = seconds % 60
        return f"{mins:02d}:{secs:02d}"
    
    def start_pause(self):
        if self.is_running:
            self.timer.stop()
            self.start_pause_button.setText("Let's go!!")
            self.is_running = False
        else:
            self.timer.start()
            self.start_pause_button.setText("Little break")
            self.is_running = True

    def reset_timer(self):
        self.timer.stop()
        self.seconds_left = self.default_seconds
        self.timer_label.setText(self.format_time(self.seconds_left))
        self.start_pause_button.setText("Let's go!")
        self.is_running = False

    def update_time(self):
        if self.seconds_left > 0:
            self.seconds_left -= 1
            self.timer_label.setText(self.format_time(self.seconds_left))
        else:
            self.timer.stop()
            self.time_label.setText("Time to take a break!")
            self.start_pause_button.setText("Let's go!!!")
            self.is_running = False