import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
IntakeReview = Transition(label='Intake Review')
VisualInspect = Transition(label='Visual Inspect')
MaterialTest = Transition(label='Material Test')
ProvenanceCheck = Transition(label='Provenance Check')
ArchivalSearch = Transition(label='Archival Search')
ExpertConsult = Transition(label='Expert Consult')
DigitalScan = Transition(label='Digital Scan')
ConditionReport = Transition(label='Condition Report')
ForgeryAssess = Transition(label='Forgery Assess')
LegalReview = Transition(label='Legal Review')
RiskAnalysis = Transition(label='Risk Analysis')
AcquisitionVote = Transition(label='Acquisition Vote')
CatalogEntry = Transition(label='Catalog Entry')
StoragePrep = Transition(label='Storage Prep')
FinalApproval = Transition(label='Final Approval')

# Define the silent transitions
skip = SilentTransition()

# Define the partial order nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[IntakeReview, VisualInspect, MaterialTest, ProvenanceCheck, ArchivalSearch, ExpertConsult, DigitalScan, ConditionReport, ForgingAssess, LegalReview, RiskAnalysis, AcquisitionVote])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, CatalogEntry, StoragePrep, FinalApproval])
root = StrictPartialOrder(nodes=[loop, xor])

# Add the order dependencies
root.order.add_edge(loop, ArchivalSearch)
root.order.add_edge(loop, ExpertConsult)
root.order.add_edge(loop, DigitalScan)
root.order.add_edge(loop, ConditionReport)
root.order.add_edge(loop, ForgingAssess)
root.order.add_edge(loop, LegalReview)
root.order.add_edge(loop, RiskAnalysis)
root.order.add_edge(loop, AcquisitionVote)
root.order.add_edge(loop, CatalogEntry)
root.order.add_edge(loop, StoragePrep)
root.order.add_edge(loop, FinalApproval)

# Print the root POWL model
print(root)