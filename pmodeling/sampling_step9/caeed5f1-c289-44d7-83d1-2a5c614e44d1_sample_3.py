import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
ClientMeet = Transition(label='Client Meet')
VisionCapture = Transition(label='Vision Capture')
ConceptDraft = Transition(label='Concept Draft')
FeedbackLoop = Transition(label='Feedback Loop')
MaterialSourcing = Transition(label='Material Sourcing')
VendorSelection = Transition(label='Vendor Selection')
ArtisanAssign = Transition(label='Artisan Assign')
PrototypeBuild = Transition(label='Prototype Build')
QualityReview = Transition(label='Quality Review')
TechnicalCheck = Transition(label='Technical Check')
FinalApproval = Transition(label='Final Approval')
PackagingPrep = Transition(label='Packaging Prep')
LogisticsPlan = Transition(label='Logistics Plan')
SecureTransport = Transition(label='Secure Transport')
InstallationSet = Transition(label='Installation Set')
ClientSupport = Transition(label='Client Support')
ArchivalRecord = Transition(label='Archival Record')

# Define silent transitions
skip = SilentTransition()

# Define the workflow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[ConceptDraft, FeedbackLoop])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[MaterialSourcing, VendorSelection])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[ArtisanAssign, PrototypeBuild])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[QualityReview, TechnicalCheck])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[FinalApproval, PackagingPrep])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[LogisticsPlan, SecureTransport])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[InstallationSet, ClientSupport])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[ArchivalRecord, skip])

# Create the root node with all the loops
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)

print(root)