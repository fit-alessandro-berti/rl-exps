import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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
Skip = SilentTransition()

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[Return_Request, Authorization_Check, Pickup_Schedule])
loop_transport = OperatorPOWL(operator=Operator.LOOP, children=[Transport_Dispatch, Receiving_Goods, Quality_Inspect, Sort_Items])
loop_refurbish = OperatorPOWL(operator=Operator.LOOP, children=[Refurbish_Prep, Recycle_Process])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Inventory_Update, Customer_Notify, Disposal_Arrange])
loop_audit = OperatorPOWL(operator=Operator.LOOP, children=[Compliance_Audit, Cost_Analysis, Report_Generate])

# Define root POWL model
root = StrictPartialOrder(nodes=[xor, loop_transport, loop_refurbish, xor2, loop_audit])
root.order.add_edge(xor, loop_transport)
root.order.add_edge(loop_transport, loop_refurbish)
root.order.add_edge(loop_refurbish, xor2)
root.order.add_edge(xor2, loop_audit)