import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
ProvenanceCheck = Transition(label='Provenance Check')
MaterialScan = Transition(label='Material Scan')
WearAnalysis = Transition(label='Wear Analysis')
ImageCapture = Transition(label='Image Capture')
PatternMatch = Transition(label='Pattern Match')
OwnershipVerify = Transition(label='Ownership Verify')
EthicsReview = Transition(label='Ethics Review')
CarbonDating = Transition(label='Carbon Dating')
RestorationEval = Transition(label='Restoration Eval')
ReportDraft = Transition(label='Report Draft')
StakeholderReview = Transition(label='Stakeholder Review')
ArchiveData = Transition(label='Archive Data')
ExhibitApprove = Transition(label='Exhibit Approve')
ConditionMonitor = Transition(label='Condition Monitor')
FinalCertification = Transition(label='Final Certification')

# Define the process
root = StrictPartialOrder(nodes=[
    ProvenanceCheck,
    MaterialScan,
    WearAnalysis,
    ImageCapture,
    PatternMatch,
    OwnershipVerify,
    EthicsReview,
    CarbonDating,
    RestorationEval,
    ReportDraft,
    StakeholderReview,
    ArchiveData,
    ExhibitApprove,
    ConditionMonitor,
    FinalCertification
])

# Define the order
root.order.add_edge(ProvenanceCheck, MaterialScan)
root.order.add_edge(MaterialScan, WearAnalysis)
root.order.add_edge(WearAnalysis, ImageCapture)
root.order.add_edge(ImageCapture, PatternMatch)
root.order.add_edge(PatternMatch, OwnershipVerify)
root.order.add_edge(OwnershipVerify, EthicsReview)
root.order.add_edge(EthicsReview, CarbonDating)
root.order.add_edge(CarbonDating, RestorationEval)
root.order.add_edge(RestorationEval, ReportDraft)
root.order.add_edge(ReportDraft, StakeholderReview)
root.order.add_edge(StakeholderReview, ArchiveData)
root.order.add_edge(ArchiveData, ExhibitApprove)
root.order.add_edge(ExhibitApprove, ConditionMonitor)
root.order.add_edge(ConditionMonitor, FinalCertification)

print(root)