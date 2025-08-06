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

# Define the process tree
site_survey_transition = OperatorPOWL(operator=Operator.LOOP, children=[site_survey])
design_layout_transition = OperatorPOWL(operator=Operator.LOOP, children=[design_layout])
system_build_transition = OperatorPOWL(operator=Operator.LOOP, children=[system_build])
install_sensors_transition = OperatorPOWL(operator=Operator.LOOP, children=[install_sensors])
set_controls_transition = OperatorPOWL(operator=Operator.LOOP, children=[set_controls])
test_modules_transition = OperatorPOWL(operator=Operator.LOOP, children=[test_modules])
select_crops_transition = OperatorPOWL(operator=Operator.LOOP, children=[select_crops])
configure_irrigation_transition = OperatorPOWL(operator=Operator.LOOP, children=[configure_irrigation])
deploy_ai_transition = OperatorPOWL(operator=Operator.LOOP, children=[deploy_ai])
monitor_pests_transition = OperatorPOWL(operator=Operator.LOOP, children=[monitor_pests])
manage_energy_transition = OperatorPOWL(operator=Operator.LOOP, children=[manage_energy])
recycle_waste_transition = OperatorPOWL(operator=Operator.LOOP, children=[recycle_waste])
train_staff_transition = OperatorPOWL(operator=Operator.LOOP, children=[train_staff])
launch_market_transition = OperatorPOWL(operator=Operator.LOOP, children=[launch_market])
engage_community_transition = OperatorPOWL(operator=Operator.LOOP, children=[engage_community])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey_transition, design_layout_transition, system_build_transition, install_sensors_transition, set_controls_transition, test_modules_transition, select_crops_transition, configure_irrigation_transition, deploy_ai_transition, monitor_pests_transition, manage_energy_transition, recycle_waste_transition, train_staff_transition, launch_market_transition, engage_community_transition])

# Add dependencies
root.order.add_edge(site_survey_transition, design_layout_transition)
root.order.add_edge(design_layout_transition, system_build_transition)
root.order.add_edge(system_build_transition, install_sensors_transition)
root.order.add_edge(install_sensors_transition, set_controls_transition)
root.order.add_edge(set_controls_transition, test_modules_transition)
root.order.add_edge(test_modules_transition, select_crops_transition)
root.order.add_edge(select_crops_transition, configure_irrigation_transition)
root.order.add_edge(configure_irrigation_transition, deploy_ai_transition)
root.order.add_edge(deploy_ai_transition, monitor_pests_transition)
root.order.add_edge(monitor_pests_transition, manage_energy_transition)
root.order.add_edge(manage_energy_transition, recycle_waste_transition)
root.order.add_edge(recycle_waste_transition, train_staff_transition)
root.order.add_edge(train_staff_transition, launch_market_transition)
root.order.add_edge(launch_market_transition, engage_community_transition)

print(root)