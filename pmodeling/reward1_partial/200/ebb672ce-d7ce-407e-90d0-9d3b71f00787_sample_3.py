import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
activities = ['Site Survey', 'Design Layout', 'Modular Build', 'Install Pumps', 'Setup Sensors', 'Calibrate Lights', 'Nutrient Mix', 'Plant Seeding', 'Water Cycling', 'Energy Audit', 'Pest Control', 'Growth Monitor', 'Data Analysis', 'Yield Forecast', 'Supply Order', 'Waste Recycle', 'System Upgrade']
transitions = [Transition(label=activity) for activity in activities]

# Define process structure
site_survey = transitions[0]
design_layout = transitions[1]
modular_build = transitions[2]
install_pumps = transitions[3]
setup_sensors = transitions[4]
calibrate_lights = transitions[5]
nutrient_mix = transitions[6]
plant_seeding = transitions[7]
water_cycling = transitions[8]
energy_audit = transitions[9]
pest_control = transitions[10]
growth_monitor = transitions[11]
data_analysis = transitions[12]
yield_forecast = transitions[13]
supply_order = transitions[14]
waste_recycle = transitions[15]
system_upgrade = transitions[16]

# Define control flow
site_survey -> design_layout
design_layout -> modular_build
modular_build -> install_pumps
install_pumps -> setup_sensors
setup_sensors -> calibrate_lights
calibrate_lights -> nutrient_mix
nutrient_mix -> plant_seeding
plant_seeding -> water_cycling
water_cycling -> energy_audit
energy_audit -> pest_control
pest_control -> growth_monitor
growth_monitor -> data_analysis
data_analysis -> yield_forecast
yield_forecast -> supply_order
supply_order -> waste_recycle
waste_recycle -> system_upgrade

# Create the root node
root = StrictPartialOrder(nodes=[site_survey, design_layout, modular_build, install_pumps, setup_sensors, calibrate_lights, nutrient_mix, plant_seeding, water_cycling, energy_audit, pest_control, growth_monitor, data_analysis, yield_forecast, supply_order, waste_recycle, system_upgrade])