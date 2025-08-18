import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Create a root partial order
root = StrictPartialOrder()

# Define the partial order structure
root.nodes.extend([ReceiveArtifact, ConditionLog, RadiocarbonTest, SpectroscopyScan, ExpertConsult, ProvenanceCheck, ArchiveSearch, RiskAssess, ThreeDScan, LegalReview, InsuranceSetup, CertificateDraft, CertificateApprove, ClimatePack, ConservationPlan, MonitoringSchedule])

# Define the partial order dependencies
root.order.add_edge(ReceiveArtifact, ConditionLog)
root.order.add_edge(ConditionLog, RadiocarbonTest)
root.order.add_edge(ConditionLog, SpectroscopyScan)
root.order.add_edge(RadiocarbonTest, ExpertConsult)
root.order.add_edge(RadiocarbonTest, ArchiveSearch)
root.order.add_edge(SpectroscopyScan, ExpertConsult)
root.order.add_edge(SpectroscopyScan, ArchiveSearch)
root.order.add_edge(ExpertConsult, ProvenanceCheck)
root.order.add_edge(ProvenanceCheck, ArchiveSearch)
root.order.add_edge(ProvenanceCheck, RiskAssess)
root.order.add_edge(RiskAssess, LegalReview)
root.order.add_edge(LegalReview, InsuranceSetup)
root.order.add_edge(InsuranceSetup, CertificateDraft)
root.order.add_edge(CertificateDraft, CertificateApprove)
root.order.add_edge(CertificateApprove, ClimatePack)
root.order.add_edge(ClimatePack, ConservationPlan)
root.order.add_edge(ConservationPlan, MonitoringSchedule)

# Print the root partial order
print(root)