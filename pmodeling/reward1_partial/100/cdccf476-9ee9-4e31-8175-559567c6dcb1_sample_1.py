import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the nodes and their relationships
loop = OperatorPOWL(operator=Operator.LOOP, children=[MilkSourcing, CurdFormation, MicrobialTest, WheyRemoval, PressingCheese, SaltApplication, AgingControl, QualityCheck])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[InventoryLog, TempMonitoring])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[CarrierBooking, EcoPackaging])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[TraceRecording, FeedbackReview])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ComplianceAudit, BatchAdjustment])

# Connect the nodes in the partial order
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4])
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)

# Print the root
print(root)