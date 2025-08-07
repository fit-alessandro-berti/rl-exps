import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
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

# Build the main production‐cycle partial order A
A = StrictPartialOrder(nodes=[
    ms, fd, ac, bs, aa, ca, qi, bu,
    df, pa, cr, lp, ds, cf, pr, ra
])
# Material sourcing -> forager dispatch -> authenticity check -> batch scheduling
A.order.add_edge(ms, fd)
A.order.add_edge(fd, ac)
A.order.add_edge(ac, bs)
# Then allocate artisans and start assembly, concurrent with blockchain update
A.order.add_edge(bs, aa)
A.order.add_edge(aa, ca)
A.order.add_edge(ac, bu)
# After assembly, quality inspection and then blockchain update
A.order.add_edge(ca, qi)
A.order.add_edge(qi, bu)

# Loop: after each cycle, do demand forecast, price adjustment, compliance review
loop_body = StrictPartialOrder(nodes=[
    df, pa, cr
])
loop_body.order.add_edge(df, pa)
loop_body.order.add_edge(pa, cr)
# then seasonal review, and refinement, and reputation audit
loop_body.nodes += [sr, pr, ra]
loop_body.order.add_edge(cr, sr)
loop_body.order.add_edge(sr, pr)
loop_body.order.add_edge(pr, ra)

# LOOP: do the production‐cycle A, then either exit or do the loop_body then A again
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, loop_body])

# Assemble the root partial order
root = StrictPartialOrder(nodes=[loop, ds, cf])
root.order.add_edge(loop, ds)
root.order.add_edge(ds, cf)