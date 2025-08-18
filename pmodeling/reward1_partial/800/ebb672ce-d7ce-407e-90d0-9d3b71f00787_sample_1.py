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

# Site Survey
site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey])
site_survey_loop.order.add_edge(site_survey, site_survey_loop)

# Design Layout
design_layout_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_layout])
design_layout_loop.order.add_edge(design_layout, design_layout_loop)

# Modular Build
modular_build_loop = OperatorPOWL(operator=Operator.LOOP, children=[modular_build])
modular_build_loop.order.add_edge(modular_build, modular_build_loop)

# Install Pumps
install_pumps_loop = OperatorPOWL(operator=Operator.LOOP, children=[install_pumps])
install_pumps_loop.order.add_edge(install_pumps, install_pumps_loop)

# Setup Sensors
setup_sensors_loop = OperatorPOWL(operator=Operator.LOOP, children=[setup_sensors])
setup_sensors_loop.order.add_edge(setup_sensors, setup_sensors_loop)

# Calibrate Lights
calibrate_lights_loop = OperatorPOWL(operator=Operator.LOOP, children=[calibrate_lights])
calibrate_lights_loop.order.add_edge(calibrate_lights, calibrate_lights_loop)

# Nutrient Mix
nutrient_mix_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix])
nutrient_mix_loop.order.add_edge(nutrient_mix, nutrient_mix_loop)

# Plant Seeding
plant_seeding_loop = OperatorPOWL(operator=Operator.LOOP, children=[plant_seeding])
plant_seeding_loop.order.add_edge(plant_seeding, plant_seeding_loop)

# Water Cycling
water_cycling_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_cycling])
water_cycling_loop.order.add_edge(water_cycling, water_cycling_loop)

# Energy Audit
energy_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit])
energy_audit_loop.order.add_edge(energy_audit, energy_audit_loop)

# Pest Control
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])
pest_control_loop.order.add_edge(pest_control, pest_control_loop)

# Growth Monitor
growth_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor])
growth_monitor_loop.order.add_edge(growth_monitor, growth_monitor_loop)

# Data Analysis
data_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis])
data_analysis_loop.order.add_edge(data_analysis, data_analysis_loop)

# Yield Forecast
yield_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast])
yield_forecast_loop.order.add_edge(yield_forecast, yield_forecast_loop)

# Supply Order
supply_order_loop = OperatorPOWL(operator=Operator.LOOP, children=[supply_order])
supply_order_loop.order.add_edge(supply_order, supply_order_loop)

# Waste Recycle
waste_recycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycle])
waste_recycle_loop.order.add_edge(waste_recycle, waste_recycle_loop)

# System Upgrade
system_upgrade_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_upgrade])
system_upgrade_loop.order.add_edge(system_upgrade, system_upgrade_loop)

root = StrictPartialOrder(nodes=[site_survey_loop, design_layout_loop, modular_build_loop, install_pumps_loop, setup_sensors_loop, calibrate_lights_loop, nutrient_mix_loop, plant_seeding_loop, water_cycling_loop, energy_audit_loop, pest_control_loop, growth_monitor_loop, data_analysis_loop, yield_forecast_loop, supply_order_loop, waste_recycle_loop, system_upgrade_loop])
root.order.add_edge(site_survey_loop, design_layout_loop)
root.order.add_edge(design_layout_loop, modular_build_loop)
root.order.add_edge(modular_build_loop, install_pumps_loop)
root.order.add_edge(install_pumps_loop, setup_sensors_loop)
root.order.add_edge(setup_sensors_loop, calibrate_lights_loop)
root.order.add_edge(calibrate_lights_loop, nutrient_mix_loop)
root.order.add_edge(nutrient_mix_loop, plant_seeding_loop)
root.order.add_edge(plant_seeding_loop, water_cycling_loop)
root.order.add_edge(water_cycling_loop, energy_audit_loop)
root.order.add_edge(energy_audit_loop, pest_control_loop)
root.order.add_edge(pest_control_loop, growth_monitor_loop)
root.order.add_edge(growth_monitor_loop, data_analysis_loop)
root.order.add_edge(data_analysis_loop, yield_forecast_loop)
root.order.add_edge(yield_forecast_loop, supply_order_loop)
root.order.add_edge(supply_order_loop, waste_recycle_loop)
root.order.add_edge(waste_recycle_loop, system_upgrade_loop)