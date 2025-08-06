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

# Define the workflow
site_survey_choice = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
procure_modules_choice = OperatorPOWL(operator=Operator.XOR, children=[procure_modules, install_framework])
sensors_choice = OperatorPOWL(operator=Operator.XOR, children=[setup_sensors, calibrate_nutrients])
iot_choice = OperatorPOWL(operator=Operator.XOR, children=[configure_iot, plant_seeding])
monitor_growth_choice = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, manage_lighting])
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, recycle_waste])
data_choice = OperatorPOWL(operator=Operator.XOR, children=[analyze_data, adjust_environment])
harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[harvest_crops, distribute_produce])

# Define the loop for monitoring and adjusting the environment
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth_choice, pest_control_choice, data_choice, adjust_environment])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_survey_choice, procure_modules_choice, sensors_choice, iot_choice, loop, harvest_choice])
root.order.add_edge(site_survey_choice, procure_modules_choice)
root.order.add_edge(procure_modules_choice, install_framework)
root.order.add_edge(install_framework, setup_sensors)
root.order.add_edge(setup_sensors, calibrate_nutrients)
root.order.add_edge(calibrate_nutrients, configure_iot)
root.order.add_edge(configure_iot, plant_seeding)
root.order.add_edge(plant_seeding, monitor_growth_choice)
root.order.add_edge(monitor_growth_choice, pest_control_choice)
root.order.add_edge(pest_control_choice, analyze_data)
root.order.add_edge(analyze_data, adjust_environment)
root.order.add_edge(adjust_environment, harvest_choice)
root.order.add_edge(harvest_choice, distribute_produce)