import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms = Transition(label='Milk Sourcing')
dm = Transition(label='Diet Monitoring')
cs = Transition(label='Culture Selection')
mp = Transition(label='Milk Pasteurize')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Draining')
mi = Transition(label='Mold Inoculate')
pf = Transition(label='Press Forming')
sa = Transition(label='Salt Application')
asg = Transition(label='Aging Setup')
hc = Transition(label='Humidity Control')
ft = Transition(label='Flavor Testing')
pd = Transition(label='Packaging Design')
op = Transition(label='Order Processing')
rd = Transition(label='Retail Delivery')
ec = Transition(label='Event Coordination')
fr = Transition(label='Feedback Review')

# Define the aging sub‐process as a partial order
aging = StrictPartialOrder(nodes=[asg, hc, ft])
aging.order.add_edge(asg, hc)
aging.order.add_edge(hc, ft)

# Define the loop for repeated aging and feedback
loop = OperatorPOWL(operator=Operator.LOOP, children=[aging, fr])

# Build the overall supply chain process as a strict partial order
root = StrictPartialOrder(nodes=[
    ms, dm, cs, mp, cc, wd, mi, pf, sa, loop, pd, op, rd, ec
])

# Define the control‐flow dependencies
root.order.add_edge(ms, dm)
root.order.add_edge(dm, cs)
root.order.add_edge(cs, mp)
root.order.add_edge(mp, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, mi)
root.order.add_edge(mi, pf)
root.order.add_edge(pf, sa)
root.order.add_edge(sa, loop)
root.order.add_edge(loop, pd)
root.order.add_edge(pd, op)
root.order.add_edge(op, rd)
root.order.add_edge(rd, ec)