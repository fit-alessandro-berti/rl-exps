import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
Assess_Artifact = Transition(label='Assess Artifact')
Verify_Provenance = Transition(label='Verify Provenance')
Analyze_Condition = Transition(label='Analyze Condition')
Plan_Conservation = Transition(label='Plan Conservation')
Clean_Surface = Transition(label='Clean Surface')
Stabilize_Structure = Transition(label='Stabilize Structure')
Source_Materials = Transition(label='Source Materials')
Fabricate_Parts = Transition(label='Fabricate Parts')
Perform_Repairs = Transition(label='Perform Repairs')
Apply_Patina = Transition(label='Apply Patina')
Match_Colors = Transition(label='Match Colors')
Document_Process = Transition(label='Document Process')
Review_Quality = Transition(label='Review Quality')
Obtain_Approval = Transition(label='Obtain Approval')
Package_Securely = Transition(label='Package Securely')
Arrange_Transport = Transition(label='Arrange Transport')

# Define the process as a strict partial order
root = StrictPartialOrder(nodes=[
    Assess_Artifact, Verify_Provenance, Analyze_Condition,
    Plan_Conservation, Clean_Surface, Stabilize_Structure,
    Source_Materials, Fabricate_Parts, Perform_Repairs,
    Apply_Patina, Match_Colors, Document_Process,
    Review_Quality, Obtain_Approval, Package_Securely,
    Arrange_Transport
])

# Define dependencies between activities
root.order.add_edge(Assess_Artifact, Verify_Provenance)
root.order.add_edge(Verify_Provenance, Analyze_Condition)
root.order.add_edge(Analyze_Condition, Plan_Conservation)
root.order.add_edge(Plan_Conservation, Clean_Surface)
root.order.add_edge(Clean_Surface, Stabilize_Structure)
root.order.add_edge(Stabilize_Structure, Source_Materials)
root.order.add_edge(Source_Materials, Fabricate_Parts)
root.order.add_edge(Fabricate_Parts, Perform_Repairs)
root.order.add_edge(Perform_Repairs, Apply_Patina)
root.order.add_edge(Apply_Patina, Match_Colors)
root.order.add_edge(Match_Colors, Document_Process)
root.order.add_edge(Document_Process, Review_Quality)
root.order.add_edge(Review_Quality, Obtain_Approval)
root.order.add_edge(Obtain_Approval, Package_Securely)
root.order.add_edge(Package_Securely, Arrange_Transport)