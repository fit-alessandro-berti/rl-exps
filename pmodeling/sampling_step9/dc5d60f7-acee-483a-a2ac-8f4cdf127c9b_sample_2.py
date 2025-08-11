import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
IntakeReview = Transition(label='Intake Review')
ConditionScan = Transition(label='Condition Scan')
MaterialTest = Transition(label='Material Test')
StyleMatch = Transition(label='Style Match')
ProvenanceLog = Transition(label='Provenance Log')
ForgeryRisk = Transition(label='Forgery Risk')
LegalAudit = Transition(label='Legal Audit')
ExpertPanel = Transition(label='Expert Panel')
DataCrosscheck = Transition(label='Data Crosscheck')
ReportDraft = Transition(label='Report Draft')
BlockchainTag = Transition(label='Blockchain Tag')
Certification = Transition(label='Certification')
ClientFeedback = Transition(label='Client Feedback')
FinalApproval = Transition(label='Final Approval')
ReleasePrep = Transition(label='Release Prep')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[ForgeryRisk, LegalAudit, ExpertPanel, DataCrosscheck])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ReportDraft, BlockchainTag, Certification])

# Define exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[ClientFeedback, FinalApproval])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ReleasePrep, xor1])

# Define partial order
root = StrictPartialOrder(nodes=[IntakeReview, ConditionScan, MaterialTest, StyleMatch, ProvenanceLog, xor2])
root.order.add_edge(IntakeReview, ConditionScan)
root.order.add_edge(ConditionScan, MaterialTest)
root.order.add_edge(MaterialTest, StyleMatch)
root.order.add_edge(StyleMatch, ProvenanceLog)
root.order.add_edge(ProvenanceLog, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor2)