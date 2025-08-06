import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
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

# Define silent transitions for the loop and XOR operations
skip1 = SilentTransition()
skip2 = SilentTransition()

# Define the loop operation (A, B) where A is Site Select and Env Assess, B is Software Dev
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_select, env_assess])

# Define the XOR operation (A, B) where A is Hydroponics Setup and B is Skip
xor1 = OperatorPOWL(operator=Operator.XOR, children=[hydroponics_setup, skip1])

# Define the loop operation (A, B) where A is Seed Choose and B is LED Install
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[seed_choose, led_install])

# Define the XOR operation (A, B) where A is Train Staff and B is Compliance Check
xor2 = OperatorPOWL(operator=Operator.XOR, children=[train_staff, compliance_check])

# Define the loop operation (A, B) where A is Engage Community and B is Skip
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[engage_community, skip2])

# Define the XOR operation (A, B) where A is Plant Crops and B is Skip
xor3 = OperatorPOWL(operator=Operator.XOR, children=[plant_crops, skip2])

# Define the loop operation (A, B) where A is Monitor Growth and B is Skip
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[monitor_growth, skip2])

# Define the XOR operation (A, B) where A is Optimize Yields and B is Skip
xor4 = OperatorPOWL(operator=Operator.XOR, children=[optimize_yields, skip2])

# Define the loop operation (A, B) where A is Waste Manage and B is Skip
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[waste_manage, skip2])

# Define the XOR operation (A, B) where A is Energy Audit and B is Skip
xor5 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip2])

# Define the loop operation (A, B) where A is Water Recycle and B is Skip
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[water_recycle, skip2])

# Define the root partial order
root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, loop3, xor3, loop4, xor4, loop5, xor5, loop6])

# Add dependencies between nodes
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, loop3)
root.order.add_edge(loop3, xor3)
root.order.add_edge(xor3, loop4)
root.order.add_edge(loop4, xor4)
root.order.add_edge(xor4, loop5)
root.order.add_edge(loop5, xor5)
root.order.add_edge(xor5, loop6)
root.order.add_edge(loop6, skip2)  # Add the last loop dependency to the silent transition

print(root)