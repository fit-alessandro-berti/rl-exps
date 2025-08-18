import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names as provided
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, modular_build, install_pumps, setup_sensors, calibrate_lights, nutrient_mix,
    plant_seeding, water_cycling, energy_audit, pest_control, growth_monitor, data_analysis, yield_forecast,
    supply_order, waste_recycle, system_upgrade
])

# Define the dependencies (control flow)
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, modular_build)
root.order.add_edge(modular_build, install_pumps)
root.order.add_edge(install_pumps, setup_sensors)
root.order.add_edge(setup_sensors, calibrate_lights)
root.order.add_edge(calibrate_lights, nutrient_mix)
root.order.add_edge(nutrient_mix, plant_seeding)
root.order.add_edge(plant_seeding, water_cycling)
root.order.add_edge(water_cycling, energy_audit)
root.order.add_edge(energy_audit, pest_control)
root.order.add_edge(pest_control, growth_monitor)
root.order.add_edge(growth_monitor, data_analysis)
root.order.add_edge(data_analysis, yield_forecast)
root.order.add_edge(yield_forecast, supply_order)
root.order.add_edge(supply_order, waste_recycle)
root.order.add_edge(waste_recycle, system_upgrade)

print(root)