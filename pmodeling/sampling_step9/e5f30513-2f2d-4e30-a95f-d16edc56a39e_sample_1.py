import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[MaterialTesting, RadiocarbonDate, StylisticAssess])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, ExpertConsult])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[FindingsCompile, InternalReview])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[ClientPresent, ApprovalConfirm])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[SecurePackage, TransportArrange])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[ChainCustody, xor4])

root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor)