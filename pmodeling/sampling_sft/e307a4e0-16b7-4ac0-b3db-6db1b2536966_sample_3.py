import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
ia = Transition(label='Initial Assess')
ascan = Transition(label='Artifact Scan')
cond = Transition(label='Condition Map')
mat = Transition(label='Material Test')
clean = Transition(label='Cleaning Phase')
stable = Transition(label='Stability Check')
minor = Transition(label='Minor Repair')
struct = Transition(label='Structural Reinforce')
surf = Transition(label='Surface Restore')
coating = Transition(label='Coating Apply')
ethics = Transition(label='Ethics Review')
provenance = Transition(label='Provenance Verify')
client = Transition(label='Client Update')
final = Transition(label='Final Report')
archive = Transition(label='Archive Store')

# Silent transition for optional client review
skip_client = SilentTransition()

# Choice between client update and skipping
client_choice = OperatorPOWL(operator=Operator.XOR, children=[client, skip_client])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ia, ascan, cond, mat,
    clean, stable, minor, struct, surf,
    coating, ethics, provenance,
    client_choice,
    final, archive
])

# Sequential flow from initial assessment to artifact scan
root.order.add_edge(ia, ascan)

# Artifact scan leads to condition mapping and material testing in parallel
root.order.add_edge(ascan, cond)
root.order.add_edge(ascan, mat)

# After material test, either clean or skip
root.order.add_edge(mat, clean)

# Cleaning phase leads to stability check
root.order.add_edge(clean, stable)

# Stability check leads to minor repair or skipping
root.order.add_edge(stable, minor)
root.order.add_edge(stable, skip_client)

# Minor repair leads to structural reinforce and surface restore
root.order.add_edge(minor, struct)
root.order.add_edge(minor, surf)

# Structural reinforce leads to surface restore
root.order.add_edge(struct, surf)

# Surface restore leads to coating apply
root.order.add_edge(surf, coating)

# Coating apply leads to ethics review
root.order.add_edge(coating, ethics)

# Ethics review leads to provenance verify
root.order.add_edge(ethics, provenance)

# Provenance verify leads to final report
root.order.add_edge(provenance, final)

# Final report leads to archive store
root.order.add_edge(final, archive)