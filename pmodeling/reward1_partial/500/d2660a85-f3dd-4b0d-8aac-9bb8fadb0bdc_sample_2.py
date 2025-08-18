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

site_survey_choice = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])
design_layout_choice = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])
install_modules_choice = OperatorPOWL(operator=Operator.XOR, children=[install_modules, skip])
set_controls_choice = OperatorPOWL(operator=Operator.XOR, children=[set_controls, skip])
select_crops_choice = OperatorPOWL(operator=Operator.XOR, children=[select_crops, skip])
configure_irrigation_choice = OperatorPOWL(operator=Operator.XOR, children=[configure_irrigation, skip])
setup_lighting_choice = OperatorPOWL(operator=Operator.XOR, children=[setup_lighting, skip])
deploy_sensors_choice = OperatorPOWL(operator=Operator.XOR, children=[deploy_sensors, skip])
train_staff_choice = OperatorPOWL(operator=Operator.XOR, children=[train_staff, skip])
start_cultivation_choice = OperatorPOWL(operator=Operator.XOR, children=[start_cultivation, skip])
monitor_growth_choice = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, skip])
manage_pests_choice = OperatorPOWL(operator=Operator.XOR, children=[manage_pests, skip])
harvest_crops_choice = OperatorPOWL(operator=Operator.XOR, children=[harvest_crops, skip])
pack_produce_choice = OperatorPOWL(operator=Operator.XOR, children=[pack_produce, skip])
distribute_goods_choice = OperatorPOWL(operator=Operator.XOR, children=[distribute_goods, skip])

root = StrictPartialOrder(nodes=[
    site_survey_choice, design_layout_choice, install_modules_choice, set_controls_choice, select_crops_choice,
    configure_irrigation_choice, setup_lighting_choice, deploy_sensors_choice, train_staff_choice,
    start_cultivation_choice, monitor_growth_choice, manage_pests_choice, harvest_crops_choice,
    pack_produce_choice, distribute_goods_choice
])
root.order.add_edge(site_survey_choice, design_layout_choice)
root.order.add_edge(design_layout_choice, install_modules_choice)
root.order.add_edge(install_modules_choice, set_controls_choice)
root.order.add_edge(set_controls_choice, select_crops_choice)
root.order.add_edge(select_crops_choice, configure_irrigation_choice)
root.order.add_edge(configure_irrigation_choice, setup_lighting_choice)
root.order.add_edge(setup_lighting_choice, deploy_sensors_choice)
root.order.add_edge(deploy_sensors_choice, train_staff_choice)
root.order.add_edge(train_staff_choice, start_cultivation_choice)
root.order.add_edge(start_cultivation_choice, monitor_growth_choice)
root.order.add_edge(monitor_growth_choice, manage_pests_choice)
root.order.add_edge(manage_pests_choice, harvest_crops_choice)
root.order.add_edge(harvest_crops_choice, pack_produce_choice)
root.order.add_edge(pack_produce_choice, distribute_goods_choice)