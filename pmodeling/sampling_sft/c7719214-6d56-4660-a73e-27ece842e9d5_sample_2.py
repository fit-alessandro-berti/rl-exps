import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
ms = Transition(label='Milk Sourcing')
dm = Transition(label='Diet Monitoring')
cs = Transition(label='Culture Selection')
mp = Transition(label='Milk Pasteurize')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Draining')
mi = Transition(label='Mold Inoculate')
pf = Transition(label='Press Forming')
sa = Transition(label='Salt Application')
asup = Transition(label='Aging Setup')
hc = Transition(label='Humidity Control')
ft = Transition(label='Flavor Testing')
pd = Transition(label='Packaging Design')
op = Transition(label='Order Processing')
rd = Transition(label='Retail Delivery')
ec = Transition(label='Event Coordination')
fr = Transition(label='Feedback Review')

# Define the aging loop: Aging Setup -> Humidity Control repeated until exit
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[asup, hc]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, dm, cs, mp, cc, wd, mi, pf, sa, aging_loop,
    ft, pd, op, rd, ec, fr
])

# Define the overall flow order
root.order.add_edge(ms, dm)
root.order.add_edge(dm, cs)
root.order.add_edge(cs, mp)
root.order.add_edge(mp, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, mi)
root.order.add_edge(mi, pf)
root.order.add_edge(pf, sa)
root.order.add_edge(sa, aging_loop)
root.order.add_edge(aging_loop, ft)
root.order.add_edge(ft, pd)
root.order.add_edge(pd, op)
root.order.add_edge(op, rd)
root.order.add_edge(rd, ec)
root.order.add_edge(ec, fr)

print(root)