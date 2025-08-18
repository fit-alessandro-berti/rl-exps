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

# Define the process model
loopMicrobialTest = OperatorPOWL(operator=Operator.LOOP, children=[MicrobialTest])
xorInventoryLog = OperatorPOWL(operator=Operator.XOR, children=[InventoryLog, SilentTransition()])
xorTempMonitoring = OperatorPOWL(operator=Operator.XOR, children=[TempMonitoring, SilentTransition()])
xorCarrierBooking = OperatorPOWL(operator=Operator.XOR, children=[CarrierBooking, SilentTransition()])
xorTraceRecording = OperatorPOWL(operator=Operator.XOR, children=[TraceRecording, SilentTransition()])
xorFeedbackReview = OperatorPOWL(operator=Operator.XOR, children=[FeedbackReview, SilentTransition()])
xorComplianceAudit = OperatorPOWL(operator=Operator.XOR, children=[ComplianceAudit, SilentTransition()])
xorBatchAdjustment = OperatorPOWL(operator=Operator.XOR, children=[BatchAdjustment, SilentTransition()])

# Create the root partial order
root = StrictPartialOrder(nodes=[MilkSourcing, CurdFormation, loopMicrobialTest, WheyRemoval, PressingCheese, SaltApplication, AgingControl, QualityCheck, EcoPackaging, xorInventoryLog, xorTempMonitoring, xorCarrierBooking, xorTraceRecording, xorFeedbackReview, xorComplianceAudit, xorBatchAdjustment])
root.order.add_edge(MilkSourcing, CurdFormation)
root.order.add_edge(CurdFormation, loopMicrobialTest)
root.order.add_edge(loopMicrobialTest, WheyRemoval)
root.order.add_edge(WheyRemoval, PressingCheese)
root.order.add_edge(PressingCheese, SaltApplication)
root.order.add_edge(SaltApplication, AgingControl)
root.order.add_edge(AgingControl, QualityCheck)
root.order.add_edge(QualityCheck, EcoPackaging)
root.order.add_edge(EcoPackaging, xorInventoryLog)
root.order.add_edge(xorInventoryLog, xorTempMonitoring)
root.order.add_edge(xorTempMonitoring, xorCarrierBooking)
root.order.add_edge(xorCarrierBooking, xorTraceRecording)
root.order.add_edge(xorTraceRecording, xorFeedbackReview)
root.order.add_edge(xorFeedbackReview, xorComplianceAudit)
root.order.add_edge(xorComplianceAudit, xorBatchAdjustment)