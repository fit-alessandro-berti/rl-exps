from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

site_survey_to_design = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
design_to_install = OperatorPOWL(operator=Operator.XOR, children=[design_layout, install_modules])
install_to_set_controls = OperatorPOWL(operator=Operator.XOR, children=[install_modules, set_controls])
set_to_select = OperatorPOWL(operator=Operator.XOR, children=[set_controls, select_crops])
select_to_configure = OperatorPOWL(operator=Operator.XOR, children=[select_crops, configure_irrigation])
configure_to_setup = OperatorPOWL(operator=Operator.XOR, children=[configure_irrigation, setup_lighting])
setup_to_deploy = OperatorPOWL(operator=Operator.XOR, children=[setup_lighting, deploy_sensors])
deploy_to_train = OperatorPOWL(operator=Operator.XOR, children=[deploy_sensors, train_staff])
train_to_start = OperatorPOWL(operator=Operator.XOR, children=[train_staff, start_cultivation])
start_to_monitor = OperatorPOWL(operator=Operator.XOR, children=[start_cultivation, monitor_growth])
monitor_to_manage = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, manage_pests])
manage_to_harvest = OperatorPOWL(operator=Operator.XOR, children=[manage_pests, harvest_crops])
harvest_to_pack = OperatorPOWL(operator=Operator.XOR, children=[harvest_crops, pack_produce])
pack_to_distribute = OperatorPOWL(operator=Operator.XOR, children=[pack_produce, distribute_goods])

root = StrictPartialOrder(nodes=[
    site_survey, design_layout, install_modules, set_controls, select_crops,
    configure_irrigation, setup_lighting, deploy_sensors, train_staff,
    start_cultivation, monitor_growth, manage_pests, harvest_crops, pack_produce,
    distribute_goods
])
root.order.add_edge(site_survey, design_to_install)
root.order.add_edge(design_to_install, install_to_set_controls)
root.order.add_edge(install_to_set_controls, set_to_select)
root.order.add_edge(set_to_select, select_to_configure)
root.order.add_edge(select_to_configure, configure_to_setup)
root.order.add_edge(configure_to_setup, setup_to_deploy)
root.order.add_edge(setup_to_deploy, deploy_to_train)
root.order.add_edge(deploy_to_train, train_to_start)
root.order.add_edge(train_to_start, start_to_monitor)
root.order.add_edge(start_to_monitor, monitor_to_manage)
root.order.add_edge(monitor_to_manage, manage_to_harvest)
root.order.add_edge(manage_to_harvest, harvest_to_pack)
root.order.add_edge(harvest_to_pack, pack_to_distribute)

print(root)