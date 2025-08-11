import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define silent transitions (if any)
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[AssessArtifact, VerifyProvenance, AnalyzeCondition, PlanConservation])
xor = OperatorPOWL(operator=Operator.XOR, children=[StabilizeStructure, SourceMaterials, FabricateParts, PerformRepairs])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[CleanSurface, ApplyPatina, MatchColors])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[DocumentProcess, ReviewQuality, ObtainApproval, PackageSecurely])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ArrangeTransport])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, skip)