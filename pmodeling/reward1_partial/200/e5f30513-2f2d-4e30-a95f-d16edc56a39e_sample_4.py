import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
IntakeReview = Transition(label='Intake Review')
PreliminaryInspect = Transition(label='Preliminary Inspect')
ProvenanceCheck = Transition(label='Provenance Check')
ArchivalResearch = Transition(label='Archival Research')
MaterialTesting = Transition(label='Material Testing')
RadiocarbonDate = Transition(label='Radiocarbon Date')
StylisticAssess = Transition(label='Stylistic Assess')
ExpertConsult = Transition(label='Expert Consult')
FindingsCompile = Transition(label='Findings Compile')
InternalReview = Transition(label='Internal Review')
ClientPresent = Transition(label='Client Present')
ApprovalConfirm = Transition(label='Approval Confirm')
SecurePackage = Transition(label='Secure Package')
TransportArrange = Transition(label='Transport Arrange')
ChainCustody = Transition(label='Chain Custody')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
artifactAnalysis = OperatorPOWL(operator=Operator.LOOP, children=[ArchivalResearch, MaterialTesting, RadiocarbonDate, StylisticAssess, ExpertConsult])
findingsCompilation = OperatorPOWL(operator=Operator.LOOP, children=[InternalReview, ClientPresent, ApprovalConfirm])

# Define the root POWL model
root = StrictPartialOrder(nodes=[IntakeReview, PreliminaryInspect, ProvenanceCheck, artifactAnalysis, findingsCompilation, SecurePackage, TransportArrange, ChainCustody])
root.order.add_edge(IntakeReview, PreliminaryInspect)
root.order.add_edge(PreliminaryInspect, ProvenanceCheck)
root.order.add_edge(ProvenanceCheck, artifactAnalysis)
root.order.add_edge(artifactAnalysis, findingsCompilation)
root.order.add_edge(findingsCompilation, SecurePackage)
root.order.add_edge(SecurePackage, TransportArrange)
root.order.add_edge(TransportArrange, ChainCustody)

print(root)