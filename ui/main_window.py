from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTabWidget
from PySide6.QtCore import QFile, QTextStream
from ui.dashboard import Dashboard
from ui.history import History
from ui.settings import Settings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PrintProfitCalc 3D")
        self.resize(1000, 800)
        
        # Load Styles
        self.load_styles()
        
        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Tabs
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)
        
        # Initialize Tabs
        self.dashboard_tab = Dashboard()
        self.history_tab = History()
        self.settings_tab = Settings()
        
        self.tabs.addTab(self.dashboard_tab, "Dashboard")
        self.tabs.addTab(self.history_tab, "Histórico")
        self.tabs.addTab(self.settings_tab, "Configurações")
        
    def load_styles(self):
        style_file = QFile("resources/styles.qss")
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style_file)
            self.setStyleSheet(stream.readAll())
            style_file.close()
