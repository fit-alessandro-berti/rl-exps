import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

VisualInspect = Transition(label='Visual Inspect')
DocumentGather = Transition(label='Document Gather')
MaterialTest = Transition(label='Material Test')
PigmentAnalyze = Transition(label='Pigment Analyze')
StyleCompare = Transition(label='Style Compare')
ProvenanceTrace = Transition(label='Provenance Trace')
DataCrosscheck = Transition(label='Data Crosscheck')
InfraredScan = Transition(label='Infrared Scan')
XrayFluoresce = Transition(label='Xray Fluoresce')
ExpertConsult = Transition(label='Expert Consult')
ForgeryDetect = Transition(label='Forgery Detect')
ReportDraft = Transition(label='Report Draft')
StakeholderReview = Transition(label='Stakeholder Review')
FinalApproval = Transition(label='Final Approval')
ArchiveStore = Transition(label='Archive Store')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[VisualInspect, DocumentGather])
xor = OperatorPOWL(operator=Operator.XOR, children=[MaterialTest, PigmentAnalyze, StyleCompare, ProvenanceTrace, DataCrosscheck, InfraredScan, XrayFluoresce, ExpertConsult, ForgeryDetect, ReportDraft, StakeholderReview, FinalApproval, ArchiveStore])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)