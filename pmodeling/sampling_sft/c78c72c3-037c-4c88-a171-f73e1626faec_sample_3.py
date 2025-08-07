import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey      = Transition(label='Site Survey')
design_layout    = Transition(label='Design Layout')
system_build     = Transition(label='System Build')
install_sensors  = Transition(label='Install Sensors')
set_controls     = Transition(label='Set Controls')
test_modules     = Transition(label='Test Modules')
select_crops     = Transition(label='Select Crops')
configure_irrig  = Transition(label='Configure Irrigation')
deploy_ai        = Transition(label='Deploy AI')
monitor_pests    = Transition(label='Monitor Pests')
manage_energy    = Transition(label='Manage Energy')
recycle_waste    = Transition(label='Recycle Waste')
train_staff      = Transition(label='Train Staff')
launch_market    = Transition(label='Launch Market')
engage_community = Transition(label='Engage Community')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    site_survey, design_layout, system_build,
    install_sensors, set_controls, test_modules,
    select_crops, configure_irrig, deploy_ai,
    monitor_pests, manage_energy, recycle_waste,
    train_staff, launch_market, engage_community
])

# Define the control‐flow dependencies
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, system_build)

# After system build, concurrent installation and control setup
root.order.add_edge(system_build, install_sensors)
root.order.add_edge(system_build, set_controls)

# Test modules must be done after installation and control setup
root.order.add_edge(install_sensors, test_modules)
root.order.add_edge(set_controls, test_modules)

# Test modules must be done before further steps
root.order.add_edge(test_modules, select_crops)
root.order.add_edge(test_modules, configure_irrig)
root.order.add_edge(test_modules, deploy_ai)

# Select crops and configure irrigation must be done before AI deployment
root.order.add_edge(select_crops, deploy_ai)
root.order.add_edge(configure_irrig, deploy_ai)

# All monitoring, management, and waste‐recycling activities can occur concurrently after deployment
root.order.add_edge(deploy_ai, monitor_pests)
root.order.add_edge(deploy_ai, manage_energy)
root.order.add_edge(deploy_ai, recycle_waste)

# All monitoring, management, and waste‐recycling activities must be done before staff training
root.order.add_edge(monitor_pests, train_staff)
root.order.add_edge(manage_energy, train_staff)
root.order.add_edge(recycle_waste, train_staff)

# Staff training must be done before launching the market
root.order.add_edge(train_staff, launch_market)

# Launch market must be done before engaging the community
root.order.add_edge(launch_market, engage_community)