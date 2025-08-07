import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
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
da2 = Transition(label='Data Analyze')
fc = Transition(label='Feedback Collect')

# Define the monitoring loop: Traffic Monitor -> Weather Assess -> Obstacle Avoid -> Battery Check
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[tm, wa, oa, bc])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ov, ro, da, pc, lp, fl, monitor_loop, dv, bs, pr, rf, pf, da2, da, fc
])

# Add edges
root.order.add_edge(ov, ro)
root.order.add_edge(ro, da)
root.order.add_edge(da, pc)
root.order.add_edge(pc, lp)
root.order.add_edge(lp, fl)
root.order.add_edge(fl, monitor_loop)
root.order.add_edge(monitor_loop, dv)
root.order.add_edge(dv, bs)
root.order.add_edge(bs, pr)
root.order.add_edge(pr, rf)
root.order.add_edge(rf, pf)
root.order.add_edge(pf, da2)
root.order.add_edge(da2, da)
root.order.add_edge(da, fc)