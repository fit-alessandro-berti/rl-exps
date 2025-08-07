import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ts = Transition(label='Trend Sensing')
ifusion = Transition(label='Idea Fusion')
pb = Transition(label='Prototype Build')
er = Transition(label='Expert Review')
ft = Transition(label='Field Testing')
ua = Transition(label='User Profiling')
ic = Transition(label='IP Analysis')
cc = Transition(label='Compliance Check')
ps = Transition(label='Partner Setup')
lp = Transition(label='Launch Prep')
fl = Transition(label='Feedback Loop')
sp = Transition(label='Scale Planning')
ra = Transition(label='Risk Assess')
ds = Transition(label='Demand Scan')

# Loop for iterative testing and feedback
# Body A: Field Testing -> Expert Review -> User Profiling
body_a = StrictPartialOrder(nodes=[ft, er, ua])
body_a.order.add_edge(ft, er)
body_a.order.add_edge(er, ua)

# Loop B: Risk Assess -> Demand Scan
body_b = StrictPartialOrder(nodes=[ra, ds])
body_b.order.add_edge(ra, ds)

# Concurrent loop: do body_a, then optionally do body_b, then body_a again, etc.
loop = OperatorPOWL(operator=Operator.LOOP, children=[body_a, body_b])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ts, ifusion, pb, loop,
    ic, cc, ps,
    lp, fl, sp
])

# Define the control‐flow dependencies
root.order.add_edge(ts, ifusion)
root.order.add_edge(ifusion, pb)
root.order.add_edge(pb, loop)
root.order.add_edge(loop, ic)
root.order.add_edge(loop, cc)
root.order.add_edge(loop, ps)
root.order.add_edge(ic, lp)
root.order.add_edge(cc, lp)
root.order.add_edge(ps, lp)
root.order.add_edge(lp, fl)
root.order.add_edge(lp, sp)