import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms = Transition(label='Milk Sourcing')
fa = Transition(label='Farm Audit')
mt = Transition(label='Milk Testing')
bf = Transition(label='Batch Forming')
cc = Transition(label='Curd Cutting')
mc = Transition(label='Molding Cheese')
sp = Transition(label='Salting Process')
ac = Transition(label='Aging Control')
qc = Transition(label='Quality Check')
pd = Transition(label='Packaging Design')
lp = Transition(label='Label Printing')
iu = Transition(label='Inventory Update')
or_ = Transition(label='Order Receiving')
rc = Transition(label='Retail Coordination')
sp_prep = Transition(label='Shipping Prep')
cf = Transition(label='Customer Feedback')
df = Transition(label='Demand Forecast')
lr = Transition(label='Limited Release')

# Build the loop body: Quality Check -> Packaging Design -> Label Printing -> Inventory Update
body = StrictPartialOrder(nodes=[qc, pd, lp, iu])
body.order.add_edge(qc, pd)
body.order.add_edge(pd, lp)
body.order.add_edge(lp, iu)

# Define the loop: do Quality Check, then optionally do Body, then do Quality Check again
loop = OperatorPOWL(operator=Operator.LOOP, children=[qc, body])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    ms, fa, mt, bf, cc, mc, sp, ac, loop,
    or_, rc, sp_prep, cf, df, lr
])

# Sequential dependencies
root.order.add_edge(ms, fa)
root.order.add_edge(fa, mt)
root.order.add_edge(mt, bf)
root.order.add_edge(bf, cc)
root.order.add_edge(cc, mc)
root.order.add_edge(mc, sp)
root.order.add_edge(sp, ac)
root.order.add_edge(ac, loop)
root.order.add_edge(loop, or_)
root.order.add_edge(or_, rc)
root.order.add_edge(rc, sp_prep)
root.order.add_edge(sp_prep, cf)
root.order.add_edge(cf, df)
root.order.add_edge(df, lr)