import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Return_Request = Transition(label='Return Request')
Authorization_Check = Transition(label='Authorization Check')
Pickup_Schedule = Transition(label='Pickup Schedule')
Transport_Dispatch = Transition(label='Transport Dispatch')
Receiving_Goods = Transition(label='Receiving Goods')
Quality_Inspect = Transition(label='Quality Inspect')
Sort_Items = Transition(label='Sort Items')
Refurbish_Prep = Transition(label='Refurbish Prep')
Recycle_Process = Transition(label='Recycle Process')
Inventory_Update = Transition(label='Inventory Update')
Customer_Notify = Transition(label='Customer Notify')
Disposal_Arrange = Transition(label='Disposal Arrange')
Compliance_Audit = Transition(label='Compliance Audit')
Cost_Analysis = Transition(label='Cost Analysis')
Report_Generate = Transition(label='Report Generate')

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Authorization_Check, Pickup_Schedule])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Transport_Dispatch, Receiving_Goods])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Quality_Inspect, Sort_Items])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Refurbish_Prep, Recycle_Process])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Inventory_Update, Customer_Notify])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Disposal_Arrange, Compliance_Audit])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[Cost_Analysis, Report_Generate])

# Define the partial order
root = StrictPartialOrder(nodes=[Return_Request, xor1, xor2, xor3, xor4, xor5, xor6, xor7])

# Add the dependencies
root.order.add_edge(Return_Request, xor1)
root.order.add_edge(Return_Request, xor2)
root.order.add_edge(Return_Request, xor3)
root.order.add_edge(Return_Request, xor4)
root.order.add_edge(Return_Request, xor5)
root.order.add_edge(Return_Request, xor6)
root.order.add_edge(Return_Request, xor7)

# Print the final result
print(root)