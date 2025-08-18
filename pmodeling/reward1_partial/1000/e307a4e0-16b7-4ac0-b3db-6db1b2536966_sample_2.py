import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[structural_reinforce, surface_restore])
loop = OperatorPOWL(operator=Operator.LOOP, children=[coating_apply, ethics_review, provenance_verify])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[client_update, final_report])
root = StrictPartialOrder(nodes=[initial_assess, artifact_scan, condition_map, material_test, cleaning_phase, stability_check, minor_repair, xor, loop, xor2, archive_store])
root.order.add_edge(initial_assess, artifact_scan)
root.order.add_edge(artifact_scan, condition_map)
root.order.add_edge(condition_map, material_test)
root.order.add_edge(material_test, cleaning_phase)
root.order.add_edge(cleaning_phase, stability_check)
root.order.add_edge(stability_check, minor_repair)
root.order.add_edge(minor_repair, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, archive_store)