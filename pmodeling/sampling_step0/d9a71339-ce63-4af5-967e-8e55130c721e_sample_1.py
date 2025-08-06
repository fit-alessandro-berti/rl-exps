import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Structural_Check = Transition(label='Structural Check')
Modular_Install = Transition(label='Modular Install')
Hydroponic_Setup = Transition(label='Hydroponic Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Sensor_Setup = Transition(label='Sensor Setup')
AI_Training = Transition(label='AI Training')
Data_Capture = Transition(label='Data Capture')
Maintenance_Plan = Transition(label='Maintenance Plan')
Pest_Scan = Transition(label='Pest Scan')
Growth_Monitor = Transition(label='Growth Monitor')
Harvest_Sync = Transition(label='Harvest Sync')
Quality_Test = Transition(label='Quality Test')
Package_Prep = Transition(label='Package Prep')
Logistics_Plan = Transition(label='Logistics Plan')

# Define the partial order structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[Site_Survey, Structural_Check, Modular_Install, Hydroponic_Setup, Nutrient_Mix, Sensor_Setup, AI_Training])
xor = OperatorPOWL(operator=Operator.XOR, children=[Data_Capture, Maintenance_Plan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Pest_Scan, Growth_Monitor])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Harvest_Sync, Quality_Test])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Package_Prep, Logistics_Plan])

# Connect the partial order nodes
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)

# Print the root POWL model
print(root)