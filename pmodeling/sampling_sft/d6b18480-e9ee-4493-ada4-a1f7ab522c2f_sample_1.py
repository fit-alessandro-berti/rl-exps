import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms = Transition(label='Material Sourcing')
fd = Transition(label='Forager Dispatch')
ac = Transition(label='Authenticity Check')
bs = Transition(label='Batch Scheduling')
aa = Transition(label='Artisan Allocation')
ca = Transition(label='Craft Assembly')
qi = Transition(label='Quality Inspection')
bu = Transition(label='Blockchain Update')
df = Transition(label='Demand Forecast')
pa = Transition(label='Price Adjustment')
cr = Transition(label='Compliance Review')
lp = Transition(label='Logistics Planning')
ds = Transition(label='Distributor Sync')
cf = Transition(label='Customer Feedback')
pr = Transition(label='Product Refinement')
ra = Transition(label='Reputation Audit')
sr = Transition(label='Seasonal Review')

# Define the core assembly‐inspection loop: Assembly → Inspection → Blockchain Update
loop_body = StrictPartialOrder(nodes=[ca, qi, bu])
loop_body.order.add_edge(ca, qi)
loop_body.order.add_edge(qi, bu)

# Define the loop: do Assembly → Inspection → Blockchain Update, then either exit or do Seasonal Review then back to body
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, sr])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ms, fd, ac, bs, aa, loop, df, pa, cr, lp, ds, cf, pr, ra
])

# Add control-flow edges
root.order.add_edge(ms, fd)
root.order.add_edge(fd, ac)
root.order.add_edge(ac, bs)
root.order.add_edge(bs, aa)
root.order.add_edge(aa, loop)
root.order.add_edge(loop, df)
root.order.add_edge(df, pa)
root.order.add_edge(pa, cr)
root.order.add_edge(cr, lp)
root.order.add_edge(lp, ds)
root.order.add_edge(ds, cf)
root.order.add_edge(cf, pr)
root.order.add_edge(pr, ra)

# Optionally, if you want to explicitly show the refinement‐audit‐refinement cycle:
# root.order.add_edge(ra, pr)