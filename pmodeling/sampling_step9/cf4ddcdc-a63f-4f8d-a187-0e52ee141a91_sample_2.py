import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the process flow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Pickup_Schedule, Transport_Dispatch, Receiving_Goods, Quality_Inspect])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Sort_Items, Refurbish_Prep, Recycle_Process])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Inventory_Update, Customer_Notify, Disposal_Arrange])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Compliance_Audit, Cost_Analysis, Report_Generate])

# Create the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)

print(root)