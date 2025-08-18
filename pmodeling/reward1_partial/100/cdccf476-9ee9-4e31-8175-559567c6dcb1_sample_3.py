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

# Define the partial order nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[AgingControl, TempMonitoring])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ComplianceAudit, FeedbackReview])
xor = OperatorPOWL(operator=Operator.XOR, children=[InventoryLog, CarrierBooking])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[EcoPackaging, BatchAdjustment])

# Define the root node
root = StrictPartialOrder(nodes=[loop1, loop2, xor, xor2])

# Add edges to the partial order
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor, xor2)

# Print the root node
print(root)