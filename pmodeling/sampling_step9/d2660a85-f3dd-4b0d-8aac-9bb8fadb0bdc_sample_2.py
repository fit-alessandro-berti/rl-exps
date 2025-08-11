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

# Define exclusive choice (XOR) for staff training
xor = OperatorPOWL(operator=Operator.XOR, children=[train_staff, skip])

# Define loops for cultivation, pest management, and harvesting
loop_cultivation = OperatorPOWL(operator=Operator.LOOP, children=[start_cultivation, monitor_growth])
loop_pest_management = OperatorPOWL(operator=Operator.LOOP, children=[manage_pests, skip])
loop_harvesting = OperatorPOWL(operator=Operator.LOOP, children=[harvest_crops, pack_produce])

# Define the POWL model
root = StrictPartialOrder(nodes=[site_survey, design_layout, install_modules, set_controls, select_crops, configure_irrigation, setup_lighting, deploy_sensors, xor, loop_cultivation, loop_pest_management, loop_harvesting, distribute_goods])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, install_modules)
root.order.add_edge(install_modules, set_controls)
root.order.add_edge(set_controls, select_crops)
root.order.add_edge(select_crops, configure_irrigation)
root.order.add_edge(configure_irrigation, setup_lighting)
root.order.add_edge(setup_lighting, deploy_sensors)
root.order.add_edge(deploy_sensors, xor)
root.order.add_edge(xor, loop_cultivation)
root.order.add_edge(loop_cultivation, loop_pest_management)
root.order.add_edge(loop_pest_management, loop_harvesting)
root.order.add_edge(loop_harvesting, distribute_goods)