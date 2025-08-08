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

# Define the control flow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[minor_repair, structural_reinforce, surface_restore, coating_apply])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, provenance_verify, client_update])
loop = OperatorPOWL(operator=Operator.LOOP, children=[stability_check, xor1])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[cleaning_phase, loop])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[final_report, archive_store])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[artifact_scan, condition_map, material_test, xor3])

# Define the root
root = StrictPartialOrder(nodes=[xor5, xor4])
root.order.add_edge(xor5, xor4)