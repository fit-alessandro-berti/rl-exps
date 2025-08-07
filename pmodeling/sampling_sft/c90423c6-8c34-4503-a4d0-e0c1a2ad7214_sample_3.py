import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
fs = Transition(label='Farm Selection')
st = Transition(label='Sample Testing')
tn = Transition(label='Trade Negotiation')
mls = Transition(label='Micro-Lot Sorting')
fc = Transition(label='Fermentation Control')
sp = Transition(label='Sensory Profiling')
rc = Transition(label='Roast Calibration')
bc = Transition(label='Blend Creation')
sa = Transition(label='Sustainability Audit')
pd = Transition(label='Packaging Design')
qi = Transition(label='Quality Inspection')
isyn = Transition(label='Inventory Sync')
lp = Transition(label='Logistics Planning')
ct = Transition(label='Cafe Training')
dp = Transition(label='Dynamic Pricing')
cf = Transition(label='Customer Feedback')
tl = Transition(label='Traceability Logging')

# Loop for continuous quality and feedback
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[qi, cf])

# Build the partial order
root = StrictPartialOrder(nodes=[
    fs, st, tn, mls, fc, sp, rc, bc, sa, pd, isyn, lp, ct, dp, quality_loop, tl
])

# Main flow edges
root.order.add_edge(fs, st)
root.order.add_edge(st, tn)
root.order.add_edge(tn, mls)
root.order.add_edge(mls, fc)
root.order.add_edge(fc, sp)
root.order.add_edge(sp, rc)
root.order.add_edge(rc, bc)
root.order.add_edge(bc, sa)
root.order.add_edge(sa, pd)
root.order.add_edge(pd, isyn)
root.order.add_edge(isyn, lp)
root.order.add_edge(lp, ct)
root.order.add_edge(ct, dp)
root.order.add_edge(dp, quality_loop)

# Loop for continuous quality and feedback
root.order.add_edge(quality_loop, tl)