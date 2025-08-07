import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_select     = Transition(label='Site Select')
env_assess      = Transition(label='Env Assess')
design_modules  = Transition(label='Design Modules')
hydroponics     = Transition(label='Hydroponics Setup')
software_dev    = Transition(label='Software Dev')
seed_choose     = Transition(label='Seed Choose')
led_install     = Transition(label='LED Install')
train_staff     = Transition(label='Train Staff')
compliance_check= Transition(label='Compliance Check')
engage_community= Transition(label='Engage Community')
plant_crops     = Transition(label='Plant Crops')
monitor_growth  = Transition(label='Monitor Growth')
optimize_yields = Transition(label='Optimize Yields')
waste_manage    = Transition(label='Waste Manage')
energy_audit    = Transition(label='Energy Audit')
water_recycle   = Transition(label='Water Recycle')

# Loop for continuous monitoring & optimization
loop = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, optimize_yields])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_select, env_assess, design_modules, hydroponics,
    software_dev, seed_choose, led_install, train_staff,
    compliance_check, engage_community, plant_crops,
    loop, waste_manage, energy_audit, water_recycle
])

# Define the control-flow dependencies
root.order.add_edge(site_select, env_assess)
root.order.add_edge(env_assess, design_modules)
root.order.add_edge(design_modules, hydroponics)
root.order.add_edge(hydroponics, software_dev)
root.order.add_edge(software_dev, seed_choose)
root.order.add_edge(seed_choose, led_install)
root.order.add_edge(led_install, train_staff)
root.order.add_edge(train_staff, compliance_check)
root.order.add_edge(compliance_check, engage_community)
root.order.add_edge(engage_community, plant_crops)
root.order.add_edge(plant_crops, loop)
root.order.add_edge(loop, waste_manage)
root.order.add_edge(loop, energy_audit)
root.order.add_edge(loop, water_recycle)