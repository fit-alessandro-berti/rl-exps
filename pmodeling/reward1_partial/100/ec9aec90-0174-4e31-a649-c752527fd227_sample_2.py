import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[Stabilize_Structure, Fabricate_Parts])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Clean_Surface, Source_Materials])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Perform_Repairs, Match_Colors])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Apply_Patina, Review_Quality])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Package_Securely, Arrange_Transport])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Obtain_Approval, Package_Securely])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Assess_Artifact, Verify_Provenance, Analyze_Condition, Plan_Conservation])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6])

root = StrictPartialOrder(nodes=[loop1, loop2])
root.order.add_edge(loop1, loop2)

# Print the root POWL model
print(root)