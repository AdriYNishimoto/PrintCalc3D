from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, 
                               QLabel, QLineEdit, QComboBox, QPushButton, QGroupBox, 
                               QScrollArea, QMessageBox, QDoubleSpinBox, QSpinBox)
from PySide6.QtCore import Qt
from core.costs import (calculate_filament_cost, calculate_energy_cost, 
                       calculate_labor_cost, calculate_maintenance_cost, 
                       calculate_amortization, calculate_total_cost, suggest_price)
from data.storage import load_config, save_history
from datetime import datetime

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_defaults()

    def init_ui(self):
        main_layout = QHBoxLayout(self)
        
        # Left Side - Inputs
        input_scroll = QScrollArea()
        input_scroll.setWidgetResizable(True)
        input_widget = QWidget()
        input_layout = QVBoxLayout(input_widget)
        
        # Section 1: Material
        material_group = QGroupBox("Material")
        material_layout = QGridLayout()
        
        self.spool_price = QDoubleSpinBox()
        self.spool_price.setRange(0, 10000)
        self.spool_price.setPrefix("R$ ")
        
        self.spool_weight = QDoubleSpinBox()
        self.spool_weight.setRange(0, 10000)
        self.spool_weight.setSuffix(" g")
        
        self.part_weight = QDoubleSpinBox()
        self.part_weight.setRange(0, 10000)
        self.part_weight.setSuffix(" g")
        
        material_layout.addWidget(QLabel("Preço do Rolo:"), 0, 0)
        material_layout.addWidget(self.spool_price, 0, 1)
        material_layout.addWidget(QLabel("Peso do Rolo:"), 1, 0)
        material_layout.addWidget(self.spool_weight, 1, 1)
        material_layout.addWidget(QLabel("Peso da Peça:"), 2, 0)
        material_layout.addWidget(self.part_weight, 2, 1)
        
        material_group.setLayout(material_layout)
        input_layout.addWidget(material_group)
        
        # Section 2: Print Time & Energy
        energy_group = QGroupBox("Tempo e Energia")
        energy_layout = QGridLayout()
        
        self.print_time = QDoubleSpinBox()
        self.print_time.setRange(0, 1000)
        self.print_time.setSuffix(" h")
        
        self.power_consumption = QDoubleSpinBox()
        self.power_consumption.setRange(0, 2000)
        self.power_consumption.setSuffix(" W")
        
        self.energy_rate = QDoubleSpinBox()
        self.energy_rate.setRange(0, 100)
        self.energy_rate.setPrefix("R$ ")
        self.energy_rate.setDecimals(3)
        
        energy_layout.addWidget(QLabel("Tempo de Impressão:"), 0, 0)
        energy_layout.addWidget(self.print_time, 0, 1)
        energy_layout.addWidget(QLabel("Consumo da Impressora:"), 1, 0)
        energy_layout.addWidget(self.power_consumption, 1, 1)
        energy_layout.addWidget(QLabel("Tarifa de Energia (kWh):"), 2, 0)
        energy_layout.addWidget(self.energy_rate, 2, 1)
        
        energy_group.setLayout(energy_layout)
        input_layout.addWidget(energy_group)
        
        # Section 3: Labor
        labor_group = QGroupBox("Mão de Obra")
        labor_layout = QGridLayout()
        
        self.hourly_rate = QDoubleSpinBox()
        self.hourly_rate.setRange(0, 1000)
        self.hourly_rate.setPrefix("R$ ")
        
        self.prep_time = QDoubleSpinBox()
        self.prep_time.setRange(0, 100)
        self.prep_time.setSuffix(" h")
        
        labor_layout.addWidget(QLabel("Valor da Hora:"), 0, 0)
        labor_layout.addWidget(self.hourly_rate, 0, 1)
        labor_layout.addWidget(QLabel("Tempo de Prep/Pós:"), 1, 0)
        labor_layout.addWidget(self.prep_time, 1, 1)
        
        labor_group.setLayout(labor_layout)
        input_layout.addWidget(labor_group)
        
        # Section 4: Printer & Maintenance
        printer_group = QGroupBox("Impressora e Manutenção")
        printer_layout = QGridLayout()
        
        self.maintenance_cost = QDoubleSpinBox()
        self.maintenance_cost.setRange(0, 1000)
        self.maintenance_cost.setPrefix("R$ ")
        
        self.monthly_prints = QSpinBox()
        self.monthly_prints.setRange(1, 10000)
        
        self.printer_price = QDoubleSpinBox()
        self.printer_price.setRange(0, 100000)
        self.printer_price.setPrefix("R$ ")
        
        self.lifespan_prints = QSpinBox()
        self.lifespan_prints.setRange(1, 1000000)
        
        printer_layout.addWidget(QLabel("Manutenção Mensal:"), 0, 0)
        printer_layout.addWidget(self.maintenance_cost, 0, 1)
        printer_layout.addWidget(QLabel("Est. Impressões Mensais:"), 1, 0)
        printer_layout.addWidget(self.monthly_prints, 1, 1)
        printer_layout.addWidget(QLabel("Preço da Impressora:"), 2, 0)
        printer_layout.addWidget(self.printer_price, 2, 1)
        printer_layout.addWidget(QLabel("Vida Útil (peças):"), 3, 0)
        printer_layout.addWidget(self.lifespan_prints, 3, 1)
        
        printer_group.setLayout(printer_layout)
        input_layout.addWidget(printer_group)
        
        # Section 5: Additional & Profit
        other_group = QGroupBox("Adicionais e Lucro")
        other_layout = QGridLayout()
        
        self.additional_costs = QDoubleSpinBox()
        self.additional_costs.setRange(0, 1000)
        self.additional_costs.setPrefix("R$ ")
        
        self.profit_margin = QDoubleSpinBox()
        self.profit_margin.setRange(0, 1000)
        self.profit_margin.setSuffix(" %")
        
        other_layout.addWidget(QLabel("Custos Adicionais:"), 0, 0)
        other_layout.addWidget(self.additional_costs, 0, 1)
        other_layout.addWidget(QLabel("Margem de Lucro:"), 1, 0)
        other_layout.addWidget(self.profit_margin, 1, 1)
        
        other_group.setLayout(other_layout)
        input_layout.addWidget(other_group)
        
        # Calculate Button
        self.calc_btn = QPushButton("CALCULAR")
        self.calc_btn.clicked.connect(self.calculate)
        input_layout.addWidget(self.calc_btn)
        
        input_layout.addStretch()
        input_scroll.setWidget(input_widget)
        main_layout.addWidget(input_scroll, 2)
        
        # Right Side - Results
        result_group = QGroupBox("Resultados")
        result_layout = QVBoxLayout()
        
        self.results_label = QLabel("Insira os valores e clique em Calcular")
        self.results_label.setAlignment(Qt.AlignTop)
        self.results_label.setWordWrap(True)
        
        result_layout.addWidget(self.results_label)
        result_layout.addStretch()
        
        # Save Button
        self.save_btn = QPushButton("SALVAR NO HISTÓRICO")
        self.save_btn.clicked.connect(self.save_result)
        self.save_btn.setEnabled(False)
        self.save_btn.setObjectName("SecondaryButton")
        result_layout.addWidget(self.save_btn)
        
        result_group.setLayout(result_layout)
        main_layout.addWidget(result_group, 1)
        
        self.current_result = None

    def load_defaults(self):
        config = load_config()
        defaults = config.get("defaults", {})
        printer = config.get("printer", {})
        
        self.spool_price.setValue(defaults.get("spool_price", 0))
        self.spool_weight.setValue(defaults.get("spool_weight", 1000))
        self.hourly_rate.setValue(defaults.get("hourly_rate", 0))
        self.profit_margin.setValue(defaults.get("profit_margin", 0))
        
        self.power_consumption.setValue(printer.get("power_consumption_w", 0))
        self.energy_rate.setValue(printer.get("energy_rate", 0))
        self.maintenance_cost.setValue(printer.get("monthly_maintenance", 0))
        self.printer_price.setValue(printer.get("printer_price", 0))
        self.lifespan_prints.setValue(printer.get("lifespan_prints", 1))

    def calculate(self):
        try:
            filament_cost = calculate_filament_cost(
                self.part_weight.value(), 
                self.spool_weight.value(), 
                self.spool_price.value()
            )
            
            energy_cost = calculate_energy_cost(
                self.power_consumption.value(), 
                self.print_time.value(), 
                self.energy_rate.value()
            )
            
            labor_cost = calculate_labor_cost(
                self.hourly_rate.value(), 
                self.prep_time.value()
            )
            
            maintenance_cost = calculate_maintenance_cost(
                self.maintenance_cost.value(), 
                self.monthly_prints.value()
            )
            
            amortization_cost = calculate_amortization(
                self.printer_price.value(), 
                self.lifespan_prints.value()
            )
            
            total_cost = calculate_total_cost(
                filament_cost, energy_cost, labor_cost, 
                maintenance_cost, amortization_cost, 
                self.additional_costs.value()
            )
            
            suggested_price = suggest_price(total_cost, self.profit_margin.value())
            
            self.current_result = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "filament_cost": filament_cost,
                "energy_cost": energy_cost,
                "labor_cost": labor_cost,
                "maintenance_cost": maintenance_cost,
                "amortization_cost": amortization_cost,
                "additional_costs": self.additional_costs.value(),
                "total_cost": total_cost,
                "suggested_price": suggested_price,
                "part_weight": self.part_weight.value(),
                "print_time": self.print_time.value()
            }
            
            result_text = f"""
            <h3>Resultados do Cálculo</h3>
            <p><b>Custo de Filamento:</b> R$ {filament_cost:.2f}</p>
            <p><b>Custo de Energia:</b> R$ {energy_cost:.2f}</p>
            <p><b>Mão de Obra:</b> R$ {labor_cost:.2f}</p>
            <p><b>Manutenção:</b> R$ {maintenance_cost:.2f}</p>
            <p><b>Amortização:</b> R$ {amortization_cost:.2f}</p>
            <p><b>Adicionais:</b> R$ {self.additional_costs.value():.2f}</p>
            <hr>
            <p style='font-size: 16px'><b>Custo Total:</b> R$ {total_cost:.2f}</p>
            <p style='font-size: 18px; color: #4caf50'><b>Preço Sugerido:</b> R$ {suggested_price:.2f}</p>
            """
            
            self.results_label.setText(result_text)
            self.save_btn.setEnabled(True)
            
        except Exception as e:
            QMessageBox.critical(self, "Erro", str(e))

    def save_result(self):
        if self.current_result:
            save_history(self.current_result)
            QMessageBox.information(self, "Sucesso", "Cálculo salvo no histórico!")
            self.save_btn.setEnabled(False)
