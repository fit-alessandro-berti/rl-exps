import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
AssessArtifact = Transition(label='Assess Artifact')
VerifyProvenance = Transition(label='Verify Provenance')
AnalyzeCondition = Transition(label='Analyze Condition')
PlanConservation = Transition(label='Plan Conservation')
CleanSurface = Transition(label='Clean Surface')
StabilizeStructure = Transition(label='Stabilize Structure')
SourceMaterials = Transition(label='Source Materials')
FabricateParts = Transition(label='Fabricate Parts')
PerformRepairs = Transition(label='Perform Repairs')
ApplyPatina = Transition(label='Apply Patina')
MatchColors = Transition(label='Match Colors')
DocumentProcess = Transition(label='Document Process')
ReviewQuality = Transition(label='Review Quality')
ObtainApproval = Transition(label='Obtain Approval')
PackageSecurely = Transition(label='Package Securely')
ArrangeTransport = Transition(label='Arrange Transport')

# Define the workflow model
root = StrictPartialOrder(nodes=[
    AssessArtifact,
    VerifyProvenance,
    AnalyzeCondition,
    PlanConservation,
    CleanSurface,
    StabilizeStructure,
    SourceMaterials,
    FabricateParts,
    PerformRepairs,
    ApplyPatina,
    MatchColors,
    DocumentProcess,
    ReviewQuality,
    ObtainApproval,
    PackageSecurely,
    ArrangeTransport
])

# Define the order of execution
root.order.add_edge(AssessArtifact, VerifyProvenance)
root.order.add_edge(VerifyProvenance, AnalyzeCondition)
root.order.add_edge(AnalyzeCondition, PlanConservation)
root.order.add_edge(PlanConservation, CleanSurface)
root.order.add_edge(CleanSurface, StabilizeStructure)
root.order.add_edge(StabilizeStructure, SourceMaterials)
root.order.add_edge(SourceMaterials, FabricateParts)
root.order.add_edge(FabricateParts, PerformRepairs)
root.order.add_edge(PerformRepairs, ApplyPatina)
root.order.add_edge(ApplyPatina, MatchColors)
root.order.add_edge(MatchColors, DocumentProcess)
root.order.add_edge(DocumentProcess, ReviewQuality)
root.order.add_edge(ReviewQuality, ObtainApproval)
root.order.add_edge(ObtainApproval, PackageSecurely)
root.order.add_edge(PackageSecurely, ArrangeTransport)

print(root)