import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with their labels
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

# Define the POWL model structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[IntakeReview, PreliminaryInspect, ProvenanceCheck])
xor = OperatorPOWL(operator=Operator.XOR, children=[ArchivalResearch, MaterialTesting, RadiocarbonDate, StylisticAssess, ExpertConsult])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[FindingsCompile, InternalReview, ClientPresent, ApprovalConfirm])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[SecurePackage, TransportArrange, ChainCustody])

# Construct the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)