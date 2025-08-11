import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
install_modules = Transition(label='Install Modules')
calibrate_climate = Transition(label='Calibrate Climate')
prepare_nutrients = Transition(label='Prepare Nutrients')
select_seeds = Transition(label='Select Seeds')
start_germination = Transition(label='Start Germination')
deploy_sensors = Transition(label='Deploy Sensors')
monitor_growth = Transition(label='Monitor Growth')
manage_pests = Transition(label='Manage Pests')
schedule_harvest = Transition(label='Schedule Harvest')
process_waste = Transition(label='Process Waste')
optimize_energy = Transition(label='Optimize Energy')
conduct_training = Transition(label='Conduct Training')
update_records = Transition(label='Update Records')
review_performance = Transition(label='Review Performance')

# Define the silent transitions (no actions)
skip = SilentTransition()

# Define the loop nodes
module_installation_loop = OperatorPOWL(operator=Operator.LOOP, children=[install_modules, calibrate_climate, prepare_nutrients])
pest_management_loop = OperatorPOWL(operator=Operator.LOOP, children=[manage_pests, schedule_harvest, process_waste])

# Define the exclusive choice nodes
nutrient_choice = OperatorPOWL(operator=Operator.XOR, children=[prepare_nutrients, skip])
pest_choice = OperatorPOWL(operator=Operator.XOR, children=[manage_pests, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, design_layout, module_installation_loop, nutrient_choice, pest_choice, monitor_growth, deploy_sensors, conduct_training, update_records, review_performance])

# Define the partial order edges
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, module_installation_loop)
root.order.add_edge(module_installation_loop, nutrient_choice)
root.order.add_edge(module_installation_loop, pest_choice)
root.order.add_edge(nutrient_choice, monitor_growth)
root.order.add_edge(pest_choice, monitor_growth)
root.order.add_edge(monitor_growth, deploy_sensors)
root.order.add_edge(deploy_sensors, conduct_training)
root.order.add_edge(conduct_training, update_records)
root.order.add_edge(update_records, review_performance)

print(root)