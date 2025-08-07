import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
SubmitArtifact = Transition(label='Submit Artifact')
InitialReview = Transition(label='Initial Review')
ProvenanceCheck = Transition(label='Provenance Check')
MaterialScan = Transition(label='Material Scan')
ContextAnalysis = Transition(label='Context Analysis')
ExpertPanel = Transition(label='Expert Panel')
DigitalFingerprint = Transition(label='Digital Fingerprint')
AI_Pattern = Transition(label='AI Pattern')
LegalAudit = Transition(label='Legal Audit')
EthicsReview = Transition(label='Ethics Review')
FraudDetection = Transition(label='Fraud Detection')
BlockchainLog = Transition(label='Blockchain Log')
Certification = Transition(label='Certification')
OwnerNotify = Transition(label='Owner Notify')
ArchiveData = Transition(label='Archive Data')
SecureStorage = Transition(label='Secure Storage')

# Define the partial order
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[InitialReview, ProvenanceCheck, MaterialScan, ContextAnalysis, ExpertPanel, DigitalFingerprint, AI_Pattern, LegalAudit, EthicsReview, FraudDetection, BlockchainLog, Certification, OwnerNotify, ArchiveData, SecureStorage])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[BlockchainLog, Certification, OwnerNotify, ArchiveData, SecureStorage])

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[loop_1, loop_2])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop_1, xor)
root.order.add_edge(loop_2, xor)

print(root)