import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

DiscoverItem = Transition(label='Discover Item')
DocumentFind = Transition(label='Document Find')
InitialSurvey = Transition(label='Initial Survey')
ImageCapture = Transition(label='Image Capture')
MaterialTesting = Transition(label='Material Testing')
StyleCompare = Transition(label='Style Compare')
ExpertConsult = Transition(label='Expert Consult')
ProvenanceCheck = Transition(label='Provenance Check')
OwnershipVerify = Transition(label='Ownership Verify')
LegalReview = Transition(label='Legal Review')
RiskAssess = Transition(label='Risk Assess')
ConservationPlan = Transition(label='Conservation Plan')
Certification = Transition(label='Certification')
SecureTransfer = Transition(label='Secure Transfer')
DisputeResolve = Transition(label='Dispute Resolve')
FinalArchive = Transition(label='Final Archive')
skip = SilentTransition()

# Initial steps
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[DiscoverItem, DocumentFind])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[InitialSurvey, skip])
root = StrictPartialOrder(nodes=[loop1, xor1])
root.order.add_edge(loop1, xor1)

# Image capture and material testing
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ImageCapture, MaterialTesting])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[StyleCompare, skip])
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop2, xor2)

# Expert consultation and provenance check
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[ExpertConsult, ProvenanceCheck])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[OwnershipVerify, skip])
root.order.add_edge(xor2, loop3)
root.order.add_edge(loop3, xor3)

# Legal review and risk assessment
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[LegalReview, RiskAssess])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ConservationPlan, skip])
root.order.add_edge(xor3, loop4)
root.order.add_edge(loop4, xor4)

# Certification and secure transfer
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Certification, SecureTransfer])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[DisputeResolve, skip])
root.order.add_edge(xor4, loop5)
root.order.add_edge(loop5, xor5)

# Final archive
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[FinalArchive, skip])
root.order.add_edge(xor5, loop6)
root.order.add_edge(loop6, xor5)

print(root)