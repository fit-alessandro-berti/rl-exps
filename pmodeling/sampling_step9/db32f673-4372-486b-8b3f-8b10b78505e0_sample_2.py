import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
ReceiveArtifact = Transition(label='Receive Artifact')
ConditionLog = Transition(label='Condition Log')
RadiocarbonTest = Transition(label='Radiocarbon Test')
SpectroscopyScan = Transition(label='Spectroscopy Scan')
ExpertConsult = Transition(label='Expert Consult')
ProvenanceCheck = Transition(label='Provenance Check')
ArchiveSearch = Transition(label='Archive Search')
RiskAssess = Transition(label='Risk Assess')
ThreeDScan = Transition(label='3D Scan')
LegalReview = Transition(label='Legal Review')
InsuranceSetup = Transition(label='Insurance Setup')
CertificateDraft = Transition(label='Certificate Draft')
CertificateApprove = Transition(label='Certificate Approve')
ClimatePack = Transition(label='Climate Pack')
ConservationPlan = Transition(label='Conservation Plan')
MonitoringSchedule = Transition(label='Monitoring Schedule')

# Define silent transitions
skip = SilentTransition()

# Define loop node for expert consultations
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[ExpertConsult, ArchiveSearch, RiskAssess])

# Define xor node for legal review and insurance setup
legal_xor = OperatorPOWL(operator=Operator.XOR, children=[LegalReview, InsuranceSetup])

# Define root POWL model
root = StrictPartialOrder(nodes=[ReceiveArtifact, ConditionLog, RadiocarbonTest, SpectroscopyScan, expert_loop, ThreeDScan, legal_xor, CertificateDraft, CertificateApprove, ClimatePack, ConservationPlan, MonitoringSchedule])

# Add edges to the root POWL model
root.order.add_edge(ReceiveArtifact, ConditionLog)
root.order.add_edge(ConditionLog, RadiocarbonTest)
root.order.add_edge(RadiocarbonTest, SpectroscopyScan)
root.order.add_edge(SpectroscopyScan, expert_loop)
root.order.add_edge(expert_loop, ThreeDScan)
root.order.add_edge(ThreeDScan, legal_xor)
root.order.add_edge(legal_xor, CertificateDraft)
root.order.add_edge(CertificateDraft, CertificateApprove)
root.order.add_edge(CertificateApprove, ClimatePack)
root.order.add_edge(ClimatePack, ConservationPlan)
root.order.add_edge(ConservationPlan, MonitoringSchedule)

# Print the root POWL model
print(root)