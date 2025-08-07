import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ts = Transition(label='Trend Scan')
ih = Transition(label='Idea Harvest')
sm = Transition(label='Sector Match')
bh = Transition(label='Brainstorm Hub')
cf = Transition(label='Concept Filter')
pb = Transition(label='Prototype Build')
ht = Transition(label='Hybrid Testing')
ss = Transition(label='Stakeholder Sync')
ra = Transition(label='Risk Assess')
sm2 = Transition(label='Scenario Map')
sa = Transition(label='Strategy Align')
pl = Transition(label='Pilot Launch')
dc = Transition(label='Data Capture')
ms = Transition(label='Market Sense')
sp = Transition(label='Scale Plan')

# Loop for iterative feedback: do Hybrid Testing, then either exit or do Stakeholder Sync and Hybrid Testing again
loop_feedback = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ht, OperatorPOWL(operator=Operator.XOR, children=[SilentTransition(), ss])]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ts, ih, sm, bh, cf, pb, loop_feedback, sa, ra, sm2, pl, dc, ms, sp
])

# Sequence of activities
root.order.add_edge(ts, ih)
root.order.add_edge(ih, sm)
root.order.add_edge(sm, bh)
root.order.add_edge(bh, cf)
root.order.add_edge(cf, pb)
root.order.add_edge(pb, loop_feedback)
root.order.add_edge(loop_feedback, sa)
root.order.add_edge(sa, ra)
root.order.add_edge(ra, sm2)
root.order.add_edge(sm2, pl)
root.order.add_edge(pl, dc)
root.order.add_edge(dc, ms)
root.order.add_edge(ms, sp)