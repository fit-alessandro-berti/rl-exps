import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
xor = OperatorPOWL(operator=Operator.XOR, children=[BlockchainLog, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[OwnerNotify, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Certification, skip])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[ProvenanceCheck, MaterialScan, ContextAnalysis, ExpertPanel, DigitalFingerprint, AI_Pattern])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[LegalAudit, EthicsReview, FraudDetection])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[ArchiveData, SecureStorage])

root = StrictPartialOrder(nodes=[SubmitArtifact, InitialReview, loop1, loop2, xor, xor2, xor3])
root.order.add_edge(SubmitArtifact, InitialReview)
root.order.add_edge(InitialReview, loop1)
root.order.add_edge(InitialReview, loop2)
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, BlockchainLog)
root.order.add_edge(xor3, OwnerNotify)
root.order.add_edge(xor3, Certification)
root.order.add_edge(BlockchainLog, OwnerNotify)
root.order.add_edge(BlockchainLog, Certification)
root.order.add_edge(OwnerNotify, Certification)
root.order.add_edge(Certification, ArchiveData)
root.order.add_edge(Certification, SecureStorage)
root.order.add_edge(ArchiveData, SecureStorage)

# Print the root POWL model
print(root)