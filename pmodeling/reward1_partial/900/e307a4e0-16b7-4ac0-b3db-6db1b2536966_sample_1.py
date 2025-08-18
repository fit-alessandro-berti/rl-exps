import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for loop and choice nodes
skip = SilentTransition()

# Define the POWL model
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[condition_map, minor_repair, structural_reinforce, surface_restore])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[stability_check, coating_apply])
xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_verify, ethics_review])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[client_update, final_report])
root = StrictPartialOrder(nodes=[initial_assess, artifact_scan, material_test, cleaning_phase, loop_1, loop_2, xor, xor_2, archive_store])

# Define the order dependencies
root.order.add_edge(initial_assess, artifact_scan)
root.order.add_edge(artifact_scan, material_test)
root.order.add_edge(material_test, cleaning_phase)
root.order.add_edge(cleaning_phase, loop_1)
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, xor)
root.order.add_edge(xor, xor_2)
root.order.add_edge(xor_2, archive_store)
root.order.add_edge(archive_store, final_report)