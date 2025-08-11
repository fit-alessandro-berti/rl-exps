import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Return_Request, Authorization_Check, Pickup_Schedule, Transport_Dispatch, Receiving_Goods, Quality_Inspect, Sort_Items, Refurbish_Prep, Recycle_Process, Inventory_Update, Customer_Notify, Disposal_Arrange, Compliance_Audit, Cost_Analysis, Report_Generate])

xor = OperatorPOWL(operator=Operator.XOR, children=[skip])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)