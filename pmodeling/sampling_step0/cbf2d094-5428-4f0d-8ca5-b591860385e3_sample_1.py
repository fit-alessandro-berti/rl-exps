from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Seed_Select = Transition(label='Seed Select')
Nutrient_Mix = Transition(label='Nutrient Mix')
Climate_Adjust = Transition(label='Climate Adjust')
Planting_Robotic = Transition(label='Planting Robotic')
Growth_Monitor = Transition(label='Growth Monitor')
Pest_Control = Transition(label='Pest Control')
Water_Recycle = Transition(label='Water Recycle')
Light_Optimize = Transition(label='Light Optimize')
Growth_Analyze = Transition(label='Growth Analyze')
Harvest_Sync = Transition(label='Harvest Sync')
Sterilize_Crop = Transition(label='Sterilize Crop')
Package_Fresh = Transition(label='Package Fresh')
Demand_Forecast = Transition(label='Demand Forecast')
Delivery_Plan = Transition(label='Delivery Plan')
Data_Feedback = Transition(label='Data Feedback')

# Define the nodes and their relationships
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Climate_Adjust, Nutrient_Mix])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Planting_Robotic, Growth_Monitor])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Pest_Control, Water_Recycle])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Light_Optimize, Growth_Analyze])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Harvest_Sync, Sterilize_Crop])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Package_Fresh, Demand_Forecast])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Delivery_Plan, Data_Feedback])

# Define the root node
root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, loop3, xor3, loop4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor3)

# Return the root node
return root