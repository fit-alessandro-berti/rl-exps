import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the atomic activities
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
rt = Transition(label='Radiocarbon Test')
dc = Transition(label='Database Query')
sp = Transition(label='Style Compare')
bp = Transition(label='Blockchain Prep')
lr = Transition(label='Legal Review')
oa = Transition(label='Ownership Audit')
cp = Transition(label='Conservation Plan')
ep = Transition(label='Expert Panel')
rd = Transition(label='Report Draft')
cr = Transition(label='Client Review')
asub = Transition(label='Authority Submit')
esetup = Transition(label='Exhibit Setup')
fa = Transition(label='Final Approval')

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, ms, rt, dc, sp,
    bp, lr, oa, cp,
    ep, rd, cr, asub,
    esetup, fa
])

# Order dependencies
root.order.add_edge(pc, ms)
root.order.add_edge(pc, rt)
root.order.add_edge(ms, dc)
root.order.add_edge(rt, dc)
root.order.add_edge(dc, sp)
root.order.add_edge(ms, bp)
root.order.add_edge(rt, bp)
root.order.add_edge(dc, bp)
root.order.add_edge(bp, lr)
root.order.add_edge(lr, oa)
root.order.add_edge(oa, cp)
root.order.add_edge(cp, ep)
root.order.add_edge(ep, rd)
root.order.add_edge(rd, cr)
root.order.add_edge(cr, asub)
root.order.add_edge(asub, esetup)
root.order.add_edge(esetup, fa)

print(root)