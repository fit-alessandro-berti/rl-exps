import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the partial order model
root = StrictPartialOrder(nodes=[DiscoverItem, DocumentFind, InitialSurvey, ImageCapture, MaterialTesting, StyleCompare, ExpertConsult, ProvenanceCheck, OwnershipVerify, LegalReview, RiskAssess, ConservationPlan, Certification, SecureTransfer, DisputeResolve, FinalArchive])

# Define the order dependencies
root.order.add_edge(DiscoverItem, DocumentFind)
root.order.add_edge(DocumentFind, InitialSurvey)
root.order.add_edge(InitialSurvey, ImageCapture)
root.order.add_edge(ImageCapture, MaterialTesting)
root.order.add_edge(MaterialTesting, StyleCompare)
root.order.add_edge(StyleCompare, ExpertConsult)
root.order.add_edge(ExpertConsult, ProvenanceCheck)
root.order.add_edge(ProvenanceCheck, OwnershipVerify)
root.order.add_edge(OwnershipVerify, LegalReview)
root.order.add_edge(LegalReview, RiskAssess)
root.order.add_edge(RiskAssess, ConservationPlan)
root.order.add_edge(ConservationPlan, Certification)
root.order.add_edge(Certification, SecureTransfer)
root.order.add_edge(SecureTransfer, DisputeResolve)
root.order.add_edge(DisputeResolve, FinalArchive)

# Print the root POWL model
print(root)