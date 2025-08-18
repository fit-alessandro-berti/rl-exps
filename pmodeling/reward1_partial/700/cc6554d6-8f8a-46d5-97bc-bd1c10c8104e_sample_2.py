import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Demand_Forecast = Transition(label='Demand Forecast')
Risk_Assess = Transition(label='Risk Assess')
Supplier_Audit = Transition(label='Supplier Audit')
Inventory_Scan = Transition(label='Inventory Scan')
Route_Optimize = Transition(label='Route Optimize')
Order_Prioritize = Transition(label='Order Prioritize')
Contract_Review = Transition(label='Contract Review')
Delay_Monitor = Transition(label='Delay Monitor')
Shipment_Reroute = Transition(label='Shipment Reroute')
Cost_Analyze = Transition(label='Cost Analyze')
Compliance_Check = Transition(label='Compliance Check')
Alternative_Engage = Transition(label='Alternative Engage')
Inventory_Reallocate = Transition(label='Inventory Reallocate')
Performance_Track = Transition(label='Performance Track')
Feedback_Loop = Transition(label='Feedback Loop')
Strategy_Update = Transition(label='Strategy Update')

# Define the control flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[Route_Optimize, Order_Prioritize])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Contract_Review, Delay_Monitor])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Cost_Analyze, Compliance_Check])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Alternative_Engage, Inventory_Reallocate])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Performance_Track, Feedback_Loop])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Strategy_Update, Inventory_Scan])

# Define the loop node
loop = OperatorPOWL(operator=Operator.LOOP, children=[Demand_Forecast, Risk_Assess, Supplier_Audit])

# Define the root node
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, loop)

# Print the root node
print(root)