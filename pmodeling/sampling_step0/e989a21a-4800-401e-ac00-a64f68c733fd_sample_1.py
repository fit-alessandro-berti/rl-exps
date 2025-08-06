import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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
root = StrictPartialOrder(
    nodes=[
        VisualInspect,
        DocumentGather,
        MaterialTest,
        PigmentAnalyze,
        StyleCompare,
        ProvenanceTrace,
        DataCrosscheck,
        InfraredScan,
        XrayFluoresce,
        ExpertConsult,
        ForgeryDetect,
        ReportDraft,
        StakeholderReview,
        FinalApproval,
        ArchiveStore
    ],
    order={
        (VisualInspect, DocumentGather): None,
        (VisualInspect, MaterialTest): None,
        (DocumentGather, PigmentAnalyze): None,
        (DocumentGather, StyleCompare): None,
        (MaterialTest, ProvenanceTrace): None,
        (PigmentAnalyze, DataCrosscheck): None,
        (StyleCompare, DataCrosscheck): None,
        (ProvenanceTrace, InfraredScan): None,
        (ProvenanceTrace, XrayFluoresce): None,
        (DataCrosscheck, ExpertConsult): None,
        (DataCrosscheck, ForgeryDetect): None,
        (InfraredScan, ReportDraft): None,
        (XrayFluoresce, ReportDraft): None,
        (ExpertConsult, ReportDraft): None,
        (ExpertConsult, StakeholderReview): None,
        (ForgeryDetect, ReportDraft): None,
        (ReportDraft, StakeholderReview): None,
        (StakeholderReview, FinalApproval): None,
        (StakeholderReview, ArchiveStore): None,
        (FinalApproval, ArchiveStore): None
    }
)