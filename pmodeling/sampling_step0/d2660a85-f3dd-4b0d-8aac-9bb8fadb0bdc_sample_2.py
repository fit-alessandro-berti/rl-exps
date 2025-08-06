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

# Define the process structure
loop_cultivation = OperatorPOWL(operator=Operator.LOOP, children=[start_cultivation, monitor_growth, manage_pests])
loop_harvest = OperatorPOWL(operator=Operator.LOOP, children=[harvest_crops, pack_produce, distribute_goods])
xor_initial_setup = OperatorPOWL(operator=Operator.XOR, children=[configure_irrigation, setup_lighting, deploy_sensors])
xor_farm_setup = OperatorPOWL(operator=Operator.XOR, children=[train_staff, select_crops, set_controls])
xor_initial_setup_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_initial_setup, loop_cultivation])
xor_initial_setup_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_initial_setup_loop, loop_harvest])
xor_initial_setup_loop_loop_loop = OperatorPOWL(operator=Operator.XOR, children=[xor_initial_setup_loop_loop, skip])

root = StrictPartialOrder(nodes=[site_survey, design_layout, install_modules, xor_initial_setup_loop_loop_loop])
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, install_modules)
root.order.add_edge(install_modules, xor_initial_setup_loop_loop_loop)

# Print the root node to verify
print(root)