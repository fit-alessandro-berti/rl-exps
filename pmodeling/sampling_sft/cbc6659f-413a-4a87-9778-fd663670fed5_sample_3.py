import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Loop for cross-departmental review: Provenance Check -> (Legal Audit + Expert Review) -> repeat
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[la, er]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, ms, loop, cr, cd, ov, hm, cc, ra, ea, rp, fa, ce, ep
])

# Define the control-flow order
root.order.add_edge(pc, ms)
root.order.add_edge(ms, loop)
root.order.add_edge(loop, cr)
root.order.add_edge(loop, cd)
root.order.add_edge(loop, ov)
root.order.add_edge(loop, hm)
root.order.add_edge(loop, cc)
root.order.add_edge(loop, ra)
root.order.add_edge(loop, ea)
root.order.add_edge(cd, rp)
root.order.add_edge(ov, rp)
root.order.add_edge(hm, rp)
root.order.add_edge(cc, rp)
root.order.add_edge(ra, rp)
root.order.add_edge(ea, rp)
root.order.add_edge(rp, fa)
root.order.add_edge(fa, ce)
root.order.add_edge(ce, ep)