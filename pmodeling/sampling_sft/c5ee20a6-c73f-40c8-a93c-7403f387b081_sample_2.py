import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ia = Transition(label='Initial Assess')
cs = Transition(label='Condition Scan')
mt = Transition(label='Material Test')
hc = Transition(label='Historical Check')
pv = Transition(label='Provenance Verify')
ps = Transition(label='Parts Sourcing')
gc = Transition(label='Gentle Clean')
si = Transition(label='Stabilize Item')
sr = Transition(label='Structural Repair')
sf = Transition(label='Surface Finish')
ec = Transition(label='Expert Consult')
ar = Transition(label='Archival Review')
ea = Transition(label='Ethics Audit')
qi = Transition(label='Quality Inspect')
pd = Transition(label='Photo Document')
pp = Transition(label='Packaging Prep')
rg = Transition(label='Report Generate')
cp = Transition(label='Certify Provenance')

# Silent transition for optional expert consultation
skip = SilentTransition()

# Expert consultation with archival review and ethics audit (exclusive choice)
xor = OperatorPOWL(operator=Operator.XOR, children=[ec, skip])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ia, cs, mt, hc, pv, ps, gc, si, sr, sf,
    xor, qi, pd, pp, rg, cp
])

# Define the control-flow dependencies
root.order.add_edge(ia, cs)
root.order.add_edge(ia, mt)
root.order.add_edge(ia, hc)
root.order.add_edge(ia, pv)

root.order.add_edge(cs, gc)
root.order.add_edge(mt, gc)
root.order.add_edge(hc, gc)
root.order.add_edge(pv, gc)

root.order.add_edge(gc, si)
root.order.add_edge(si, sr)
root.order.add_edge(sr, sf)

# After stabilization, either do optional expert consultation or skip
root.order.add_edge(si, xor)
root.order.add_edge(xor, qi)

# After quality inspection, proceed to packaging, reporting, and provenance certification
root.order.add_edge(qi, pd)
root.order.add_edge(qi, pp)
root.order.add_edge(pd, rg)
root.order.add_edge(pp, rg)
root.order.add_edge(rg, cp)