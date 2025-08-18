import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for loop nodes
silent_transition = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[start_cultivation, monitor_growth, manage_pests, harvest_crops])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[pack_produce, distribute_goods])
xor = OperatorPOWL(operator=Operator.XOR, children=[silent_transition, loop1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[silent_transition, loop2])
root = StrictPartialOrder(nodes=[site_survey, design_layout, install_modules, set_controls, select_crops, configure_irrigation, setup_lighting, deploy_sensors, train_staff, xor, xor2])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, install_modules)
root.order.add_edge(install_modules, set_controls)
root.order.add_edge(set_controls, select_crops)
root.order.add_edge(select_crops, configure_irrigation)
root.order.add_edge(configure_irrigation, setup_lighting)
root.order.add_edge(setup_lighting, deploy_sensors)
root.order.add_edge(deploy_sensors, train_staff)
root.order.add_edge(train_staff, xor)
root.order.add_edge(xor, loop1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(xor2, loop2)
root.order.add_edge(loop2, distribute_goods)
root.order.add_edge(distribute_goods, pack_produce)
root.order.add_edge(pack_produce, distribute_goods)