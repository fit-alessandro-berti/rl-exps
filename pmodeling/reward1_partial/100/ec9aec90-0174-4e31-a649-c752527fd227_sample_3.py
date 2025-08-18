import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
assess_artifact = Transition(label='Assess Artifact')
verify_provenance = Transition(label='Verify Provenance')
analyze_condition = Transition(label='Analyze Condition')
plan_conservation = Transition(label='Plan Conservation')
clean_surface = Transition(label='Clean Surface')
stabilize_structure = Transition(label='Stabilize Structure')
source_materials = Transition(label='Source Materials')
fabricate_parts = Transition(label='Fabricate Parts')
perform_repairs = Transition(label='Perform Repairs')
apply_patina = Transition(label='Apply Patina')
match_colors = Transition(label='Match Colors')
document_process = Transition(label='Document Process')
review_quality = Transition(label='Review Quality')
obtain_approval = Transition(label='Obtain Approval')
package_securely = Transition(label='Package Securely')
arrange_transport = Transition(label='Arrange Transport')

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[stabilize_structure, fabricate_parts])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[clean_surface, match_colors])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[apply_patina, package_securely])

# Construct the POWL model
root = StrictPartialOrder(nodes=[assess_artifact, verify_provenance, analyze_condition, plan_conservation, xor1, xor2, xor3, review_quality, obtain_approval, arrange_transport])
root.order.add_edge(assess_artifact, verify_provenance)
root.order.add_edge(assess_artifact, analyze_condition)
root.order.add_edge(assess_artifact, plan_conservation)
root.order.add_edge(verify_provenance, analyze_condition)
root.order.add_edge(analyze_condition, plan_conservation)
root.order.add_edge(plan_conservation, xor1)
root.order.add_edge(plan_conservation, xor2)
root.order.add_edge(plan_conservation, xor3)
root.order.add_edge(xor1, clean_surface)
root.order.add_edge(xor1, match_colors)
root.order.add_edge(xor2, apply_patina)
root.order.add_edge(xor2, package_securely)
root.order.add_edge(xor3, arrange_transport)
root.order.add_edge(review_quality, obtain_approval)
root.order.add_edge(obtain_approval, arrange_transport)

# Print the root POWL model
print(root)