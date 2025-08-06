from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[system_build, install_sensors])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[set_controls, test_modules])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[select_crops, configure_irrigation])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[deploy_ai, monitor_pests])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[manage_energy, recycle_waste])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[train_staff, launch_market])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[engage_community, system_build])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])

# Define the root
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)
root.order.add_edge(loop, xor7)
root.order.add_edge(loop, xor8)

print(root)