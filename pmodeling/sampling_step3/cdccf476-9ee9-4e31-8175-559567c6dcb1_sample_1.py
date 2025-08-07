import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
MilkSourcing = Transition(label='Milk Sourcing')
CurdFormation = Transition(label='Curd Formation')
MicrobialTest = Transition(label='Microbial Test')
WheyRemoval = Transition(label='Whey Removal')
PressingCheese = Transition(label='Pressing Cheese')
SaltApplication = Transition(label='Salt Application')
AgingControl = Transition(label='Aging Control')
QualityCheck = Transition(label='Quality Check')
EcoPackaging = Transition(label='Eco Packaging')
InventoryLog = Transition(label='Inventory Log')
TempMonitoring = Transition(label='Temp Monitoring')
CarrierBooking = Transition(label='Carrier Booking')
TraceRecording = Transition(label='Trace Recording')
FeedbackReview = Transition(label='Feedback Review')
ComplianceAudit = Transition(label='Compliance Audit')
BatchAdjustment = Transition(label='Batch Adjustment')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(nodes=[
    MilkSourcing,
    CurdFormation,
    MicrobialTest,
    WheyRemoval,
    PressingCheese,
    SaltApplication,
    AgingControl,
    QualityCheck,
    EcoPackaging,
    InventoryLog,
    TempMonitoring,
    CarrierBooking,
    TraceRecording,
    FeedbackReview,
    ComplianceAudit,
    BatchAdjustment
])

# Define the order of activities
root.order.add_edge(MilkSourcing, CurdFormation)
root.order.add_edge(CurdFormation, MicrobialTest)
root.order.add_edge(MicrobialTest, WheyRemoval)
root.order.add_edge(WheyRemoval, PressingCheese)
root.order.add_edge(PressingCheese, SaltApplication)
root.order.add_edge(SaltApplication, AgingControl)
root.order.add_edge(AgingControl, QualityCheck)
root.order.add_edge(QualityCheck, EcoPackaging)
root.order.add_edge(EcoPackaging, InventoryLog)
root.order.add_edge(InventoryLog, TempMonitoring)
root.order.add_edge(TempMonitoring, CarrierBooking)
root.order.add_edge(CarrierBooking, TraceRecording)
root.order.add_edge(TraceRecording, FeedbackReview)
root.order.add_edge(FeedbackReview, ComplianceAudit)
root.order.add_edge(ComplianceAudit, BatchAdjustment)

print(root)