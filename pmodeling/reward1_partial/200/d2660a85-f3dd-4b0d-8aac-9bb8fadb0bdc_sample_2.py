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

# Define silent transitions
skip = SilentTransition()

# Define the process flow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, design_layout, install_modules, set_controls])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[select_crops, configure_irrigation, setup_lighting, deploy_sensors])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[train_staff, start_cultivation, monitor_growth])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[manage_pests, harvest_crops, pack_produce])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[distribute_goods])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)

# Print the root of the POWL model
print(root)