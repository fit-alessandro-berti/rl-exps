import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout])
loop_system_build = OperatorPOWL(operator=Operator.LOOP, children=[system_build, install_sensors])
loop_set_controls = OperatorPOWL(operator=Operator.LOOP, children=[set_controls, test_modules])
loop_select_crops = OperatorPOWL(operator=Operator.LOOP, children=[select_crops, configure_irrigation])
loop_deploy_ai = OperatorPOWL(operator=Operator.LOOP, children=[deploy_ai, monitor_pests])
loop_manage_energy = OperatorPOWL(operator=Operator.LOOP, children=[manage_energy, recycle_waste])
loop_train_staff = OperatorPOWL(operator=Operator.LOOP, children=[train_staff, launch_market])
loop_engage_community = OperatorPOWL(operator=Operator.LOOP, children=[engage_community])

# Define exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop_site_survey, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop_system_build, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop_set_controls, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop_select_crops, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop_deploy_ai, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop_manage_energy, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[loop_train_staff, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[loop_engage_community, skip])

# Define root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)