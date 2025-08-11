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

skip = SilentTransition()

# Define the process
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Demand_Forecast, Risk_Assess])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Supplier_Audit, Inventory_Scan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Route_Optimize, Order_Prioritize])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Contract_Review, Delay_Monitor])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Shipment_Reroute, Cost_Analyze])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Compliance_Check, Alternative_Engage])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[Inventory_Reallocate, Performance_Track])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[Feedback_Loop, Strategy_Update])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])

# Define the root
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)
root.order.add_edge(loop, xor7)
root.order.add_edge(loop, xor8)

print(root)