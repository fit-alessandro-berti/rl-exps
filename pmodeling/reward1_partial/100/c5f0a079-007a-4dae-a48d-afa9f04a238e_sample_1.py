import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
ProvenanceCheck = Transition(label='Provenance Check')
MaterialScan = Transition(label='Material Scan')
WearAnalysis = Transition(label='Wear Analysis')
ImageCapture = Transition(label='Image Capture')
PatternMatch = Transition(label='Pattern Match')
OwnershipVerify = Transition(label='Ownership Verify')
EthicsReview = Transition(label='Ethics Review')
CarbonDating = Transition(label='Carbon Dating')
RestorationEval = Transition(label='Restoration Eval')
ReportDraft = Transition(label='Report Draft')
StakeholderReview = Transition(label='Stakeholder Review')
ArchiveData = Transition(label='Archive Data')
ExhibitApprove = Transition(label='Exhibit Approve')
ConditionMonitor = Transition(label='Condition Monitor')
FinalCertification = Transition(label='Final Certification')

# Define silent transitions
skip = SilentTransition()

# Define the workflow model
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    ProvenanceCheck, MaterialScan, WearAnalysis, ImageCapture, PatternMatch, OwnershipVerify, EthicsReview, CarbonDating, RestorationEval
])

xor = OperatorPOWL(operator=Operator.XOR, children=[
    skip, ReportDraft
])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the root node to verify the model
print(root)