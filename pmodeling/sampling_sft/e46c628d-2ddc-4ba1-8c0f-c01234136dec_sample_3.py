import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
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
smn = Transition(label='Safety Monitor')
il = Transition(label='Incident Log')
rp = Transition(label='Recovery Plan')
dt = Transition(label='Debrief Team')
da = Transition(label='Data Archive')
skip = SilentTransition()

# Build the loop body: Safety Monitor, Incident Log, Debrief Team, Data Archive
body = StrictPartialOrder(nodes=[smn, il, dt, da])
# No edges => all four happen concurrently

# Define the loop: do Safety Monitor, then either exit or do body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[smn, body])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    ta, ad, rc, tm, cs, ig, re, ps,
    fd, csync, pu, skip, sm,
    loop
])

# Sequence edges
root.order.add_edge(ta, ad)
root.order.add_edge(ad, rc)
root.order.add_edge(rc, cs)
root.order.add_edge(cs, ig)
root.order.add_edge(ig, re)
root.order.add_edge(re, ps)
root.order.add_edge(ps, fd)
root.order.add_edge(fd, csync)
root.order.add_edge(csync, pu)
root.order.add_edge(pu, skip)
root.order.add_edge(skip, sm)
root.order.add_edge(sm, loop)

# The loop's body is concurrent with itself
root.order.add_edge(loop, loop)

# Safety Monitor must precede Incident Log
root.order.add_edge(sm, il)

# Debrief Team must precede Data Archive
root.order.add_edge(dt, da)

# Incident Log must precede Debrief Team
root.order.add_edge(il, dt)

# Data Archive must precede Debrief Team
root.order.add_edge(da, dt)