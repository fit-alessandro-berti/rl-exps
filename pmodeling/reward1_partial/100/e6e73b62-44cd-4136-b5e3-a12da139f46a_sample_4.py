from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the loop for nutrient solution calibration and setup sensors
loop_nutrients_sensors = OperatorPOWL(operator=Operator.LOOP, children=[calibrate_nutrients, setup_sensors])

# Define the loop for pest control and manage lighting
loop_pest_control_lighting = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, manage_lighting])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[site_survey, design_layout, procure_modules, install_framework, loop_nutrients_sensors, setup_sensors, plant_seeding, monitor_growth, loop_pest_control_lighting, harvest_crops, distribute_produce])

# Define the order dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, procure_modules)
root.order.add_edge(procure_modules, install_framework)
root.order.add_edge(install_framework, loop_nutrients_sensors)
root.order.add_edge(loop_nutrients_sensors, setup_sensors)
root.order.add_edge(setup_sensors, plant_seeding)
root.order.add_edge(plant_seeding, monitor_growth)
root.order.add_edge(monitor_growth, loop_pest_control_lighting)
root.order.add_edge(loop_pest_control_lighting, harvest_crops)
root.order.add_edge(harvest_crops, distribute_produce)

print(root)