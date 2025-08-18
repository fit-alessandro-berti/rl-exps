import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) for the POWL model
ReturnRequest = Transition(label='Return Request')
AuthorizationCheck = Transition(label='Authorization Check')
PickupSchedule = Transition(label='Pickup Schedule')
TransportDispatch = Transition(label='Transport Dispatch')
ReceivingGoods = Transition(label='Receiving Goods')
QualityInspect = Transition(label='Quality Inspect')
SortItems = Transition(label='Sort Items')
RefurbishPrep = Transition(label='Refurbish Prep')
RecycleProcess = Transition(label='Recycle Process')
InventoryUpdate = Transition(label='Inventory Update')
CustomerNotify = Transition(label='Customer Notify')
DisposalArrange = Transition(label='Disposal Arrange')
ComplianceAudit = Transition(label='Compliance Audit')
CostAnalysis = Transition(label='Cost Analysis')
ReportGenerate = Transition(label='Report Generate')

# Create the POWL model
root = StrictPartialOrder(nodes=[
    ReturnRequest, AuthorizationCheck, PickupSchedule, TransportDispatch, 
    ReceivingGoods, QualityInspect, SortItems, RefurbishPrep, RecycleProcess, 
    InventoryUpdate, CustomerNotify, DisposalArrange, ComplianceAudit, 
    CostAnalysis, ReportGenerate
])

# Define the dependencies (partial order) between the transitions
root.order.add_edge(ReturnRequest, AuthorizationCheck)
root.order.add_edge(AuthorizationCheck, PickupSchedule)
root.order.add_edge(PickupSchedule, TransportDispatch)
root.order.add_edge(TransportDispatch, ReceivingGoods)
root.order.add_edge(ReceivingGoods, QualityInspect)
root.order.add_edge(QualityInspect, SortItems)
root.order.add_edge(SortItems, RefurbishPrep)
root.order.add_edge(RefurbishPrep, RecycleProcess)
root.order.add_edge(RecycleProcess, InventoryUpdate)
root.order.add_edge(InventoryUpdate, CustomerNotify)
root.order.add_edge(CustomerNotify, DisposalArrange)
root.order.add_edge(DisposalArrange, ComplianceAudit)
root.order.add_edge(ComplianceAudit, CostAnalysis)
root.order.add_edge(CostAnalysis, ReportGenerate)

print(root)