import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order model
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, install_modules, calibrate_climate, prepare_nutrients, select_seeds, start_germination, deploy_sensors, monitor_growth, manage_pests, schedule_harvest, process_waste, optimize_energy, conduct_training, update_records, review_performance
])

# Add dependencies if any (in this case, all activities are independent)
# root.order.add_edge(site_survey, design_layout)
# root.order.add_edge(site_survey, install_modules)
# root.order.add_edge(site_survey, calibrate_climate)
# root.order.add_edge(site_survey, prepare_nutrients)
# root.order.add_edge(site_survey, select_seeds)
# root.order.add_edge(site_survey, start_germination)
# root.order.add_edge(site_survey, deploy_sensors)
# root.order.add_edge(site_survey, monitor_growth)
# root.order.add_edge(site_survey, manage_pests)
# root.order.add_edge(site_survey, schedule_harvest)
# root.order.add_edge(site_survey, process_waste)
# root.order.add_edge(site_survey, optimize_energy)
# root.order.add_edge(site_survey, conduct_training)
# root.order.add_edge(site_survey, update_records)
# root.order.add_edge(site_survey, review_performance)

print(root)