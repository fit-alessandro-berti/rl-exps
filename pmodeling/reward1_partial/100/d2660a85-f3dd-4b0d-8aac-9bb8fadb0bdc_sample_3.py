import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
install_modules = Transition(label='Install Modules')
set_controls = Transition(label='Set Controls')
select_crops = Transition(label='Select Crops')
configure_irrigation = Transition(label='Configure Irrigation')
setup_lighting = Transition(label='Setup Lighting')
deploy_sensors = Transition(label='Deploy Sensors')
train_staff = Transition(label='Train Staff')
start_cultivation = Transition(label='Start Cultivation')
monitor_growth = Transition(label='Monitor Growth')
manage_pests = Transition(label='Manage Pests')
harvest_crops = Transition(label='Harvest Crops')
pack_produce = Transition(label='Pack Produce')
distribute_goods = Transition(label='Distribute Goods')

# Define the process model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[start_cultivation, monitor_growth])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[manage_pests])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[select_crops, configure_irrigation, setup_lighting, deploy_sensors])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[train_staff])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[harvest_crops, pack_produce, distribute_goods])

root = StrictPartialOrder(nodes=[site_survey, design_layout, install_modules, set_controls, xor1, loop1, xor2, xor3])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, install_modules)
root.order.add_edge(install_modules, set_controls)
root.order.add_edge(set_controls, xor1)
root.order.add_edge(xor1, loop1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, loop1)

print(root)