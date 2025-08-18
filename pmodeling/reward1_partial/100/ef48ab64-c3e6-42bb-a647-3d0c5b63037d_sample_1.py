import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
Site_Select = Transition(label='Site Select')
Env_Assess = Transition(label='Env Assess')
Design_Modules = Transition(label='Design Modules')
Hydroponics_Setup = Transition(label='Hydroponics Setup')
Software_Dev = Transition(label='Software Dev')
Seed_Choose = Transition(label='Seed Choose')
LED_Install = Transition(label='LED Install')
Train_Staff = Transition(label='Train Staff')
Compliance_Check = Transition(label='Compliance Check')
Engage_Community = Transition(label='Engage Community')
Plant_Crops = Transition(label='Plant Crops')
Monitor_Growth = Transition(label='Monitor Growth')
Optimize_Yields = Transition(label='Optimize Yields')
Waste_Manage = Transition(label='Waste Manage')
Energy_Audit = Transition(label='Energy Audit')
Water_Recycle = Transition(label='Water Recycle')

# Define silent transitions for concurrency
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()
skip5 = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Site_Select, Env_Assess])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Design_Modules, Hydroponics_Setup])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Software_Dev, Seed_Choose])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[LED_Install, Train_Staff])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Compliance_Check, Engage_Community])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Plant_Crops, Monitor_Growth])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[Optimize_Yields, Waste_Manage])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[Energy_Audit, Water_Recycle])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, skip1)
root.order.add_edge(loop8, skip2)
root.order.add_edge(loop8, skip3)
root.order.add_edge(loop8, skip4)
root.order.add_edge(loop8, skip5)

# Print the root POWL model
print(root)