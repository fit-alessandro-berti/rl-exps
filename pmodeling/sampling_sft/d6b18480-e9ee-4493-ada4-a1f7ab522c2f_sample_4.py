import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Build the loop body: after each activity, optionally do a feedback refinement
body = StrictPartialOrder(nodes=[cf, pr])
body.order.add_edge(cf, pr)

# Loop: do Material Sourcing, then optionally do the body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[ms, body])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    loop, fd, ac, bs, aa, ca, qi, bu,
    df, pa, cr, lp, ds,
    ra, sr
])

# Sequential dependencies
root.order.add_edge(loop, fd)
root.order.add_edge(fd, ac)
root.order.add_edge(ac, bs)
root.order.add_edge(bs, aa)
root.order.add_edge(aa, ca)
root.order.add_edge(ca, qi)
root.order.add_edge(qi, bu)
root.order.add_edge(bu, df)
root.order.add_edge(df, pa)
root.order.add_edge(pa, cr)
root.order.add_edge(cr, lp)
root.order.add_edge(lp, ds)
root.order.add_edge(ds, ra)
root.order.add_edge(ra, sr)