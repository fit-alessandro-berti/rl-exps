import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
root = StrictPartialOrder(nodes=[ReceiveArtifact, ConditionLog, RadiocarbonTest, SpectroscopyScan, ExpertConsult, ProvenanceCheck, ArchiveSearch, RiskAssess, ThreeDScan, LegalReview, InsuranceSetup, CertificateDraft, CertificateApprove, ClimatePack, ConservationPlan, MonitoringSchedule])

# Define the dependencies between the activities
root.order.add_edge(ReceiveArtifact, ConditionLog)
root.order.add_edge(ConditionLog, RadiocarbonTest)
root.order.add_edge(RadiocarbonTest, SpectroscopyScan)
root.order.add_edge(SpectroscopyScan, ExpertConsult)
root.order.add_edge(ExpertConsult, ProvenanceCheck)
root.order.add_edge(ProvenanceCheck, ArchiveSearch)
root.order.add_edge(ArchiveSearch, RiskAssess)
root.order.add_edge(RiskAssess, ThreeDScan)
root.order.add_edge(ThreeDScan, LegalReview)
root.order.add_edge(LegalReview, InsuranceSetup)
root.order.add_edge(InsuranceSetup, CertificateDraft)
root.order.add_edge(CertificateDraft, CertificateApprove)
root.order.add_edge(CertificateApprove, ClimatePack)
root.order.add_edge(ClimatePack, ConservationPlan)
root.order.add_edge(ConservationPlan, MonitoringSchedule)