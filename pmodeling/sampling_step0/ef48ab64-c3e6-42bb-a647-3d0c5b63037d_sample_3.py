import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[software_dev, software_dev])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[seed_choose, seed_choose])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[led_install, led_install])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[train_staff, train_staff])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, compliance_check])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[engage_community, engage_community])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[plant_crops, plant_crops])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, monitor_growth])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[optimize_yields, optimize_yields])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, waste_manage])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, energy_audit])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[water_recycle, water_recycle])

# Define the loop for automation software development
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[software_dev, software_dev])

# Define the loop for seed selection
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[seed_choose, seed_choose])

# Define the loop for LED installation
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[led_install, led_install])

# Define the loop for workforce training
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[train_staff, train_staff])

# Define the loop for regulatory compliance checks
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, compliance_check])

# Define the loop for community engagement programs
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[engage_community, engage_community])

# Define the loop for phased crop planting
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[plant_crops, plant_crops])

# Define the loop for real-time monitoring setup
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, monitor_growth])

# Define the loop for optimization cycles
loop9 = OperatorPOWL(operator=Operator.LOOP, children=[optimize_yields, optimize_yields])

# Define the loop for waste management
loop10 = OperatorPOWL(operator=Operator.LOOP, children=[waste_manage, waste_manage])

# Define the loop for energy audit
loop11 = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, energy_audit])

# Define the loop for water recycling
loop12 = OperatorPOWL(operator=Operator.LOOP, children=[water_recycle, water_recycle])

# Define the root POWL model
root = StrictPartialOrder(nodes=[site_select, env_assess, design_modules, hydroponics_setup, loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8, loop9, loop10, loop11, loop12, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, xor11, xor12])
root.order.add_edge(site_select, env_assess)
root.order.add_edge(env_assess, design_modules)
root.order.add_edge(design_modules, hydroponics_setup)
root.order.add_edge(hydroponics_setup, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, loop9)
root.order.add_edge(loop9, loop10)
root.order.add_edge(loop10, loop11)
root.order.add_edge(loop11, loop12)
root.order.add_edge(loop12, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, xor11)
root.order.add_edge(xor11, xor12)
root.order.add_edge(xor12, plant_crops)
root.order.add_edge(plant_crops, monitor_growth)
root.order.add_edge(monitor_growth, optimize_yields)
root.order.add_edge(optimize_yields, waste_manage)
root.order.add_edge(waste_manage, energy_audit)
root.order.add_edge(energy_audit, water_recycle)
root.order.add_edge(water_recycle, root)