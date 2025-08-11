import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
skip = SilentTransition()

# Initial workflow
artifact_assessment = OperatorPOWL(operator=Operator.LOOP, children=[AssessArtifact, VerifyProvenance])
condition_analysis = OperatorPOWL(operator=Operator.LOOP, children=[AnalyzeCondition, PlanConservation])
treatment_sequence = OperatorPOWL(operator=Operator.XOR, children=[CleanSurface, StabilizeStructure])
material_source = OperatorPOWL(operator=Operator.XOR, children=[SourceMaterials, FabricateParts])
repair_sequence = OperatorPOWL(operator=Operator.LOOP, children=[PerformRepairs, ApplyPatina])
color_matching = OperatorPOWL(operator=Operator.LOOP, children=[MatchColors, DocumentProcess])
quality_review = OperatorPOWL(operator=Operator.XOR, children=[ReviewQuality, ObtainApproval])
transport_arrangement = OperatorPOWL(operator=Operator.LOOP, children=[PackageSecurely, ArrangeTransport])

# Loop through all activities
root = StrictPartialOrder(nodes=[artifact_assessment, condition_analysis, treatment_sequence, material_source, repair_sequence, color_matching, quality_review, transport_arrangement])
root.order.add_edge(artifact_assessment, condition_analysis)
root.order.add_edge(condition_analysis, treatment_sequence)
root.order.add_edge(treatment_sequence, material_source)
root.order.add_edge(material_source, repair_sequence)
root.order.add_edge(repair_sequence, color_matching)
root.order.add_edge(color_matching, quality_review)
root.order.add_edge(quality_review, transport_arrangement)

print(root)