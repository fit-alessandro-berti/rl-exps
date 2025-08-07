from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the partial order
root = StrictPartialOrder(nodes=[VisualInspect, DocumentGather, MaterialTest, PigmentAnalyze, StyleCompare, ProvenanceTrace, DataCrosscheck, InfraredScan, XrayFluoresce, ExpertConsult, ForgeryDetect, ReportDraft, StakeholderReview, FinalApproval, ArchiveStore])

# Define the dependencies (partial order)
root.order.add_edge(VisualInspect, DocumentGather)
root.order.add_edge(DocumentGather, MaterialTest)
root.order.add_edge(MaterialTest, PigmentAnalyze)
root.order.add_edge(PigmentAnalyze, StyleCompare)
root.order.add_edge(StyleCompare, ProvenanceTrace)
root.order.add_edge(ProvenanceTrace, DataCrosscheck)
root.order.add_edge(DataCrosscheck, InfraredScan)
root.order.add_edge(InfraredScan, XrayFluoresce)
root.order.add_edge(XrayFluoresce, ExpertConsult)
root.order.add_edge(ExpertConsult, ForgeryDetect)
root.order.add_edge(ForgeryDetect, ReportDraft)
root.order.add_edge(ReportDraft, StakeholderReview)
root.order.add_edge(StakeholderReview, FinalApproval)
root.order.add_edge(FinalApproval, ArchiveStore)

print(root)