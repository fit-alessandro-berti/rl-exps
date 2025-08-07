import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ov = Transition(label='Order Validate')
ro = Transition(label='Route Optimize')
da = Transition(label='Drone Assign')
pc = Transition(label='Preflight Check')
lp = Transition(label='Load Package')
fl = Transition(label='Flight Launch')
tm = Transition(label='Traffic Monitor')
wa = Transition(label='Weather Assess')
oa = Transition(label='Obstacle Avoid')
bc = Transition(label='Battery Check')
dv = Transition(label='Delivery Verify')
bs = Transition(label='Biometric Scan')
pr = Transition(label='Package Release')
rf = Transition(label='Return Flight')
pf = Transition(label='Post Flight')
da1 = Transition(label='Data Analyze')
fc = Transition(label='Feedback Collect')

# Build the loop body for in-flight monitoring
in_flight_loop = StrictPartialOrder(nodes=[tm, wa, oa, bc])
# No edges => all activities are concurrent

# Build the monitoring loop: Traffic Monitor, Weather Assess, Obstacle Avoid, Battery Check
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[in_flight_loop, in_flight_loop])

# Build the main delivery sequence as a partial order
delivery_seq = StrictPartialOrder(nodes=[
    ov, ro, da, pc, lp, fl, monitor_loop,
    dv, bs, pr, rf, pf, da1, fc
])
delivery_seq.order.add_edge(ov, ro)
delivery_seq.order.add_edge(ro, da)
delivery_seq.order.add_edge(da, pc)
delivery_seq.order.add_edge(pc, lp)
delivery_seq.order.add_edge(lp, fl)
delivery_seq.order.add_edge(fl, monitor_loop)
delivery_seq.order.add_edge(monitor_loop, dv)
delivery_seq.order.add_edge(dv, bs)
delivery_seq.order.add_edge(bs, pr)
delivery_seq.order.add_edge(pr, rf)
delivery_seq.order.add_edge(rf, pf)
delivery_seq.order.add_edge(pf, da1)
delivery_seq.order.add_edge(da1, fc)

# The root model: start with order validation and proceed with the main delivery sequence
root = StrictPartialOrder(nodes=[ov, delivery_seq, da1])
root.order.add_edge(ov, delivery_seq)
root.order.add_edge(delivery_seq, da1)

print(root)