import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the exclusive choice for obtaining approval
Obtain_Approval_Choice = OperatorPOWL(operator=Operator.XOR, children=[Obtain_Approval, Package_Securely])

# Define the loop for fabricating parts
Fabricate_Parts_Loop = OperatorPOWL(operator=Operator.LOOP, children=[Fabricate_Parts, Arrange_Transport])

# Define the strict partial order for the entire process
root = StrictPartialOrder(nodes=[
    Assess_Artifact,
    Verify_Provenance,
    Analyze_Condition,
    Plan_Conservation,
    Clean_Surface,
    Stabilize_Structure,
    Source_Materials,
    Fabricate_Parts_Loop,
    Perform_Repairs,
    Apply_Patina,
    Match_Colors,
    Document_Process,
    Review_Quality,
    Obtain_Approval_Choice
])
root.order.add_edge(Analyze_Condition, Plan_Conservation)
root.order.add_edge(Plan_Conservation, Clean_Surface)
root.order.add_edge(Clean_Surface, Stabilize_Structure)
root.order.add_edge(Stabilize_Structure, Source_Materials)
root.order.add_edge(Source_Materials, Fabricate_Parts_Loop)
root.order.add_edge(Fabricate_Parts_Loop, Perform_Repairs)
root.order.add_edge(Perform_Repairs, Apply_Patina)
root.order.add_edge(Apply_Patina, Match_Colors)
root.order.add_edge(Match_Colors, Document_Process)
root.order.add_edge(Document_Process, Review_Quality)
root.order.add_edge(Review_Quality, Obtain_Approval_Choice)