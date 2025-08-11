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

initial = OperatorPOWL(operator=Operator.XOR, children=[ArtifactReceipt, InitialInspection])
initial_loop = OperatorPOWL(operator=Operator.LOOP, children=[InitialInspection, MaterialTesting, ProvenanceCheck, DigitalImaging, DatabaseSearch, ExpertConsult, LegalReview, CulturalAudit, ConditionReport, RiskAssessment, InsuranceSetup, TransportPlan, FinalCertification, ArchiveEntry, PublicationPrep])

root = StrictPartialOrder(nodes=[initial, initial_loop])
root.order.add_edge(initial, initial_loop)

print(root)