import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the atomic activities
ms = Transition(label='Milk Sourcing')
cs = Transition(label='Culture Selection')
mt = Transition(label='Milk Testing')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Draining')
mi = Transition(label='Mold Inoculation')
fc = Transition(label='Forming Cheese')
ss = Transition(label='Salting Stage')
asup = Transition(label='Aging Setup')
cc1 = Transition(label='Climate Control')
qt = Transition(label='Quality Tasting')
pp = Transition(label='Packaging Prep')
lp = Transition(label='Label Printing')
dp = Transition(label='Distribution Plan')
rd = Transition(label='Retail Delivery')
ec = Transition(label='Event Coordination')
ra = Transition(label='Regulatory Audit')

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, cs, mt, cc, wd, mi, fc, ss,
    asup, cc1, qt, pp, lp, dp,
    rd, ec, ra
])

# Define the control-flow dependencies
root.order.add_edge(ms, cs)
root.order.add_edge(cs, mt)
root.order.add_edge(mt, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, mi)
root.order.add_edge(mi, fc)
root.order.add_edge(fc, ss)
root.order.add_edge(ss, asup)
root.order.add_edge(asup, cc1)
root.order.add_edge(asup, qt)
root.order.add_edge(cc1, qt)
root.order.add_edge(qt, pp)
root.order.add_edge(pp, lp)
root.order.add_edge(lp, dp)
root.order.add_edge(dp, rd)
root.order.add_edge(rd, ec)
root.order.add_edge(ec, ra)

# Final regulatory audit must follow all other activities
for node in [ms, cs, mt, cc, wd, mi, fc, ss, asup, cc1, qt, pp, lp, dp]:
    root.order.add_edge(node, ra)