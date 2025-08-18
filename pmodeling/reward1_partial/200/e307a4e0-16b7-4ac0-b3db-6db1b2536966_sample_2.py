from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transition
skip = SilentTransition()

# Define the process tree
loop = OperatorPOWL(operator=Operator.LOOP, children=[cleaning_phase, minor_repair, structural_reinforce, surface_restore, coating_apply])
xor = OperatorPOWL(operator=Operator.XOR, children=[stability_check, ethics_review, provenance_verify, client_update])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[final_report, archive_store])

# Create the root POWL model
root = StrictPartialOrder(nodes=[initial_assess, artifact_scan, condition_map, material_test, loop, xor, xor2])
root.order.add_edge(initial_assess, artifact_scan)
root.order.add_edge(artifact_scan, condition_map)
root.order.add_edge(condition_map, material_test)
root.order.add_edge(material_test, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)

# Print the root POWL model
print(root)