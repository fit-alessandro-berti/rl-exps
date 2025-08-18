import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
InitialAssess = Transition(label='Initial Assess')
ConditionScan = Transition(label='Condition Scan')
MaterialTest = Transition(label='Material Test')
HistoricalCheck = Transition(label='Historical Check')
ProvenanceVerify = Transition(label='Provenance Verify')
PartsSourcing = Transition(label='Parts Sourcing')
GentleClean = Transition(label='Gentle Clean')
StabilizeItem = Transition(label='Stabilize Item')
StructuralRepair = Transition(label='Structural Repair')
SurfaceFinish = Transition(label='Surface Finish')
ExpertConsult = Transition(label='Expert Consult')
ArchivalReview = Transition(label='Archival Review')
EthicsAudit = Transition(label='Ethics Audit')
QualityInspect = Transition(label='Quality Inspect')
PhotoDocument = Transition(label='Photo Document')
PackagingPrep = Transition(label='Packaging Prep')
ReportGenerate = Transition(label='Report Generate')
CertifyProvenance = Transition(label='Certify Provenance')

# Define the partial order
root = StrictPartialOrder(nodes=[
    InitialAssess, 
    ConditionScan, 
    MaterialTest, 
    HistoricalCheck, 
    ProvenanceVerify, 
    PartsSourcing, 
    GentleClean, 
    StabilizeItem, 
    StructuralRepair, 
    SurfaceFinish, 
    ExpertConsult, 
    ArchivalReview, 
    EthicsAudit, 
    QualityInspect, 
    PhotoDocument, 
    PackagingPrep, 
    ReportGenerate, 
    CertifyProvenance
])

# Define the dependencies (edges) between activities
root.order.add_edge(InitialAssess, ConditionScan)
root.order.add_edge(ConditionScan, MaterialTest)
root.order.add_edge(MaterialTest, HistoricalCheck)
root.order.add_edge(HistoricalCheck, ProvenanceVerify)
root.order.add_edge(ProvenanceVerify, PartsSourcing)
root.order.add_edge(PartsSourcing, GentleClean)
root.order.add_edge(GentleClean, StabilizeItem)
root.order.add_edge(StabilizeItem, StructuralRepair)
root.order.add_edge(StructuralRepair, SurfaceFinish)
root.order.add_edge(SurfaceFinish, ExpertConsult)
root.order.add_edge(ExpertConsult, ArchivalReview)
root.order.add_edge(ArchivalReview, EthicsAudit)
root.order.add_edge(EthicsAudit, QualityInspect)
root.order.add_edge(QualityInspect, PhotoDocument)
root.order.add_edge(PhotoDocument, PackagingPrep)
root.order.add_edge(PackagingPrep, ReportGenerate)
root.order.add_edge(ReportGenerate, CertifyProvenance)

print(root)