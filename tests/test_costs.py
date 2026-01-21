import unittest
import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.costs import (calculate_filament_cost, calculate_energy_cost, 
                       calculate_labor_cost, calculate_maintenance_cost, 
                       calculate_amortization, calculate_total_cost, suggest_price)

class TestCosts(unittest.TestCase):
    def test_filament_cost(self):
        # 100g part, 1000g spool, $100 price -> $10 cost
        self.assertAlmostEqual(calculate_filament_cost(100, 1000, 100), 10.0)
        
    def test_energy_cost(self):
        # 500W (0.5kW), 10h, $0.80/kWh -> 0.5 * 10 * 0.8 = $4.00
        self.assertAlmostEqual(calculate_energy_cost(500, 10, 0.8), 4.0)
        
    def test_labor_cost(self):
        # $20/h, 0.5h -> $10
        self.assertAlmostEqual(calculate_labor_cost(20, 0.5), 10.0)
        
    def test_maintenance_cost(self):
        # $20 monthly, 20 prints -> $1/print
        self.assertAlmostEqual(calculate_maintenance_cost(20, 20), 1.0)
        
    def test_amortization(self):
        # $2000 printer, 2000 prints lifespan -> $1/print
        self.assertAlmostEqual(calculate_amortization(2000, 2000), 1.0)
        
    def test_total_cost(self):
        self.assertAlmostEqual(calculate_total_cost(10, 4, 10, 1, 1, 5), 31.0)
        
    def test_suggest_price(self):
        # Cost 100, 50% margin -> 150
        self.assertAlmostEqual(suggest_price(100, 50), 150.0)

if __name__ == '__main__':
    unittest.main()
