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

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[install_modules, calibrate_climate])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[prepare_nutrients, select_seeds])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[start_germination, deploy_sensors])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, manage_pests])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[schedule_harvest, process_waste])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[optimize_energy, conduct_training])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[update_records, review_performance])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)

# Print the root
print(root)