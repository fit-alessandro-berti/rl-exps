import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[MilkSourcing, CurdFormation, MicrobialTest, WheyRemoval, PressingCheese, SaltApplication, AgingControl, QualityCheck])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[EcoPackaging, InventoryLog, TempMonitoring, CarrierBooking, TraceRecording])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[FeedbackReview, ComplianceAudit, BatchAdjustment])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)