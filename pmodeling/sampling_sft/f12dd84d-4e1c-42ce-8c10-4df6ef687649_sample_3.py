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
asup = Transition(label='Aging Setup')
hc = Transition(label='Humidity Control')
mc = Transition(label='Microbial Check')
pd = Transition(label='Packaging Design')
lp = Transition(label='Label Printing')
tl = Transition(label='Trace Logging')
dp = Transition(label='Distribution Plan')
cr = Transition(label='Customer Review')
ia = Transition(label='Inventory Audit')
sa2 = Transition(label='Sustainability Audit')

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, qt, cp, sa, mi, pm, bs,
    asup, hc, mc, pd, lp, tl, dp, cr,
    ia, sa2
])

# Sequential flow
root.order.add_edge(ms, qt)
root.order.add_edge(qt, cp)
root.order.add_edge(cp, sa)
root.order.add_edge(sa, mi)
root.order.add_edge(mi, pm)
root.order.add_edge(pm, bs)

# Aging setup and controls
root.order.add_edge(asup, hc)
root.order.add_edge(asup, mc)
root.order.add_edge(hc, pd)
root.order.add_edge(mc, pd)

# Packaging and trace logging
root.order.add_edge(pd, lp)
root.order.add_edge(lp, tl)

# Distribution and review
root.order.add_edge(tl, dp)
root.order.add_edge(dp, cr)

# Audits
root.order.add_edge(cr, ia)
root.order.add_edge(ia, sa2)