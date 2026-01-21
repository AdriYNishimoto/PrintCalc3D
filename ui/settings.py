from PySide6.QtWidgets import (QWidget, QVBoxLayout, QGroupBox, QGridLayout, 
                               QLabel, QDoubleSpinBox, QSpinBox, QPushButton, QMessageBox)
from data.storage import load_config, save_config

class Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_data()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        # Printer Settings
        printer_group = QGroupBox("Configuração da Impressora")
        printer_layout = QGridLayout()
        
        self.power_consumption = QDoubleSpinBox()
        self.power_consumption.setRange(0, 2000)
        self.power_consumption.setSuffix(" W")
        
        self.energy_rate = QDoubleSpinBox()
        self.energy_rate.setRange(0, 100)
        self.energy_rate.setPrefix("R$ ")
        self.energy_rate.setDecimals(3)
        
        self.maintenance_cost = QDoubleSpinBox()
        self.maintenance_cost.setRange(0, 1000)
        self.maintenance_cost.setPrefix("R$ ")
        
        self.printer_price = QDoubleSpinBox()
        self.printer_price.setRange(0, 100000)
        self.printer_price.setPrefix("R$ ")
        
        self.lifespan_prints = QSpinBox()
        self.lifespan_prints.setRange(1, 1000000)
        
        printer_layout.addWidget(QLabel("Consumo da Impressora:"), 0, 0)
        printer_layout.addWidget(self.power_consumption, 0, 1)
        printer_layout.addWidget(QLabel("Tarifa de Energia (kWh):"), 1, 0)
        printer_layout.addWidget(self.energy_rate, 1, 1)
        printer_layout.addWidget(QLabel("Manutenção Mensal:"), 2, 0)
        printer_layout.addWidget(self.maintenance_cost, 2, 1)
        printer_layout.addWidget(QLabel("Preço da Impressora:"), 3, 0)
        printer_layout.addWidget(self.printer_price, 3, 1)
        printer_layout.addWidget(QLabel("Vida Útil (peças):"), 4, 0)
        printer_layout.addWidget(self.lifespan_prints, 4, 1)
        
        printer_group.setLayout(printer_layout)
        layout.addWidget(printer_group)
        
        # Default Values
        defaults_group = QGroupBox("Valores Padrão de Cálculo")
        defaults_layout = QGridLayout()
        
        self.spool_price = QDoubleSpinBox()
        self.spool_price.setRange(0, 10000)
        self.spool_price.setPrefix("R$ ")
        
        self.spool_weight = QDoubleSpinBox()
        self.spool_weight.setRange(0, 10000)
        self.spool_weight.setSuffix(" g")
        
        self.hourly_rate = QDoubleSpinBox()
        self.hourly_rate.setRange(0, 1000)
        self.hourly_rate.setPrefix("R$ ")
        
        self.profit_margin = QDoubleSpinBox()
        self.profit_margin.setRange(0, 1000)
        self.profit_margin.setSuffix(" %")
        
        defaults_layout.addWidget(QLabel("Preço Padrão do Rolo:"), 0, 0)
        defaults_layout.addWidget(self.spool_price, 0, 1)
        defaults_layout.addWidget(QLabel("Peso Padrão do Rolo:"), 1, 0)
        defaults_layout.addWidget(self.spool_weight, 1, 1)
        defaults_layout.addWidget(QLabel("Valor Padrão da Hora:"), 2, 0)
        defaults_layout.addWidget(self.hourly_rate, 2, 1)
        defaults_layout.addWidget(QLabel("Margem de Lucro Padrão:"), 3, 0)
        defaults_layout.addWidget(self.profit_margin, 3, 1)
        
        defaults_group.setLayout(defaults_layout)
        layout.addWidget(defaults_group)
        
        # Save Button
        self.save_btn = QPushButton("SALVAR CONFIGURAÇÕES")
        self.save_btn.clicked.connect(self.save_data)
        layout.addWidget(self.save_btn)
        
        layout.addStretch()

    def load_data(self):
        config = load_config()
        printer = config.get("printer", {})
        defaults = config.get("defaults", {})
        
        self.power_consumption.setValue(printer.get("power_consumption_w", 0))
        self.energy_rate.setValue(printer.get("energy_rate", 0))
        self.maintenance_cost.setValue(printer.get("monthly_maintenance", 0))
        self.printer_price.setValue(printer.get("printer_price", 0))
        self.lifespan_prints.setValue(printer.get("lifespan_prints", 1))
        
        self.spool_price.setValue(defaults.get("spool_price", 0))
        self.spool_weight.setValue(defaults.get("spool_weight", 1000))
        self.hourly_rate.setValue(defaults.get("hourly_rate", 0))
        self.profit_margin.setValue(defaults.get("profit_margin", 0))

    def save_data(self):
        config = {
            "printer": {
                "name": "Default Printer",
                "power_consumption_w": self.power_consumption.value(),
                "energy_rate": self.energy_rate.value(),
                "monthly_maintenance": self.maintenance_cost.value(),
                "printer_price": self.printer_price.value(),
                "lifespan_prints": self.lifespan_prints.value()
            },
            "defaults": {
                "spool_price": self.spool_price.value(),
                "spool_weight": self.spool_weight.value(),
                "hourly_rate": self.hourly_rate.value(),
                "profit_margin": self.profit_margin.value()
            }
        }
        save_config(config)
        QMessageBox.information(self, "Sucesso", "Configurações salvas com sucesso!")
