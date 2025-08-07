import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Define the loop for iterative product refinement
# Body of the loop: refine → audit → feedback → price → compliance → logistics → sync
refine = StrictPartialOrder(nodes=[pr, ra])
refine.order.add_edge(pr, ra)
feedback = StrictPartialOrder(nodes=[cf])
feedback.order.add_edge(cf, pa)
compliance = StrictPartialOrder(nodes=[cr, lp, ds])
compliance.order.add_edge(cr, lp)
compliance.order.add_edge(lp, ds)
body = StrictPartialOrder(nodes=[refine, feedback, pa, compliance, lp, ds])
body.order.add_edge(refine, feedback)
body.order.add_edge(feedback, pa)
body.order.add_edge(pa, compliance)
body.order.add_edge(compliance, lp)
body.order.add_edge(lp, ds)

# Loop: do seasonal review, then either exit or repeat body
loop = OperatorPOWL(operator=Operator.LOOP, children=[sr, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[ms, fd, ac, bs, aa, ca, qi, bu, df, loop])
# Material sourcing, forager dispatch, authenticity check, batch scheduling, artisan allocation
root.order.add_edge(ms, ac)
root.order.add_edge(ac, bs)
root.order.add_edge(bs, aa)
root.order.add_edge(aa, ca)
# Quality inspection and blockchain update follow assembly
root.order.add_edge(ca, qi)
root.order.add_edge(qi, bu)
# Demand forecast and price adjustment follow blockchain update
root.order.add_edge(bu, df)
root.order.add_edge(df, pa)
# The loop follows demand forecast
root.order.add_edge(df, loop)