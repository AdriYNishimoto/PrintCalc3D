def calculate_filament_cost(part_weight_g, spool_weight_g, spool_price):
    """Calculates the cost of filament used."""
    if spool_weight_g <= 0:
        return 0.0
    return (part_weight_g / spool_weight_g) * spool_price

def calculate_energy_cost(power_consumption_w, print_time_h, energy_rate_kwh):
    """Calculates the energy cost."""
    kwh = (power_consumption_w / 1000) * print_time_h
    return kwh * energy_rate_kwh

def calculate_labor_cost(hourly_rate, prep_time_h):
    """Calculates the labor cost."""
    return hourly_rate * prep_time_h

def calculate_maintenance_cost(monthly_maintenance_cost, monthly_prints_estimate):
    """Calculates maintenance cost per part."""
    if monthly_prints_estimate <= 0:
        return 0.0
    return monthly_maintenance_cost / monthly_prints_estimate

def calculate_amortization(printer_price, lifespan_prints):
    """Calculates amortization cost per part."""
    if lifespan_prints <= 0:
        return 0.0
    return printer_price / lifespan_prints

def calculate_total_cost(filament_cost, energy_cost, labor_cost, maintenance_cost, amortization_cost, additional_costs):
    """Calculates the total cost."""
    return filament_cost + energy_cost + labor_cost + maintenance_cost + amortization_cost + additional_costs

def suggest_price(total_cost, profit_margin_percent):
    """Calculates the suggested selling price."""
    return total_cost * (1 + profit_margin_percent / 100)
