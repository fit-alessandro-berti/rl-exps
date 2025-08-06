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

# Define silent transitions (for concurrency)
skip = SilentTransition()

# Define loop for cultivation and pest management
loop_cultivation = OperatorPOWL(operator=Operator.LOOP, children=[start_cultivation, monitor_growth])
loop_pest_management = OperatorPOWL(operator=Operator.LOOP, children=[manage_pests])

# Define exclusive choice for select crops and configure irrigation
xor_select_crops = OperatorPOWL(operator=Operator.XOR, children=[select_crops, configure_irrigation])

# Define exclusive choice for training staff and start cultivation
xor_train_staff = OperatorPOWL(operator=Operator.XOR, children=[train_staff, start_cultivation])

# Define exclusive choice for setup lighting and deploy sensors
xor_setup_lighting = OperatorPOWL(operator=Operator.XOR, children=[setup_lighting, deploy_sensors])

# Define exclusive choice for harvest crops and pack produce
xor_harvest_produce = OperatorPOWL(operator=Operator.XOR, children=[harvest_crops, pack_produce])

# Define exclusive choice for packing produce and distributing goods
xor_pack_distribute = OperatorPOWL(operator=Operator.XOR, children=[pack_produce, distribute_goods])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[site_survey, design_layout, install_modules, set_controls, xor_select_crops,
                                  xor_train_staff, xor_setup_lighting, loop_cultivation, loop_pest_management,
                                  xor_harvest_produce, xor_pack_distribute])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, install_modules)
root.order.add_edge(install_modules, set_controls)
root.order.add_edge(set_controls, xor_select_crops)
root.order.add_edge(xor_select_crops, xor_train_staff)
root.order.add_edge(xor_train_staff, xor_setup_lighting)
root.order.add_edge(xor_setup_lighting, loop_cultivation)
root.order.add_edge(loop_cultivation, loop_pest_management)
root.order.add_edge(loop_pest_management, xor_harvest_produce)
root.order.add_edge(xor_harvest_produce, xor_pack_distribute)
root.order.add_edge(xor_pack_distribute, distribute_goods)