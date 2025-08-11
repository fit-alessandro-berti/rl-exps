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

# Define silent transitions for the process
skip = SilentTransition()

# Define exclusive choice nodes for parallel activities
parallelAnalysis = OperatorPOWL(operator=Operator.XOR, children=[MaterialTesting, RadiocarbonDate])
parallelStyleAssess = OperatorPOWL(operator=Operator.XOR, children=[StylisticAssess, ExpertConsult])

# Define loop nodes for the provenance check process
provenanceLoop = OperatorPOWL(operator=Operator.LOOP, children=[ProvenanceCheck, skip])

# Define the root node of the POWL model
root = StrictPartialOrder(nodes=[IntakeReview, PreliminaryInspect, provenanceLoop, parallelAnalysis, parallelStyleAssess, FindingsCompile, InternalReview, ClientPresent, ApprovalConfirm, SecurePackage, TransportArrange, ChainCustody])
root.order.add_edge(IntakeReview, PreliminaryInspect)
root.order.add_edge(PreliminaryInspect, provenanceLoop)
root.order.add_edge(provenanceLoop, parallelAnalysis)
root.order.add_edge(parallelAnalysis, parallelStyleAssess)
root.order.add_edge(parallelStyleAssess, FindingsCompile)
root.order.add_edge(FindingsCompile, InternalReview)
root.order.add_edge(InternalReview, ClientPresent)
root.order.add_edge(ClientPresent, ApprovalConfirm)
root.order.add_edge(ApprovalConfirm, SecurePackage)
root.order.add_edge(SecurePackage, TransportArrange)
root.order.add_edge(TransportArrange, ChainCustody)

# Print the root of the POWL model
print(root)