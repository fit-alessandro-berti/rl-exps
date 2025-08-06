import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transitions
Skip = SilentTransition()

# Define the loops and XORs
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[RiskAssess, ArchiveSearch])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[LegalReview, InsuranceSetup])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[CertificateDraft, CertificateApprove])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[ConservationPlan, MonitoringSchedule])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[ProvenanceCheck, Skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ArchiveSearch, Skip])

# Define the partial order
root = StrictPartialOrder(nodes=[
    ReceiveArtifact,
    ConditionLog,
    RadiocarbonTest,
    SpectroscopyScan,
    ExpertConsult,
    xor1,
    xor2,
    ThreeDScan,
    loop1,
    loop2,
    loop3,
    loop4,
    ClimatePack
])

# Define the edges in the partial order
root.order.add_edge(ReceiveArtifact, ConditionLog)
root.order.add_edge(ConditionLog, RadiocarbonTest)
root.order.add_edge(RadiocarbonTest, SpectroscopyScan)
root.order.add_edge(SpectroscopyScan, ExpertConsult)
root.order.add_edge(ExpertConsult, xor1)
root.order.add_edge(ExpertConsult, xor2)
root.order.add_edge(xor1, RiskAssess)
root.order.add_edge(xor2, ArchiveSearch)
root.order.add_edge(RiskAssess, ArchiveSearch)
root.order.add_edge(ArchiveSearch, ThreeDScan)
root.order.add_edge(ThreeDScan, loop1)
root.order.add_edge(ThreeDScan, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop2, loop4)
root.order.add_edge(loop3, ClimatePack)
root.order.add_edge(loop4, ClimatePack)

# Print the root of the POWL model
print(root)