import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
procure_modules = Transition(label='Procure Modules')
install_framework = Transition(label='Install Framework')
setup_sensors = Transition(label='Setup Sensors')
calibrate_nutrients = Transition(label='Calibrate Nutrients')
configure_iot = Transition(label='Configure IoT')
plant_seeding = Transition(label='Plant Seeding')
monitor_growth = Transition(label='Monitor Growth')
manage_lighting = Transition(label='Manage Lighting')
pest_control = Transition(label='Pest Control')
recycle_waste = Transition(label='Recycle Waste')
analyze_data = Transition(label='Analyze Data')
adjust_environment = Transition(label='Adjust Environment')
harvest_crops = Transition(label='Harvest Crops')
distribute_produce = Transition(label='Distribute Produce')

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, design_layout, procure_modules, install_framework, setup_sensors, calibrate_nutrients, configure_iot, plant_seeding, monitor_growth, manage_lighting, pest_control, recycle_waste, analyze_data, adjust_environment, harvest_crops, distribute_produce])

# Add dependencies if needed (not explicitly mentioned in the problem description)
# Example: root.order.add_edge(site_survey, design_layout)
# Example: root.order.add_edge(design_layout, procure_modules)
# Example: root.order.add_edge(procure_modules, install_framework)
# Example: root.order.add_edge(install_framework, setup_sensors)
# Example: root.order.add_edge(setup_sensors, calibrate_nutrients)
# Example: root.order.add_edge(calibrate_nutrients, configure_iot)
# Example: root.order.add_edge(configure_iot, plant_seeding)
# Example: root.order.add_edge(plant_seeding, monitor_growth)
# Example: root.order.add_edge(monitor_growth, manage_lighting)
# Example: root.order.add_edge(manage_lighting, pest_control)
# Example: root.order.add_edge(pest_control, recycle_waste)
# Example: root.order.add_edge(recycle_waste, analyze_data)
# Example: root.order.add_edge(analyze_data, adjust_environment)
# Example: root.order.add_edge(adjust_environment, harvest_crops)
# Example: root.order.add_edge(harvest_crops, distribute_produce)

# Print the root POWL model
print(root)