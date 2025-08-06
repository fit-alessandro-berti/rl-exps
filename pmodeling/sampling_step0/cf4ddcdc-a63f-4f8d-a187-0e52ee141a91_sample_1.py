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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
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
    ],
    order={
        Return_Request: [Authorization_Check],
        Authorization_Check: [Pickup_Schedule],
        Pickup_Schedule: [Transport_Dispatch],
        Transport_Dispatch: [Receiving_Goods],
        Receiving_Goods: [Quality_Inspect, Sort_Items],
        Quality_Inspect: [Refurbish_Prep, Recycle_Process],
        Sort_Items: [Refurbish_Prep, Recycle_Process],
        Refurbish_Prep: [Inventory_Update],
        Recycle_Process: [Inventory_Update],
        Inventory_Update: [Customer_Notify, Disposal_Arrange],
        Customer_Notify: [Compliance_Audit, Cost_Analysis],
        Disposal_Arrange: [Compliance_Audit, Cost_Analysis],
        Compliance_Audit: [Report_Generate],
        Cost_Analysis: [Report_Generate],
        Report_Generate: []
    }
)

# Print the POWL model
print(root)