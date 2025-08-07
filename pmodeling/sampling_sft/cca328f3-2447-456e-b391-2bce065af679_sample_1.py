import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
ai = Transition(label='Artifact Intake')
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
sc = Transition(label='Style Compare')
dc = Transition(label='Digital Capture')
er = Transition(label='Expert Review')
ds = Transition(label='Database Search')
la = Transition(label='Legal Audit')
ca = Transition(label='Cultural Assess')
dsyn = Transition(label='Data Synthesis')
rd = Transition(label='Report Draft')
asr = Transition(label='Archival Store')
da = Transition(label='Display Approve')
ln = Transition(label='Lender Notify')
ifg = Transition(label='Investigation Flag')

# Build the loop for expert review and further checks
expert_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[er, ds]
)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    ai, pc, ms, sc, dc,
    expert_loop,
    ca, la, ds,
    dsyn, rd, asr,
    da, ln, ifg
])

# Define the control-flow dependencies
root.order.add_edge(ai, pc)
root.order.add_edge(ai, ms)
root.order.add_edge(ai, dc)

root.order.add_edge(pc, expert_loop)
root.order.add_edge(ms, expert_loop)
root.order.add_edge(dc, expert_loop)

root.order.add_edge(expert_loop, ca)
root.order.add_edge(expert_loop, la)

root.order.add_edge(ca, dsyn)
root.order.add_edge(la, dsyn)

root.order.add_edge(dsyn, rd)
root.order.add_edge(rd, asr)

root.order.add_edge(asr, da)
root.order.add_edge(asr, ln)
root.order.add_edge(asr, ifg)

# Print the root model for verification
print(root)