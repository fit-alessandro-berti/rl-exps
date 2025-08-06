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

# Define the control flow
site_survey_to_design_layout = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
design_layout_to_install_modules = OperatorPOWL(operator=Operator.XOR, children=[design_layout, install_modules])
install_modules_to_set_controls = OperatorPOWL(operator=Operator.XOR, children=[install_modules, set_controls])
set_controls_to_select_crops = OperatorPOWL(operator=Operator.XOR, children=[set_controls, select_crops])
select_crops_to_configure_irrigation = OperatorPOWL(operator=Operator.XOR, children=[select_crops, configure_irrigation])
configure_irrigation_to_setup_lighting = OperatorPOWL(operator=Operator.XOR, children=[configure_irrigation, setup_lighting])
setup_lighting_to_deploy_sensors = OperatorPOWL(operator=Operator.XOR, children=[setup_lighting, deploy_sensors])
deploy_sensors_to_train_staff = OperatorPOWL(operator=Operator.XOR, children=[deploy_sensors, train_staff])
train_staff_to_start_cultivation = OperatorPOWL(operator=Operator.XOR, children=[train_staff, start_cultivation])
start_cultivation_to_monitor_growth = OperatorPOWL(operator=Operator.XOR, children=[start_cultivation, monitor_growth])
monitor_growth_to_manage_pests = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, manage_pests])
manage_pests_to_harvest_crops = OperatorPOWL(operator=Operator.XOR, children=[manage_pests, harvest_crops])
harvest_crops_to_pack_produce = OperatorPOWL(operator=Operator.XOR, children=[harvest_crops, pack_produce])
pack_produce_to_distribute_goods = OperatorPOWL(operator=Operator.XOR, children=[pack_produce, distribute_goods])

# Define the root
root = StrictPartialOrder(nodes=[site_survey_to_design_layout, design_layout_to_install_modules, install_modules_to_set_controls, set_controls_to_select_crops, select_crops_to_configure_irrigation, configure_irrigation_to_setup_lighting, setup_lighting_to_deploy_sensors, deploy_sensors_to_train_staff, train_staff_to_start_cultivation, start_cultivation_to_monitor_growth, monitor_growth_to_manage_pests, manage_pests_to_harvest_crops, harvest_crops_to_pack_produce, pack_produce_to_distribute_goods])
root.order.add_edge(site_survey_to_design_layout, design_layout_to_install_modules)
root.order.add_edge(design_layout_to_install_modules, install_modules_to_set_controls)
root.order.add_edge(install_modules_to_set_controls, set_controls_to_select_crops)
root.order.add_edge(set_controls_to_select_crops, select_crops_to_configure_irrigation)
root.order.add_edge(select_crops_to_configure_irrigation, configure_irrigation_to_setup_lighting)
root.order.add_edge(configure_irrigation_to_setup_lighting, setup_lighting_to_deploy_sensors)
root.order.add_edge(setup_lighting_to_deploy_sensors, deploy_sensors_to_train_staff)
root.order.add_edge(deploy_sensors_to_train_staff, train_staff_to_start_cultivation)
root.order.add_edge(train_staff_to_start_cultivation, start_cultivation_to_monitor_growth)
root.order.add_edge(start_cultivation_to_monitor_growth, monitor_growth_to_manage_pests)
root.order.add_edge(monitor_growth_to_manage_pests, manage_pests_to_harvest_crops)
root.order.add_edge(manage_pests_to_harvest_crops, harvest_crops_to_pack_produce)
root.order.add_edge(harvest_crops_to_pack_produce, pack_produce_to_distribute_goods)

print(root)