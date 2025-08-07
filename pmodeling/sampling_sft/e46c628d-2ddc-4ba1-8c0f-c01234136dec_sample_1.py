import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ta = Transition(label='Threat Assess')
ad = Transition(label='Alert Dispatch')
rc = Transition(label='Resource Check')
tm = Transition(label='Team Mobilize')
cs = Transition(label='Command Setup')
ig = Transition(label='Intel Gather')
re = Transition(label='Risk Evaluate')
ps = Transition(label='Priority Set')
fd = Transition(label='Field Deploy')
csync = Transition(label='Comm Sync')
pu = Transition(label='Public Update')
sm = Transition(label='Supply Manage')
smo = Transition(label='Safety Monitor')
il = Transition(label='Incident Log')
rp = Transition(label='Recovery Plan')
dt = Transition(label='Debrief Team')
da = Transition(label='Data Archive')

# Loop for continuous monitoring and safety checks
# A: Safety Monitor
# B: Comm Sync
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[smo, csync])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ta, ad, rc, tm, cs, ig, re, ps, fd, loop_monitor,
    pu, sm, il, rp, dt, da
])

# Add the control-flow edges
root.order.add_edge(ta, ad)
root.order.add_edge(ad, rc)
root.order.add_edge(rc, tm)
root.order.add_edge(tm, cs)
root.order.add_edge(cs, ig)
root.order.add_edge(ig, re)
root.order.add_edge(re, ps)
root.order.add_edge(ps, fd)
root.order.add_edge(fd, loop_monitor)
root.order.add_edge(loop_monitor, pu)
root.order.add_edge(loop_monitor, sm)
root.order.add_edge(loop_monitor, il)
root.order.add_edge(pu, rp)
root.order.add_edge(sm, rp)
root.order.add_edge(il, rp)
root.order.add_edge(rp, dt)
root.order.add_edge(dt, da)