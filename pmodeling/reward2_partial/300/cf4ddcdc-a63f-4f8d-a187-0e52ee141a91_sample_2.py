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

# Define the partial order
root = StrictPartialOrder(nodes=[
    Return_Request,
    Authorization_Check,
    Pickup_Schedule,
    Transport_Dispatch,
    Receiving_Goods,
    Quality_Inspect,
    Sort_Items,
    Refurbish_Prep,
    Recycle_Process,
    Inventory_Update,
    Customer_Notify,
    Disposal_Arrange,
    Compliance_Audit,
    Cost_Analysis,
    Report_Generate
])

# Define the partial order edges
root.order.add_edge(Return_Request, Authorization_Check)
root.order.add_edge(Authorization_Check, Pickup_Schedule)
root.order.add_edge(Pickup_Schedule, Transport_Dispatch)
root.order.add_edge(Transport_Dispatch, Receiving_Goods)
root.order.add_edge(Receiving_Goods, Quality_Inspect)
root.order.add_edge(Quality_Inspect, Sort_Items)
root.order.add_edge(Sort_Items, Refurbish_Prep)
root.order.add_edge(Refurbish_Prep, Recycle_Process)
root.order.add_edge(Recycle_Process, Inventory_Update)
root.order.add_edge(Inventory_Update, Customer_Notify)
root.order.add_edge(Customer_Notify, Disposal_Arrange)
root.order.add_edge(Disposal_Arrange, Compliance_Audit)
root.order.add_edge(Compliance_Audit, Cost_Analysis)
root.order.add_edge(Cost_Analysis, Report_Generate)