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
xor = OperatorPOWL(operator=Operator.XOR, children=[ethics_review, provenance_verify])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[client_update, final_report])
loop = OperatorPOWL(operator=Operator.LOOP, children=[coating_apply, xor2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[stability_check, minor_repair])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[structural_reinforce, xor3])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[surface_restore, archive_store])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[material_test, xor4])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[cleaning_phase, loop3])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[condition_map, xor5])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[artifact_scan, xor6])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[initial_assess, xor7])

# Create the POWL model
root = StrictPartialOrder(nodes=[xor8, loop])
root.order.add_edge(xor8, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)

print(root)