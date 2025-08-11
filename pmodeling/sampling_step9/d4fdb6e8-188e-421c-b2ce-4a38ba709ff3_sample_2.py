import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

ArtifactReceipt = Transition(label='Artifact Receipt')
InitialInspection = Transition(label='Initial Inspection')
MaterialTesting = Transition(label='Material Testing')
ProvenanceCheck = Transition(label='Provenance Check')
DigitalImaging = Transition(label='Digital Imaging')
DatabaseSearch = Transition(label='Database Search')
ExpertConsult = Transition(label='Expert Consult')
LegalReview = Transition(label='Legal Review')
CulturalAudit = Transition(label='Cultural Audit')
ConditionReport = Transition(label='Condition Report')
RiskAssessment = Transition(label='Risk Assessment')
InsuranceSetup = Transition(label='Insurance Setup')
TransportPlan = Transition(label='Transport Plan')
FinalCertification = Transition(label='Final Certification')
ArchiveEntry = Transition(label='Archive Entry')
PublicationPrep = Transition(label='Publication Prep')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[ArtifactReceipt, InitialInspection, MaterialTesting, ProvenanceCheck, DigitalImaging, DatabaseSearch, ExpertConsult, LegalReview, CulturalAudit, ConditionReport, RiskAssessment, InsuranceSetup, TransportPlan, FinalCertification, ArchiveEntry, PublicationPrep])
xor = OperatorPOWL(operator=Operator.XOR, children=[TransportPlan, FinalCertification])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)