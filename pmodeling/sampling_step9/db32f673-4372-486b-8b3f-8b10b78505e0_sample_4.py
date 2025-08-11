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

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[ReceiveArtifact, ConditionLog, RadiocarbonTest, SpectroscopyScan, ExpertConsult, ProvenanceCheck, ArchiveSearch, RiskAssess, ThreeDScan, LegalReview, InsuranceSetup, CertificateDraft, CertificateApprove, ClimatePack, ConservationPlan, MonitoringSchedule])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ReceiveArtifact, ConditionLog, RadiocarbonTest, SpectroscopyScan, ExpertConsult, ProvenanceCheck, ArchiveSearch, RiskAssess, ThreeDScan, LegalReview, InsuranceSetup, CertificateDraft, CertificateApprove, ClimatePack, ConservationPlan, MonitoringSchedule])

# Define exclusive choice nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])

# Define root
root = StrictPartialOrder(nodes=[xor1])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop1)