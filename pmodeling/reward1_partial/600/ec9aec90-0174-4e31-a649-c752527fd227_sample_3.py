from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define the POWL model
root = StrictPartialOrder()

# Define the partial order dependencies
root.order.add_edge(assess_artifact, verify_provenance)
root.order.add_edge(verify_provenance, analyze_condition)
root.order.add_edge(analyze_condition, plan_conservation)
root.order.add_edge(plan_conservation, clean_surface)
root.order.add_edge(clean_surface, stabilize_structure)
root.order.add_edge(stabilize_structure, source_materials)
root.order.add_edge(source_materials, fabricate_parts)
root.order.add_edge(fabricate_parts, perform_repairs)
root.order.add_edge(perform_repairs, apply_patina)
root.order.add_edge(apply_patina, match_colors)
root.order.add_edge(match_colors, document_process)
root.order.add_edge(document_process, review_quality)
root.order.add_edge(review_quality, obtain_approval)
root.order.add_edge(obtain_approval, package_securely)
root.order.add_edge(package_securely, arrange_transport)

print(root)