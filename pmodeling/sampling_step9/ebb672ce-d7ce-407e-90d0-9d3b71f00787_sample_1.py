import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop for nutrient cycling
nutrient_cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, skip])

# Define exclusive choice for pest control and waste recycling
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, waste_recycle])

# Define exclusive choice for yield forecast and system upgrade
yield_upgrade_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, system_upgrade])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey, design_layout, modular_build, install_pumps, setup_sensors, calibrate_lights, nutrient_cycle_loop, nutrient_mix, plant_seeding, water_cycling, energy_audit, pest_control_choice, growth_monitor, data_analysis, yield_upgrade_choice, supply_order])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(site_survey, modular_build)
root.order.add_edge(design_layout, modular_build)
root.order.add_edge(modular_build, install_pumps)
root.order.add_edge(modular_build, setup_sensors)
root.order.add_edge(modular_build, calibrate_lights)
root.order.add_edge(modular_build, nutrient_cycle_loop)
root.order.add_edge(modular_build, nutrient_mix)
root.order.add_edge(modular_build, plant_seeding)
root.order.add_edge(modular_build, water_cycling)
root.order.add_edge(modular_build, energy_audit)
root.order.add_edge(modular_build, pest_control_choice)
root.order.add_edge(modular_build, growth_monitor)
root.order.add_edge(modular_build, data_analysis)
root.order.add_edge(modular_build, yield_upgrade_choice)
root.order.add_edge(modular_build, supply_order)
root.order.add_edge(nutrient_cycle_loop, nutrient_mix)
root.order.add_edge(nutrient_cycle_loop, skip)
root.order.add_edge(pest_control_choice, pest_control)
root.order.add_edge(pest_control_choice, waste_recycle)
root.order.add_edge(yield_upgrade_choice, yield_forecast)
root.order.add_edge(yield_upgrade_choice, system_upgrade)

print(root)