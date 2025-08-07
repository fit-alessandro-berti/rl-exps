import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
cp = Transition(label='Curd Processing')
sa = Transition(label='Salt Application')
mi = Transition(label='Mold Inoculation')
pm = Transition(label='Press Molding')
bs = Transition(label='Brine Soaking')
as_ = Transition(label='Aging Setup')
hc = Transition(label='Humidity Control')
mc = Transition(label='Microbial Check')
pd = Transition(label='Packaging Design')
lp = Transition(label='Label Printing')
tl = Transition(label='Trace Logging')
dp = Transition(label='Distribution Plan')
cr = Transition(label='Customer Review')
ia = Transition(label='Inventory Audit')
sa2 = Transition(label='Sustainability Audit')

# Define the aging sub-process as a partial order
nodes_aging = [as_, hc, mc]
aging = StrictPartialOrder(nodes=nodes_aging)
aging.order.add_edge(as_, hc)
aging.order.add_edge(hc, mc)

# Define the feedback loop: Customer Review then either exit or do IA and SA2 and back to Customer Review
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[cr, ia])

# Assemble the root process
root = StrictPartialOrder(nodes=[
    ms, qt, cp, sa, mi, pm, bs, aging,
    pd, lp, tl, dp, loop_feedback, ia, sa2
])

# Define the sequence of activities
root.order.add_edge(ms, qt)
root.order.add_edge(qt, cp)
root.order.add_edge(cp, sa)
root.order.add_edge(sa, mi)
root.order.add_edge(mi, pm)
root.order.add_edge(pm, bs)
root.order.add_edge(bs, aging)
root.order.add_edge(aging, pd)
root.order.add_edge(pd, lp)
root.order.add_edge(lp, tl)
root.order.add_edge(tl, dp)
root.order.add_edge(dp, loop_feedback)

# Define the feedback loop edge
root.order.add_edge(loop_feedback, ia)
root.order.add_edge(ia, sa2)

print(root)