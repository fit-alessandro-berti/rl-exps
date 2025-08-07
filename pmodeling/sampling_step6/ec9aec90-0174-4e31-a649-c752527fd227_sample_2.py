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

# Define the root POWL model
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

# Note: The order of activities is not specified in the POWL model, so it's assumed to be sequential.
# If a specific order is required, you can add edges to define the flow.
# For example, if 'Assess Artifact' should precede 'Verify Provenance':
# root.order.add_edge(AssessArtifact, VerifyProvenance)

print(root)