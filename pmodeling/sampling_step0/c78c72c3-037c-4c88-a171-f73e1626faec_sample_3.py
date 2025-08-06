from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
system_build = Transition(label='System Build')
install_sensors = Transition(label='Install Sensors')
set_controls = Transition(label='Set Controls')
test_modules = Transition(label='Test Modules')
select_crops = Transition(label='Select Crops')
configure_irrigation = Transition(label='Configure Irrigation')
deploy_ai = Transition(label='Deploy AI')
monitor_pests = Transition(label='Monitor Pests')
manage_energy = Transition(label='Manage Energy')
recycle_waste = Transition(label='Recycle Waste')
train_staff = Transition(label='Train Staff')
launch_market = Transition(label='Launch Market')
engage_community = Transition(label='Engage Community')

# Define the transitions
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
system_build = Transition(label='System Build')
install_sensors = Transition(label='Install Sensors')
set_controls = Transition(label='Set Controls')
test_modules = Transition(label='Test Modules')
select_crops = Transition(label='Select Crops')
configure_irrigation = Transition(label='Configure Irrigation')
deploy_ai = Transition(label='Deploy AI')
monitor_pests = Transition(label='Monitor Pests')
manage_energy = Transition(label='Manage Energy')
recycle_waste = Transition(label='Recycle Waste')
train_staff = Transition(label='Train Staff')
launch_market = Transition(label='Launch Market')
engage_community = Transition(label='Engage Community')

# Define the loop for building the system
loop = OperatorPOWL(operator=Operator.LOOP, children=[system_build, install_sensors, set_controls, test_modules])

# Define the choice for selecting crops
xor = OperatorPOWL(operator=Operator.XOR, children=[select_crops, train_staff])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[loop, xor, deploy_ai, monitor_pests, manage_energy, recycle_waste, launch_market, engage_community])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, deploy_ai)
root.order.add_edge(xor, monitor_pests)
root.order.add_edge(xor, manage_energy)
root.order.add_edge(xor, recycle_waste)
root.order.add_edge(xor, launch_market)
root.order.add_edge(xor, engage_community)

print(root)