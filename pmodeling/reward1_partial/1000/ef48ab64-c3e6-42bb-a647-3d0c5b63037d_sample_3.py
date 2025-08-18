import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
site_select = Transition(label='Site Select')
env_assess = Transition(label='Env Assess')
design_modules = Transition(label='Design Modules')
hydroponics_setup = Transition(label='Hydroponics Setup')
software_dev = Transition(label='Software Dev')
seed_choose = Transition(label='Seed Choose')
led_install = Transition(label='LED Install')
train_staff = Transition(label='Train Staff')
compliance_check = Transition(label='Compliance Check')
engage_community = Transition(label='Engage Community')
plant_crops = Transition(label='Plant Crops')
monitor_growth = Transition(label='Monitor Growth')
optimize_yields = Transition(label='Optimize Yields')
waste_manage = Transition(label='Waste Manage')
energy_audit = Transition(label='Energy Audit')
water_recycle = Transition(label='Water Recycle')

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, energy_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[water_recycle, optimize_yields])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[train_staff, engage_community])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[plant_crops, monitor_growth])

# Define the POWL root
root = StrictPartialOrder(nodes=[site_select, env_assess, design_modules, hydroponics_setup, software_dev, seed_choose, led_install, xor3, xor4, xor2, xor])
root.order.add_edge(site_select, env_assess)
root.order.add_edge(env_assess, design_modules)
root.order.add_edge(design_modules, hydroponics_setup)
root.order.add_edge(hydroponics_setup, software_dev)
root.order.add_edge(software_dev, seed_choose)
root.order.add_edge(seed_choose, led_install)
root.order.add_edge(led_install, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor2)
root.order.add_edge(xor2, xor)
root.order.add_edge(xor, None)