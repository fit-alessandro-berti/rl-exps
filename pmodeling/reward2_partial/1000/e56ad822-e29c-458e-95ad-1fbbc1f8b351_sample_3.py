import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with their labels
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

# Define the partial order model
root = StrictPartialOrder(nodes=[
    SubmitArtifact,
    InitialReview,
    ProvenanceCheck,
    MaterialScan,
    ContextAnalysis,
    ExpertPanel,
    DigitalFingerprint,
    AIPattern,
    LegalAudit,
    EthicsReview,
    FraudDetection,
    BlockchainLog,
    Certification,
    OwnerNotify,
    ArchiveData,
    SecureStorage
])

# Define the order dependencies
root.order.add_edge(SubmitArtifact, InitialReview)
root.order.add_edge(InitialReview, ProvenanceCheck)
root.order.add_edge(ProvenanceCheck, MaterialScan)
root.order.add_edge(MaterialScan, ContextAnalysis)
root.order.add_edge(ContextAnalysis, ExpertPanel)
root.order.add_edge(ExpertPanel, DigitalFingerprint)
root.order.add_edge(DigitalFingerprint, AIPattern)
root.order.add_edge(AIPattern, LegalAudit)
root.order.add_edge(LegalAudit, EthicsReview)
root.order.add_edge(EthicsReview, FraudDetection)
root.order.add_edge(FraudDetection, BlockchainLog)
root.order.add_edge(BlockchainLog, Certification)
root.order.add_edge(Certification, OwnerNotify)
root.order.add_edge(OwnerNotify, ArchiveData)
root.order.add_edge(ArchiveData, SecureStorage)

# Print the root model for verification
print(root)