import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
InquiryReview = Transition(label='Inquiry Review')
ClientOnboard = Transition(label='Client Onboard')
ConceptDraft = Transition(label='Concept Draft')
FeedbackCycle = Transition(label='Feedback Cycle')
ContractSetup = Transition(label='Contract Setup')
PaymentSchedule = Transition(label='Payment Schedule')
MaterialSourcing = Transition(label='Material Sourcing')
ArtworkCreate = Transition(label='Artwork Create')
QualityCheck = Transition(label='Quality Check')
FrameSelection = Transition(label='Frame Selection')
PackagingPrep = Transition(label='Packaging Prep')
ShipmentArrange = Transition(label='Shipment Arrange')
DeliveryConfirm = Transition(label='Delivery Confirm')
PostSaleSupport = Transition(label='Post-Sale Support')
RevisionManage = Transition(label='Revision Manage')
DelayMitigate = Transition(label='Delay Mitigate')

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice operators for the feedback cycle
xor1 = OperatorPOWL(operator=Operator.XOR, children=[ConceptDraft, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ContractSetup, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[PaymentSchedule, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[MaterialSourcing, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[ArtworkCreate, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[QualityCheck, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[FrameSelection, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[PackagingPrep, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[ShipmentArrange, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[DeliveryConfirm, skip])

# Define the loop operators for the revision management and delay mitigation
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[RevisionManage])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[DelayMitigate])

# Define the root partial order
root = StrictPartialOrder(nodes=[InquiryReview, ClientOnboard, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, loop1, loop2])
root.order.add_edge(InquiryReview, ClientOnboard)
root.order.add_edge(ClientOnboard, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop1)

# Print the root partial order
print(root)