import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

SubmitArtifact = Transition(label='Submit Artifact')
InitialReview = Transition(label='Initial Review')
ProvenanceCheck = Transition(label='Provenance Check')
MaterialScan = Transition(label='Material Scan')
ContextAnalysis = Transition(label='Context Analysis')
ExpertPanel = Transition(label='Expert Panel')
DigitalFingerprint = Transition(label='Digital Fingerprint')
AIPattern = Transition(label='AI Pattern')
LegalAudit = Transition(label='Legal Audit')
EthicsReview = Transition(label='Ethics Review')
FraudDetection = Transition(label='Fraud Detection')
BlockchainLog = Transition(label='Blockchain Log')
Certification = Transition(label='Certification')
OwnerNotify = Transition(label='Owner Notify')
ArchiveData = Transition(label='Archive Data')
SecureStorage = Transition(label='Secure Storage')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[SubmitArtifact, InitialReview])
xor = OperatorPOWL(operator=Operator.XOR, children=[ProvenanceCheck, MaterialScan, ContextAnalysis, ExpertPanel, DigitalFingerprint, AIPattern, LegalAudit, EthicsReview, FraudDetection, BlockchainLog, Certification, OwnerNotify, ArchiveData, SecureStorage])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)