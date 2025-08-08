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

# Define the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    install_modules,
    set_controls,
    select_crops,
    configure_irrigation,
    setup_lighting,
    deploy_sensors,
    train_staff,
    start_cultivation,
    monitor_growth,
    manage_pests,
    harvest_crops,
    pack_produce,
    distribute_goods
])

# Define the dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, install_modules)
root.order.add_edge(install_modules, set_controls)
root.order.add_edge(set_controls, select_crops)
root.order.add_edge(select_crops, configure_irrigation)
root.order.add_edge(configure_irrigation, setup_lighting)
root.order.add_edge(setup_lighting, deploy_sensors)
root.order.add_edge(deploy_sensors, train_staff)
root.order.add_edge(train_staff, start_cultivation)
root.order.add_edge(start_cultivation, monitor_growth)
root.order.add_edge(monitor_growth, manage_pests)
root.order.add_edge(manage_pests, harvest_crops)
root.order.add_edge(harvest_crops, pack_produce)
root.order.add_edge(pack_produce, distribute_goods)