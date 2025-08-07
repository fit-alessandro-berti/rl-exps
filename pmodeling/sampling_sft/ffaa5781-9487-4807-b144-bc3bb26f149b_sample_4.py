import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
pc = Transition(label='Provenance Check')
rt = Transition(label='Radiocarbon Test')
ma = Transition(label='Material Analysis')
ms = Transition(label='Microscopic Scan')
er = Transition(label='Expert Review')
cv = Transition(label='Context Validation')
la = Transition(label='Legal Audit')
ev = Transition(label='Export Verify')
di = Transition(label='Digital Imaging')
md = Transition(label='3D Modeling')
cm = Transition(label='Consensus Meeting')
fa = Transition(label='Final Approval')
ce = Transition(label='Catalog Entry')
vs = Transition(label='Virtual Setup')
ab = Transition(label='Archival Backup')

# Build the loop body: Expert Review -> Context Validation -> Legal Audit -> Export Verify
body = StrictPartialOrder(nodes=[er, cv, la, ev])
body.order.add_edge(er, cv)
body.order.add_edge(cv, la)
body.order.add_edge(la, ev)

# Loop: perform body once, then optionally repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, SilentTransition()])

# Assemble the full process as a partial order
root = StrictPartialOrder(nodes=[
    pc, rt, ma, ms, loop,
    di, md,
    cm, fa, ce, vs, ab
])

# Define the control-flow dependencies
root.order.add_edge(pc, rt)
root.order.add_edge(pc, ma)
root.order.add_edge(pc, ms)

root.order.add_edge(rt, loop)
root.order.add_edge(ma, loop)
root.order.add_edge(ms, loop)

root.order.add_edge(loop, di)
root.order.add_edge(loop, md)

root.order.add_edge(di, cm)
root.order.add_edge(md, cm)

root.order.add_edge(cm, fa)
root.order.add_edge(fa, ce)
root.order.add_edge(ce, vs)
root.order.add_edge(vs, ab)