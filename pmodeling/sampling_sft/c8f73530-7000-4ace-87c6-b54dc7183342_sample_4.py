import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
mp = Transition(label='Milk Pasteurize')
ci = Transition(label='Culture Inoculate')
co = Transition(label='Coagulation')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Drain')
pr = Transition(label='Pressing')
sa = Transition(label='Salting')
ac = Transition(label='Aging Control')
saud = Transition(label='Sensory Audit')
pd = Transition(label='Packaging Design')
la = Transition(label='Label Approval')
oc = Transition(label='Order Customization')
lp = Transition(label='Logistics Plan')
md = Transition(label='Market Delivery')
cf = Transition(label='Customer Feedback')
rc = Transition(label='Regulatory Check')

# Define the sensory evaluation loop: do sensory audit, then either exit or repeat
sensory_loop = OperatorPOWL(operator=Operator.LOOP, children=[saud, SilentTransition()])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    ms, qt, mp, ci, co, cc, wd, pr, sa, ac, sensory_loop,
    pd, la, oc, lp, md, cf, rc
])

# Add edges
root.order.add_edge(ms, qt)
root.order.add_edge(qt, mp)
root.order.add_edge(mp, ci)
root.order.add_edge(ci, co)
root.order.add_edge(co, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, pr)
root.order.add_edge(pr, sa)
root.order.add_edge(sa, ac)
root.order.add_edge(ac, sensory_loop)
root.order.add_edge(sensory_loop, pd)
root.order.add_edge(pd, la)
root.order.add_edge(la, oc)
root.order.add_edge(oc, lp)
root.order.add_edge(lp, md)
root.order.add_edge(md, cf)
root.order.add_edge(cf, rc)