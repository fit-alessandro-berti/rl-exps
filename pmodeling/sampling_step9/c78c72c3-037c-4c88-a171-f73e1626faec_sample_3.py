import pm4py
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

# Define the silent activities
skip = SilentTransition()

# Define the loops
loop_site_survey = OperatorPOWL(operator=Operator.LOOP, children=[site_survey])
loop_design_layout = OperatorPOWL(operator=Operator.LOOP, children=[design_layout])
loop_system_build = OperatorPOWL(operator=Operator.LOOP, children=[system_build])
loop_install_sensors = OperatorPOWL(operator=Operator.LOOP, children=[install_sensors])
loop_set_controls = OperatorPOWL(operator=Operator.LOOP, children=[set_controls])
loop_test_modules = OperatorPOWL(operator=Operator.LOOP, children=[test_modules])
loop_select_crops = OperatorPOWL(operator=Operator.LOOP, children=[select_crops])
loop_configure_irrigation = OperatorPOWL(operator=Operator.LOOP, children=[configure_irrigation])
loop_deploy_ai = OperatorPOWL(operator=Operator.LOOP, children=[deploy_ai])
loop_monitor_pests = OperatorPOWL(operator=Operator.LOOP, children=[monitor_pests])
loop_manage_energy = OperatorPOWL(operator=Operator.LOOP, children=[manage_energy])
loop_recycle_waste = OperatorPOWL(operator=Operator.LOOP, children=[recycle_waste])
loop_train_staff = OperatorPOWL(operator=Operator.LOOP, children=[train_staff])
loop_launch_market = OperatorPOWL(operator=Operator.LOOP, children=[launch_market])
loop_engage_community = OperatorPOWL(operator=Operator.LOOP, children=[engage_community])

# Define the partial order
root = StrictPartialOrder(nodes=[
    loop_site_survey,
    loop_design_layout,
    loop_system_build,
    loop_install_sensors,
    loop_set_controls,
    loop_test_modules,
    loop_select_crops,
    loop_configure_irrigation,
    loop_deploy_ai,
    loop_monitor_pests,
    loop_manage_energy,
    loop_recycle_waste,
    loop_train_staff,
    loop_launch_market,
    loop_engage_community
])

# Define the order
root.order.add_edge(loop_site_survey, loop_design_layout)
root.order.add_edge(loop_design_layout, loop_system_build)
root.order.add_edge(loop_system_build, loop_install_sensors)
root.order.add_edge(loop_install_sensors, loop_set_controls)
root.order.add_edge(loop_set_controls, loop_test_modules)
root.order.add_edge(loop_test_modules, loop_select_crops)
root.order.add_edge(loop_select_crops, loop_configure_irrigation)
root.order.add_edge(loop_configure_irrigation, loop_deploy_ai)
root.order.add_edge(loop_deploy_ai, loop_monitor_pests)
root.order.add_edge(loop_monitor_pests, loop_manage_energy)
root.order.add_edge(loop_manage_energy, loop_recycle_waste)
root.order.add_edge(loop_recycle_waste, loop_train_staff)
root.order.add_edge(loop_train_staff, loop_launch_market)
root.order.add_edge(loop_launch_market, loop_engage_community)

print(root)