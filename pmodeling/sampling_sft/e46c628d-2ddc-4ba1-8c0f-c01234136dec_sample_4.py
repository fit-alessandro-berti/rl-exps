import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
sm2 = Transition(label='Safety Monitor')
il = Transition(label='Incident Log')
rp = Transition(label='Recovery Plan')
dt = Transition(label='Debrief Team')
da = Transition(label='Data Archive')

# Loop for continuous monitoring and response
loop = OperatorPOWL(operator=Operator.LOOP, children=[sm, sm2])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ta, ad, rc, tm, cs, ig, re, ps, fd, csync, pu, loop,
    il, rp, dt, da
])

# Define the control-flow dependencies
root.order.add_edge(ta, ad)
root.order.add_edge(ad, rc)
root.order.add_edge(rc, tm)
root.order.add_edge(tm, cs)
root.order.add_edge(cs, ig)
root.order.add_edge(ig, re)
root.order.add_edge(re, ps)
root.order.add_edge(ps, fd)
root.order.add_edge(fd, csync)
root.order.add_edge(csync, pu)
root.order.add_edge(pu, loop)
root.order.add_edge(loop, il)
root.order.add_edge(il, rp)
root.order.add_edge(rp, da)

print(root)