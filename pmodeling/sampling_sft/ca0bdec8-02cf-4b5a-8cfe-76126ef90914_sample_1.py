import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
cp = Transition(label='Culture Prep')
mp = Transition(label='Milk Pasteurize')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Draining')
mc = Transition(label='Molding Cheese')
pb = Transition(label='Pressing Blocks')
sp = Transition(label='Salting Process')
am = Transition(label='Aging Monitoring')
fp = Transition(label='Flavor Profiling')
pd = Transition(label='Packaging Design')
ccs = Transition(label='Compliance Check')
mr = Transition(label='Market Research')
ds = Transition(label='Direct Shipping')
cf = Transition(label='Customer Feedback')
ra = Transition(label='Recipe Adjust')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    ms, qt, cp, mp, cc, wd, mc, pb, sp, am, fp, pd, ccs, mr, ds, cf, ra
])

# Sequential milk sourcing to quality testing
root.order.add_edge(ms, qt)

# After quality testing, parallelize culture prep & milk pasteurize
root.order.add_edge(qt, cp)
root.order.add_edge(qt, mp)

# Both culture prep and milk pasteurize must complete before curd cutting
root.order.add_edge(cp, cc)
root.order.add_edge(mp, cc)

# Curd cutting leads to whey draining and molding cheese
root.order.add_edge(cc, wd)
root.order.add_edge(cc, mc)

# Whey draining and molding cheese are concurrent before pressing blocks
root.order.add_edge(wd, pb)
root.order.add_edge(mc, pb)

# Pressing blocks must finish before salting process
root.order.add_edge(pb, sp)

# Salting process must finish before aging monitoring
root.order.add_edge(sp, am)

# Aging monitoring leads to flavor profiling and packaging design
root.order.add_edge(am, fp)
root.order.add_edge(am, pd)

# Flavor profiling and packaging design can happen in parallel
root.order.add_edge(fp, pd)

# After packaging, compliance check and market research must be done
root.order.add_edge(pd, ccs)
root.order.add_edge(pd, mr)

# Compliance check and market research are concurrent before shipping
root.order.add_edge(ccs, ds)
root.order.add_edge(mr, ds)

# Shipping leads to customer feedback and recipe adjustment
root.order.add_edge(ds, cf)
root.order.add_edge(ds, ra)

# Customer feedback and recipe adjustment are optional after shipping
root.order.add_edge(cf, ra)

# Finally, feedback loops back to milk sourcing to start again
root.order.add_edge(ra, ms)