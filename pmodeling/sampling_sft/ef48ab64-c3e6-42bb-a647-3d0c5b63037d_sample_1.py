import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
site_select    = Transition(label='Site Select')
env_assess     = Transition(label='Env Assess')
design_modules = Transition(label='Design Modules')
hydro_setup    = Transition(label='Hydroponics Setup')
software_dev   = Transition(label='Software Dev')
seed_choose    = Transition(label='Seed Choose')
led_install    = Transition(label='LED Install')
train_staff    = Transition(label='Train Staff')
compliance_chk = Transition(label='Compliance Check')
engage_comm    = Transition(label='Engage Community')
plant_crops    = Transition(label='Plant Crops')
monitor_growth = Transition(label='Monitor Growth')
optimize_ylds  = Transition(label='Optimize Yields')
waste_manage   = Transition(label='Waste Manage')
energy_audit   = Transition(label='Energy Audit')
water_recycle  = Transition(label='Water Recycle')

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_select, env_assess,
    design_modules, hydro_setup,
    software_dev, seed_choose, led_install,
    train_staff, compliance_chk, engage_comm,
    plant_crops, monitor_growth,
    optimize_ylds, waste_manage,
    energy_audit, water_recycle
])

# Define the control-flow dependencies
root.order.add_edge(site_select, env_assess)
root.order.add_edge(env_assess, design_modules)
root.order.add_edge(env_assess, hydro_setup)

root.order.add_edge(design_modules, software_dev)
root.order.add_edge(design_modules, seed_choose)
root.order.add_edge(design_modules, led_install)

root.order.add_edge(hydro_setup, software_dev)

root.order.add_edge(software_dev, train_staff)
root.order.add_edge(software_dev, compliance_chk)
root.order.add_edge(software_dev, engage_comm)

root.order.add_edge(train_staff, plant_crops)
root.order.add_edge(compliance_chk, plant_crops)
root.order.add_edge(engage_comm, plant_crops)

# Concurrent growth monitoring and optimization
root.order.add_edge(plant_crops, monitor_growth)
root.order.add_edge(plant_crops, optimize_ylds)

# Concurrency of waste management and energy audit
root.order.add_edge(monitor_growth, waste_manage)
root.order.add_edge(monitor_growth, energy_audit)

# Concurrency of water recycling and waste management
root.order.add_edge(waste_manage, water_recycle)

# Final concurrent execution
root.order.add_edge(optimize_ylds, water_recycle)