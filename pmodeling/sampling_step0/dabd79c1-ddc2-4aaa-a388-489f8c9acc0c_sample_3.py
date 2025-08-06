import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
DocumentReview = Transition(label='Document Review')
MaterialTesting = Transition(label='Material Testing')
RadiocarbonDate = Transition(label='Radiocarbon Date')
StylisticEval = Transition(label='Stylistic Eval')
DatabaseCheck = Transition(label='Database Check')
OwnershipAudit = Transition(label='Ownership Audit')
ExportVerify = Transition(label='Export Verify')
ExpertArbitration = Transition(label='Expert Arbitration')
ConservationPlan = Transition(label='Conservation Plan')
RiskAssessment = Transition(label='Risk Assessment')
ApprovalReview = Transition(label='Approval Review')
InsuranceSetup = Transition(label='Insurance Setup')
SecureTransport = Transition(label='Secure Transport')
AcquisitionsMeet = Transition(label='Acquisitions Meet')
FinalDocumentation = Transition(label='Final Documentation')

# Define silent transitions
skip = SilentTransition()

# Define the workflow
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, ExpertArbitration])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[DatabaseCheck, OwnershipAudit, ExportVerify])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[RiskAssessment, ApprovalReview, InsuranceSetup])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[SecureTransport, AcquisitionsMeet, FinalDocumentation])
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, xor])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)
root.order.add_edge(loop3, xor)

# Print the root
print(root)