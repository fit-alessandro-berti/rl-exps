import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ia = Transition(label='Initial Assess')
ascan = Transition(label='Artifact Scan')
condmap = Transition(label='Condition Map')
mattest = Transition(label='Material Test')
clean = Transition(label='Cleaning Phase')
stability = Transition(label='Stability Check')
minor_repair = Transition(label='Minor Repair')
struct_reinforce = Transition(label='Structural Reinforce')
surface_restore = Transition(label='Surface Restore')
coating_apply = Transition(label='Coating Apply')
ethics_review = Transition(label='Ethics Review')
prov_verify = Transition(label='Provenance Verify')
client_update = Transition(label='Client Update')
final_report = Transition(label='Final Report')
archive_store = Transition(label='Archive Store')

# Silent transition for optional client review
skip_client = SilentTransition()

# Loop for optional client review: repeat Client Update until exit
client_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_update, skip_client])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ia, ascan, condmap, mattest,
    clean, stability, minor_repair, struct_reinforce, surface_restore, coating_apply,
    ethics_review, prov_verify, client_loop, final_report, archive_store
])

# Define the control-flow dependencies
root.order.add_edge(ia, ascan)
root.order.add_edge(ia, condmap)
root.order.add_edge(ascan, mattest)
root.order.add_edge(condmap, mattest)
root.order.add_edge(mattest, clean)
root.order.add_edge(clean, stability)
root.order.add_edge(stability, minor_repair)
root.order.add_edge(minor_repair, struct_reinforce)
root.order.add_edge(struct_reinforce, surface_restore)
root.order.add_edge(surface_restore, coating_apply)
root.order.add_edge(coating_apply, ethics_review)
root.order.add_edge(ethics_review, prov_verify)
root.order.add_edge(prov_verify, client_loop)
root.order.add_edge(client_loop, final_report)
root.order.add_edge(final_report, archive_store)

# The final report must follow the client review loop
root.order.add_edge(client_loop, final_report)