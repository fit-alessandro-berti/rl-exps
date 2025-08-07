import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
fs = Transition(label='Farm Selection')
sn = Transition(label='Sample Testing')
tn = Transition(label='Trade Negotiation')
mls = Transition(label='Micro-Lot Sorting')
fc = Transition(label='Fermentation Control')
sp = Transition(label='Sensory Profiling')
rc = Transition(label='Roast Calibration')
bc = Transition(label='Blend Creation')
sa = Transition(label='Sustainability Audit')
pd = Transition(label='Packaging Design')
qi = Transition(label='Quality Inspection')
isync = Transition(label='Inventory Sync')
lp = Transition(label='Logistics Planning')
ct = Transition(label='Cafe Training')
dp = Transition(label='Dynamic Pricing')
cf = Transition(label='Customer Feedback')
tl = Transition(label='Traceability Logging')

# Define the main workflow as a strict partial order
root = StrictPartialOrder(nodes=[fs, sn, tn, mls, fc, sp, rc, bc, sa, pd, qi, isync, lp, ct, dp, cf, tl])

# Sequence: Farm Selection -> Sample Testing -> Trade Negotiation
root.order.add_edge(fs, sn)
root.order.add_edge(sn, tn)

# After negotiation, multiple parallel tasks:
# - Micro-lot sorting -> Fermentation control -> Sensory profiling
root.order.add_edge(tn, mls)
root.order.add_edge(mls, fc)
root.order.add_edge(fc, sp)

# After sensory profiling, blend creation
root.order.add_edge(sp, bc)

# After all preparation, sustainability audit and packaging design are done in parallel
root.order.add_edge(bc, sa)
root.order.add_edge(bc, pd)

# Quality inspection and inventory sync are concurrent
root.order.add_edge(sa, qi)
root.order.add_edge(pd, qi)
root.order.add_edge(qi, isync)

# Logistics planning and cafe training are concurrent
root.order.add_edge(qi, lp)
root.order.add_edge(qi, ct)

# Dynamic pricing and traceability logging are concurrent
root.order.add_edge(lp, dp)
root.order.add_edge(ct, dp)
root.order.add_edge(dp, tl)

# Finally, customer feedback is triggered
root.order.add_edge(dp, cf)