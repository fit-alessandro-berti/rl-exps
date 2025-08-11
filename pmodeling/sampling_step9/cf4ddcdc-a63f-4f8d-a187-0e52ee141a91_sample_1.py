import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Authorization_Check, Pickup_Schedule])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Transport_Dispatch, Receiving_Goods])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Inspect, Sort_Items])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Refurbish_Prep, Recycle_Process])

# Define exclusive choices
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Inventory_Update, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Customer_Notify, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Disposal_Arrange, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Compliance_Audit, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Cost_Analysis, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Report_Generate, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)
root.order.add_edge(loop1, xor5)
root.order.add_edge(loop2, xor6)

print(root)