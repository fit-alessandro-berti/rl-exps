import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
modular_build = Transition(label='Modular Build')
install_pumps = Transition(label='Install Pumps')
setup_sensors = Transition(label='Setup Sensors')
calibrate_lights = Transition(label='Calibrate Lights')
nutrient_mix = Transition(label='Nutrient Mix')
plant_seeding = Transition(label='Plant Seeding')
water_cycling = Transition(label='Water Cycling')
energy_audit = Transition(label='Energy Audit')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
data_analysis = Transition(label='Data Analysis')
yield_forecast = Transition(label='Yield Forecast')
supply_order = Transition(label='Supply Order')
waste_recycle = Transition(label='Waste Recycle')
system_upgrade = Transition(label='System Upgrade')

skip = SilentTransition()

# Site Survey and Design Layout
site_design = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])

# Modular Build
modular_loop = OperatorPOWL(operator=Operator.LOOP, children=[modular_build, skip])

# Install Pumps, Setup Sensors, Calibrate Lights, Nutrient Mix, Plant Seeding
pump_sensor_light_mixing = OperatorPOWL(operator=Operator.XOR, children=[install_pumps, setup_sensors, calibrate_lights, nutrient_mix, plant_seeding])

# Water Cycling
water_cycling_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_cycling, skip])

# Energy Audit, Pest Control, Growth Monitor
energy_pest_growth = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, pest_control, growth_monitor])

# Data Analysis, Yield Forecast, Supply Order, Waste Recycle
data_analysis_forecast_order_recycle = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, yield_forecast, supply_order, waste_recycle])

# System Upgrade
system_upgrade_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_upgrade, skip])

root = StrictPartialOrder(nodes=[site_design, modular_loop, pump_sensor_light_mixing, water_cycling_loop, energy_pest_growth, data_analysis_forecast_order_recycle, system_upgrade_loop])
root.order.add_edge(site_design, modular_loop)
root.order.add_edge(modular_loop, pump_sensor_light_mixing)
root.order.add_edge(pump_sensor_light_mixing, water_cycling_loop)
root.order.add_edge(water_cycling_loop, energy_pest_growth)
root.order.add_edge(energy_pest_growth, data_analysis_forecast_order_recycle)
root.order.add_edge(data_analysis_forecast_order_recycle, system_upgrade_loop)
root.order.add_edge(system_upgrade_loop, modular_loop)