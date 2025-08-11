import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for material test
xor_material_test = OperatorPOWL(operator=Operator.XOR, children=[material_test, skip])

# Define exclusive choice for cleaning phase
xor_cleaning_phase = OperatorPOWL(operator=Operator.XOR, children=[cleaning_phase, skip])

# Define exclusive choice for stability check
xor_stability_check = OperatorPOWL(operator=Operator.XOR, children=[stability_check, skip])

# Define exclusive choice for minor repair
xor_minor_repair = OperatorPOWL(operator=Operator.XOR, children=[minor_repair, skip])

# Define exclusive choice for structural reinforce
xor_structural_reinforce = OperatorPOWL(operator=Operator.XOR, children=[structural_reinforce, skip])

# Define exclusive choice for surface restore
xor_surface_restore = OperatorPOWL(operator=Operator.XOR, children=[surface_restore, skip])

# Define exclusive choice for coating apply
xor_coating_apply = OperatorPOWL(operator=Operator.XOR, children=[coating_apply, skip])

# Define loop for ethics review
loop_ethics_review = OperatorPOWL(operator=Operator.LOOP, children=[ethics_review])

# Define loop for provenance verify
loop_provenance_verify = OperatorPOWL(operator=Operator.LOOP, children=[provenance_verify])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    initial_assess,
    artifact_scan,
    condition_map,
    xor_material_test,
    xor_cleaning_phase,
    xor_stability_check,
    xor_minor_repair,
    xor_structural_reinforce,
    xor_surface_restore,
    xor_coating_apply,
    loop_ethics_review,
    loop_provenance_verify,
    client_update,
    final_report,
    archive_store
])

# Define the order of the POWL model
root.order.add_edge(initial_assess, artifact_scan)
root.order.add_edge(artifact_scan, condition_map)
root.order.add_edge(condition_map, xor_material_test)
root.order.add_edge(xor_material_test, xor_cleaning_phase)
root.order.add_edge(xor_cleaning_phase, xor_stability_check)
root.order.add_edge(xor_stability_check, xor_minor_repair)
root.order.add_edge(xor_minor_repair, xor_structural_reinforce)
root.order.add_edge(xor_structural_reinforce, xor_surface_restore)
root.order.add_edge(xor_surface_restore, xor_coating_apply)
root.order.add_edge(xor_coating_apply, loop_ethics_review)
root.order.add_edge(loop_ethics_review, loop_provenance_verify)
root.order.add_edge(loop_provenance_verify, client_update)
root.order.add_edge(client_update, final_report)
root.order.add_edge(final_report, archive_store)

print(root)