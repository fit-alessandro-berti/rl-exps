import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
rt = Transition(label='Radiocarbon Test')
sr = Transition(label='Stylistic Review')
ec = Transition(label='Expert Consult')
da = Transition(label='Document Audit')
lv = Transition(label='Legal Verify')
cr = Transition(label='Condition Report')
df = Transition(label='Discrepancy Flag')
re = Transition(label='Re-examination')
asr = Transition(label='Alternative Source')
av = Transition(label='Acquisition Vote')
ce = Transition(label='Catalog Entry')
ep = Transition(label='Exhibit Plan')
fa = Transition(label='Final Approval')

# Loop for discrepancies: do Discrepancy Flag, then either exit or do Re-examination then Discrepancy Flag again
discrepancy_loop = OperatorPOWL(operator=Operator.LOOP, children=[df, re])

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, ms, rt, sr, ec, da, lv, cr, discrepancy_loop,
    asr, av, ce, ep, fa
])

# Define the control-flow edges
root.order.add_edge(pc, ms)
root.order.add_edge(ms, rt)
root.order.add_edge(rt, sr)
root.order.add_edge(sr, ec)
root.order.add_edge(ec, da)
root.order.add_edge(da, lv)
root.order.add_edge(lv, cr)
root.order.add_edge(cr, discrepancy_loop)
root.order.add_edge(discrepancy_loop, asr)
root.order.add_edge(asr, discrepancy_loop)
root.order.add_edge(asr, av)
root.order.add_edge(av, ce)
root.order.add_edge(ce, ep)
root.order.add_edge(ep, fa)