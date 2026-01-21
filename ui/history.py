from PySide6.QtWidgets import (QWidget, QVBoxLayout, QTableWidget, 
                               QTableWidgetItem, QPushButton, QHBoxLayout, 
                               QHeaderView, QMessageBox, QFileDialog)
from data.storage import load_history, export_history_csv

class History(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Data", "Peso da Peça", "Custo Total", "Preço Sugerido", "Tempo de Impressão"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)
        
        # Buttons
        btn_layout = QHBoxLayout()
        
        self.refresh_btn = QPushButton("Atualizar")
        self.refresh_btn.clicked.connect(self.load_data)
        btn_layout.addWidget(self.refresh_btn)
        
        self.export_btn = QPushButton("Exportar para CSV")
        self.export_btn.clicked.connect(self.export_data)
        btn_layout.addWidget(self.export_btn)
        
        layout.addLayout(btn_layout)
        
        self.load_data()

    def load_data(self):
        history = load_history()
        self.table.setRowCount(len(history))
        
        for row, item in enumerate(history):
            self.table.setItem(row, 0, QTableWidgetItem(item.get("date", "")))
            self.table.setItem(row, 1, QTableWidgetItem(f"{item.get('part_weight', 0)} g"))
            self.table.setItem(row, 2, QTableWidgetItem(f"R$ {item.get('total_cost', 0):.2f}"))
            self.table.setItem(row, 3, QTableWidgetItem(f"R$ {item.get('suggested_price', 0):.2f}"))
            self.table.setItem(row, 4, QTableWidgetItem(f"{item.get('print_time', 0)} h"))

    def export_data(self):
        filepath, _ = QFileDialog.getSaveFileName(self, "Exportar CSV", "", "Arquivos CSV (*.csv)")
        if filepath:
            if export_history_csv(filepath):
                QMessageBox.information(self, "Sucesso", "Histórico exportado com sucesso!")
            else:
                QMessageBox.critical(self, "Erro", "Falha ao exportar histórico.")
