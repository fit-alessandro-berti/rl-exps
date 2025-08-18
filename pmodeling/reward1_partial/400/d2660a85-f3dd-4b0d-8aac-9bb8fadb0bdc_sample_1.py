import pm4py
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

skip = SilentTransition()

site_survey_xor = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])
install_modules_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, install_modules])
set_controls_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, set_controls])
select_crops_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, select_crops])
configure_irrigation_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, configure_irrigation])
setup_lighting_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, setup_lighting])
deploy_sensors_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, deploy_sensors])
train_staff_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, train_staff])
start_cultivation_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, start_cultivation])
monitor_growth_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, monitor_growth])
manage_pests_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, manage_pests])
harvest_crops_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, harvest_crops])
pack_produce_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, pack_produce])
distribute_goods_xor = OperatorPOWL(operator=Operator.XOR, children=[skip, distribute_goods])

root = StrictPartialOrder(nodes=[
    site_survey, design_layout, install_modules, set_controls, select_crops,
    configure_irrigation, setup_lighting, deploy_sensors, train_staff,
    start_cultivation, monitor_growth, manage_pests, harvest_crops, pack_produce,
    distribute_goods
])
root.order.add_edge(site_survey, site_survey_xor)
root.order.add_edge(site_survey_xor, install_modules_xor)
root.order.add_edge(install_modules_xor, set_controls_xor)
root.order.add_edge(set_controls_xor, select_crops_xor)
root.order.add_edge(select_crops_xor, configure_irrigation_xor)
root.order.add_edge(configure_irrigation_xor, setup_lighting_xor)
root.order.add_edge(setup_lighting_xor, deploy_sensors_xor)
root.order.add_edge(deploy_sensors_xor, train_staff_xor)
root.order.add_edge(train_staff_xor, start_cultivation_xor)
root.order.add_edge(start_cultivation_xor, monitor_growth_xor)
root.order.add_edge(monitor_growth_xor, manage_pests_xor)
root.order.add_edge(manage_pests_xor, harvest_crops_xor)
root.order.add_edge(harvest_crops_xor, pack_produce_xor)
root.order.add_edge(pack_produce_xor, distribute_goods_xor)