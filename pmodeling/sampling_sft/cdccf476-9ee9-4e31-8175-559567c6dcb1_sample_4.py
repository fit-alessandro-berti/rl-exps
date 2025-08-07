import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms = Transition(label='Milk Sourcing')
cf = Transition(label='Curd Formation')
mt = Transition(label='Microbial Test')
wr = Transition(label='Whey Removal')
pc = Transition(label='Pressing Cheese')
sa = Transition(label='Salt Application')
ac = Transition(label='Aging Control')
qc = Transition(label='Quality Check')
ep = Transition(label='Eco Packaging')
il = Transition(label='Inventory Log')
tm = Transition(label='Temp Monitoring')
cb = Transition(label='Carrier Booking')
tr = Transition(label='Trace Recording')
fr = Transition(label='Feedback Review')
ca = Transition(label='Compliance Audit')
ba = Transition(label='Batch Adjustment')
skip = SilentTransition()

# Loop for continuous aging and quality checks
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[ac, qc])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, cf, mt, wr, pc, sa, aging_loop, ep,
    il, tm, cb, tr, fr, ca, ba
])

# Define the control-flow edges
root.order.add_edge(ms, cf)
root.order.add_edge(cf, mt)
root.order.add_edge(mt, wr)
root.order.add_edge(wr, pc)
root.order.add_edge(pc, sa)
root.order.add_edge(sa, aging_loop)
root.order.add_edge(aging_loop, ep)

root.order.add_edge(ep, il)
root.order.add_edge(il, tm)
root.order.add_edge(tm, cb)
root.order.add_edge(cb, tr)
root.order.add_edge(tr, fr)
root.order.add_edge(fr, ca)
root.order.add_edge(ca, ba)