import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
er = Transition(label='Expert Review')
la = Transition(label='Legal Audit')
cr = Transition(label='Condition Report')
cd = Transition(label='Carbon Dating')
ov = Transition(label='Ownership Verify')
hm = Transition(label='Historical Match')
cc = Transition(label='Customs Clearance')
ra = Transition(label='Risk Assessment')
ea = Transition(label='Ethics Approval')
rp = Transition(label='Restoration Plan')
fa = Transition(label='Final Approval')
ce = Transition(label='Catalog Entry')
ep = Transition(label='Exhibit Prep')

# Loop for cross-departmental reviews
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[la, er, cc, oa, cr, cd, ov, hm, ra, ea]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, ms, loop, rp, fa, ce, ep
])

# Define the control-flow edges
root.order.add_edge(pc, ms)
root.order.add_edge(ms, loop)
root.order.add_edge(loop, rp)
root.order.add_edge(rp, fa)
root.order.add_edge(fa, ce)
root.order.add_edge(ce, ep)