from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QStackedWidget, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt,QSize
from .dashboard import DashboardTab
from .file_opener import FileOpenerTab
from .report_generator import ReportGeneratorTab
from .test import NetworkGraphTabTest
from .settings import SettingsTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CypherSol")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("""
                           
            QMainWindow {
                background-color: #f0f0f0;
            }
                           
            QPushButton {
                background-color: #ffffff;
                color: #2c3e50;
                border: none;  
                padding: 12px 20px;
                text-align: left;
                font-size: 16px;
                margin: 2px 10px;
                outline: none;
                border-left: 3px solid transparent;
            }
            QPushButton:hover {
                background-color: #f8f9fa;
                color: #3498db;
            }
            QPushButton:checked {
                background-color: #f0f7ff;
                color: #3498db;
                border-left: 3px solid #3498db;
            }
        """)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Add footer label
        footer_label = QLabel("© Copyright 2024 CypherSOL Fintech India Pvt Ltd.\nAll Rights Reserved")
        footer_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 11px;
                padding: 20px;
                qproperty-alignment: AlignCenter;
            }
        """)
        footer_label.setWordWrap(True)

        # Sidebar
        sidebar = QWidget()
        sidebar.setStyleSheet("""
            QWidget {
                background-color: white;
                border-right: 1px solid #e0e0e0;
            }
        """)
        sidebar.setFixedWidth(300)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setSpacing(0)
        sidebar_layout.setContentsMargins(0, 20, 0, 20)

        # Logo
        logo_label = QLabel()
        logo_pixmap = QPixmap("assets/logo.png")
        scaled_pixmap = logo_pixmap.scaled(200, 60, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        logo_label.setPixmap(scaled_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_label.setContentsMargins(0, 10, 0, 45)
        sidebar_layout.addWidget(logo_label)

        # Navigation buttons with updated styles
        self.nav_buttons = []
        button_icons = [
            ("Dashboard", "dashboard.png"),
            ("File Opener", "file.png"),
            ("Generate Report", "report.png"),
            ("Settings", "settings.png"),
            ("Network Graph Test", "test.png"),
        ]

        for text, icon in button_icons:
            btn = QPushButton(text)
            btn.setIcon(QIcon(f"resources/icons/{icon}"))
            btn.setIconSize(QSize(24, 24))  # Make icons slightly larger
            btn.setCheckable(True)
            btn.setChecked(text == "Dashboard")
            self.nav_buttons.append(btn)
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()
        sidebar_layout.addWidget(footer_label)

        main_layout.addWidget(sidebar)

        # Content area with updated background
        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: #f8f9fa;")
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 20, 20, 20)

        self.content_area = QStackedWidget()
        self.content_area.addWidget(DashboardTab())
        self.content_area.addWidget(FileOpenerTab())
        self.content_area.addWidget(ReportGeneratorTab())
        self.content_area.addWidget(SettingsTab())
        self.content_area.addWidget(NetworkGraphTabTest())

        content_layout.addWidget(self.content_area)
        main_layout.addWidget(content_widget)

        # Connect buttons
        for i, btn in enumerate(self.nav_buttons):
            btn.clicked.connect(lambda checked, index=i: self.switch_page(index))

    def switch_page(self, index):
        self.content_area.setCurrentIndex(index)
        for i, btn in enumerate(self.nav_buttons):
            btn.setChecked(i == index)
