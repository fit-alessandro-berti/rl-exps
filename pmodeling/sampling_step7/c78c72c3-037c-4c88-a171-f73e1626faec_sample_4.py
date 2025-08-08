from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the partial order of the process
root = StrictPartialOrder(nodes=[
    site_survey,
    design_layout,
    system_build,
    install_sensors,
    set_controls,
    test_modules,
    select_crops,
    configure_irrigation,
    deploy_ai,
    monitor_pests,
    manage_energy,
    recycle_waste,
    train_staff,
    launch_market,
    engage_community
])

# Define the order of dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, system_build)
root.order.add_edge(system_build, install_sensors)
root.order.add_edge(install_sensors, set_controls)
root.order.add_edge(set_controls, test_modules)
root.order.add_edge(test_modules, select_crops)
root.order.add_edge(select_crops, configure_irrigation)
root.order.add_edge(configure_irrigation, deploy_ai)
root.order.add_edge(deploy_ai, monitor_pests)
root.order.add_edge(monitor_pests, manage_energy)
root.order.add_edge(manage_energy, recycle_waste)
root.order.add_edge(recycle_waste, train_staff)
root.order.add_edge(train_staff, launch_market)
root.order.add_edge(launch_market, engage_community)

# Print the final POWL model
print(root)