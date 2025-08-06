from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
loop = OperatorPOWL(operator=Operator.LOOP, children=[start_germination, schedule_harvest, manage_pests])
xor = OperatorPOWL(operator=Operator.XOR, children=[deploy_sensors, monitor_growth])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[select_seeds, site_survey])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[design_layout, install_modules])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[calibrate_climate, prepare_nutrients])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[process_waste, optimize_energy])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[conduct_training, update_records])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[review_performance, conduct_training])

# Define the partial order
root = StrictPartialOrder(nodes=[xor2, xor3, xor4, xor5, xor6, xor7, loop, xor])
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, loop)
root.order.add_edge(loop, xor)

# Print the root
print(root)