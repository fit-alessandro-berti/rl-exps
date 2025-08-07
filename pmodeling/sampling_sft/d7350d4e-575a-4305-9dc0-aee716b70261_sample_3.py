import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
pc = Transition(label='Provenance Check')
sc = Transition(label='Sample Collection')
st = Transition(label='Spectroscopy Test')
cd = Transition(label='Carbon Dating')
er = Transition(label='Expert Review')
lc = Transition(label='Legal Clearance')
ca = Transition(label='Cultural Assessment')
ds = Transition(label='Digital Scan')
rd = Transition(label='Report Draft')
sm = Transition(label='Stakeholder Meet')
av = Transition(label='Acquisition Vote')
rp = Transition(label='Restoration Plan')
cr = Transition(label='Condition Report')
ae = Transition(label='Archival Entry')
fa = Transition(label='Final Approval')

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, sc, st, cd, er, lc, ca, ds, rd,
    sm, av, rp, cr, ae, fa
])

# Add the control-flow dependencies
root.order.add_edge(pc, sc)
root.order.add_edge(sc, st)
root.order.add_edge(sc, cd)
root.order.add_edge(st, er)
root.order.add_edge(cd, er)
root.order.add_edge(er, lc)
root.order.add_edge(lc, ca)
root.order.add_edge(ca, ds)
root.order.add_edge(ds, rd)
root.order.add_edge(rd, sm)
root.order.add_edge(sm, av)
root.order.add_edge(av, rp)
root.order.add_edge(rp, cr)
root.order.add_edge(cr, ae)
root.order.add_edge(ae, fa)

print(root)