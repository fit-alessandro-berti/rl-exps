import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

ClientMeet = Transition(label='Client Meet')
VisionCapture = Transition(label='Vision Capture')
ConceptDraft = Transition(label='Concept Draft')
FeedbackLoop = OperatorPOWL(operator=Operator.XOR, children=[ConceptDraft, SilentTransition()])
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

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[VisionCapture, ConceptDraft])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[FeedbackLoop, QualityReview, TechnicalCheck, FinalApproval])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[PackagingPrep, LogisticsPlan, SecureTransport, InstallationSet])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[ClientSupport, ArchivalRecord])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop2, loop4)
root.order.add_edge(loop3, loop4)

print(root)