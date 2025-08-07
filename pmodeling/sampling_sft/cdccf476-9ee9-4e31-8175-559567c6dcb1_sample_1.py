import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
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

# Loop for aging control: repeat AC then either exit or do QC, then repeat
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[ac, qc])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ms, cf, mt, wr, pc, sa, aging_loop,
    qc, ep, il, tm, cb, tr, fr, ca
])

# Add the control-flow edges
root.order.add_edge(ms, cf)
root.order.add_edge(cf, mt)
root.order.add_edge(mt, wr)
root.order.add_edge(wr, pc)
root.order.add_edge(pc, sa)
root.order.add_edge(sa, aging_loop)
root.order.add_edge(aging_loop, qc)

# After aging, either QC then loop back or do the rest
root.order.add_edge(qc, ep)
root.order.add_edge(qc, il)
root.order.add_edge(ep, il)
root.order.add_edge(il, tm)
root.order.add_edge(tm, cb)
root.order.add_edge(cb, tr)
root.order.add_edge(tr, fr)
root.order.add_edge(fr, ca)

# Batch adjustment can happen at any point
root.order.add_edge(ca, ba)
root.order.add_edge(ba, ba)