from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
initial_assess = Transition(label='Initial Assess')
artifact_scan = Transition(label='Artifact Scan')
condition_map = Transition(label='Condition Map')
material_test = Transition(label='Material Test')
cleaning_phase = Transition(label='Cleaning Phase')
stability_check = Transition(label='Stability Check')
minor_repair = Transition(label='Minor Repair')
structural_reinforce = Transition(label='Structural Reinforce')
surface_restore = Transition(label='Surface Restore')
coating_apply = Transition(label='Coating Apply')
ethics_review = Transition(label='Ethics Review')
provenance_verify = Transition(label='Provenance Verify')
client_update = Transition(label='Client Update')
final_report = Transition(label='Final Report')
archive_store = Transition(label='Archive Store')

# Define nodes
initial_assess_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[initial_assess])
artifact_scan_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[artifact_scan])
condition_map_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[condition_map])
material_test_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[material_test])
cleaning_phase_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[cleaning_phase])
stability_check_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[stability_check])
minor_repair_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[minor_repair])
structural_reinforce_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[structural_reinforce])
surface_restore_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[surface_restore])
coating_apply_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[coating_apply])
ethics_review_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[ethics_review])
provenance_verify_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[provenance_verify])
client_update_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[client_update])
final_report_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[final_report])
archive_store_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[archive_store])

# Define partial order
root = StrictPartialOrder(nodes=[
    initial_assess_node,
    artifact_scan_node,
    condition_map_node,
    material_test_node,
    cleaning_phase_node,
    stability_check_node,
    minor_repair_node,
    structural_reinforce_node,
    surface_restore_node,
    coating_apply_node,
    ethics_review_node,
    provenance_verify_node,
    client_update_node,
    final_report_node,
    archive_store_node
])

# Define dependencies
root.order.add_edge(initial_assess_node, artifact_scan_node)
root.order.add_edge(artifact_scan_node, condition_map_node)
root.order.add_edge(condition_map_node, material_test_node)
root.order.add_edge(material_test_node, cleaning_phase_node)
root.order.add_edge(cleaning_phase_node, stability_check_node)
root.order.add_edge(stability_check_node, minor_repair_node)
root.order.add_edge(minor_repair_node, structural_reinforce_node)
root.order.add_edge(structural_reinforce_node, surface_restore_node)
root.order.add_edge(surface_restore_node, coating_apply_node)
root.order.add_edge(coating_apply_node, ethics_review_node)
root.order.add_edge(ethics_review_node, provenance_verify_node)
root.order.add_edge(provenance_verify_node, client_update_node)
root.order.add_edge(client_update_node, final_report_node)
root.order.add_edge(final_report_node, archive_store_node)

print(root)