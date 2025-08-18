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

# Site Survey --> Design Layout
site_survey_to_design_layout = OperatorPOWL(operator=Operator.PO, children=[site_survey, design_layout])

# Design Layout --> Modular Build
design_layout_to_modular_build = OperatorPOWL(operator=Operator.PO, children=[design_layout, modular_build])

# Modular Build --> Install Pumps
modular_build_to_install_pumps = OperatorPOWL(operator=Operator.PO, children=[modular_build, install_pumps])

# Install Pumps --> Setup Sensors
install_pumps_to_setup_sensors = OperatorPOWL(operator=Operator.PO, children=[install_pumps, setup_sensors])

# Setup Sensors --> Calibrate Lights
setup_sensors_to_calibrate_lights = OperatorPOWL(operator=Operator.PO, children=[setup_sensors, calibrate_lights])

# Calibrate Lights --> Nutrient Mix
calibrate_lights_to_nutrient_mix = OperatorPOWL(operator=Operator.PO, children=[calibrate_lights, nutrient_mix])

# Nutrient Mix --> Plant Seeding
nutrient_mix_to_plant_seeding = OperatorPOWL(operator=Operator.PO, children=[nutrient_mix, plant_seeding])

# Plant Seeding --> Water Cycling
plant_seeding_to_water_cycling = OperatorPOWL(operator=Operator.PO, children=[plant_seeding, water_cycling])

# Water Cycling --> Energy Audit
water_cycling_to_energy_audit = OperatorPOWL(operator=Operator.PO, children=[water_cycling, energy_audit])

# Energy Audit --> Pest Control
energy_audit_to_pest_control = OperatorPOWL(operator=Operator.PO, children=[energy_audit, pest_control])

# Pest Control --> Growth Monitor
pest_control_to_growth_monitor = OperatorPOWL(operator=Operator.PO, children=[pest_control, growth_monitor])

# Growth Monitor --> Data Analysis
growth_monitor_to_data_analysis = OperatorPOWL(operator=Operator.PO, children=[growth_monitor, data_analysis])

# Data Analysis --> Yield Forecast
data_analysis_to_yield_forecast = OperatorPOWL(operator=Operator.PO, children=[data_analysis, yield_forecast])

# Yield Forecast --> Supply Order
yield_forecast_to_supply_order = OperatorPOWL(operator=Operator.PO, children=[yield_forecast, supply_order])

# Supply Order --> Waste Recycle
supply_order_to_waste_recycle = OperatorPOWL(operator=Operator.PO, children=[supply_order, waste_recycle])

# Waste Recycle --> System Upgrade
waste_recycle_to_system_upgrade = OperatorPOWL(operator=Operator.PO, children=[waste_recycle, system_upgrade])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    site_survey_to_design_layout,
    design_layout_to_modular_build,
    modular_build_to_install_pumps,
    install_pumps_to_setup_sensors,
    setup_sensors_to_calibrate_lights,
    calibrate_lights_to_nutrient_mix,
    nutrient_mix_to_plant_seeding,
    plant_seeding_to_water_cycling,
    water_cycling_to_energy_audit,
    energy_audit_to_pest_control,
    pest_control_to_growth_monitor,
    growth_monitor_to_data_analysis,
    data_analysis_to_yield_forecast,
    yield_forecast_to_supply_order,
    supply_order_to_waste_recycle,
    waste_recycle_to_system_upgrade
])

# Add edges to establish the partial order
root.order.add_edge(site_survey_to_design_layout, design_layout_to_modular_build)
root.order.add_edge(design_layout_to_modular_build, modular_build_to_install_pumps)
root.order.add_edge(modular_build_to_install_pumps, install_pumps_to_setup_sensors)
root.order.add_edge(install_pumps_to_setup_sensors, setup_sensors_to_calibrate_lights)
root.order.add_edge(setup_sensors_to_calibrate_lights, calibrate_lights_to_nutrient_mix)
root.order.add_edge(calibrate_lights_to_nutrient_mix, nutrient_mix_to_plant_seeding)
root.order.add_edge(nutrient_mix_to_plant_seeding, plant_seeding_to_water_cycling)
root.order.add_edge(plant_seeding_to_water_cycling, water_cycling_to_energy_audit)
root.order.add_edge(water_cycling_to_energy_audit, energy_audit_to_pest_control)
root.order.add_edge(energy_audit_to_pest_control, pest_control_to_growth_monitor)
root.order.add_edge(pest_control_to_growth_monitor, growth_monitor_to_data_analysis)
root.order.add_edge(growth_monitor_to_data_analysis, data_analysis_to_yield_forecast)
root.order.add_edge(data_analysis_to_yield_forecast, yield_forecast_to_supply_order)
root.order.add_edge(yield_forecast_to_supply_order, supply_order_to_waste_recycle)
root.order.add_edge(supply_order_to_waste_recycle, waste_recycle_to_system_upgrade)