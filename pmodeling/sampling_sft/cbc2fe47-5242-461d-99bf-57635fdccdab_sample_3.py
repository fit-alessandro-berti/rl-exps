import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ti = Transition(label='Artifact Intake')
dc = Transition(label='Document Check')
ps = Transition(label='Provenance Search')
ov = Transition(label='Ownership Validate')
rt = Transition(label='Radiocarbon Test')
ss = Transition(label='Spectroscopy Scan')
ma = Transition(label='Material Analysis')
sa = Transition(label='Style Assessment')
cr = Transition(label='Context Review')
ep = Transition(label='Expert Panel')
rd = Transition(label='Report Draft')
qr = Transition(label='Quality Review')
ce = Transition(label='Catalog Entry')
isup = Transition(label='Insurance Setup')
ar = Transition(label='Archive Data')
rtg = Transition(label='Reevaluation Trigger')

# Loop for periodic re-evaluation: repeat Archive Data then Reevaluation Trigger
loop = OperatorPOWL(operator=Operator.LOOP, children=[ar, rtg])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ti, dc, ps, ov, rt, ss, ma, sa, cr, ep, rd, qr, ce, isup, loop
])

# Initial intake and document check are concurrent
root.order.add_edge(ti, dc)

# After intake and document check, do provenance and ownership validation in parallel
root.order.add_edge(dc, ps)
root.order.add_edge(dc, ov)

# After provenance and ownership, run all scientific tests in parallel
root.order.add_edge(ps, rt)
root.order.add_edge(ps, ss)
root.order.add_edge(ps, ma)

# After all tests, run style and context assessment in parallel
root.order.add_edge(rt, sa)
root.order.add_edge(ss, sa)
root.order.add_edge(ma, sa)
root.order.add_edge(sa, cr)

# After style and context, the expert panel meets
root.order.add_edge(cr, ep)

# After the panel, draft the report
root.order.add_edge(ep, rd)

# After the report, do quality review and either catalog or insurance setup
root.order.add_edge(rd, qr)
root.order.add_edge(qr, [ce, isup])

# Finally, include the periodic re-evaluation loop
root.order.add_edge(qr, loop)