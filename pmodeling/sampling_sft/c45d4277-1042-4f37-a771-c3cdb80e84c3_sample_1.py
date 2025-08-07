import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ts = Transition(label='Trend Scan')
om = Transition(label='Opportunity Map')
eg = Transition(label='Expert Gather')
isprint = Transition(label='Idea Sprint')
pb = Transition(label='Proto Build')
uf = Transition(label='User Feedback')
rr = Transition(label='Risk Review')
ia = Transition(label='IP Audit')
pl = Transition(label='Pilot Launch')
sm = Transition(label='Stakeholder Meet')
rs = Transition(label='Resource Shift')
su = Transition(label='Scale Up')
iaa = Transition(label='Impact Assess')
ks = Transition(label='Knowledge Share')
mt = Transition(label='Monitor Trends')

# Build the loop body: User Feedback -> Risk Review -> IP Audit -> Pilot Launch
loop_body = StrictPartialOrder(nodes=[uf, rr, ia, pl])
loop_body.order.add_edge(uf, rr)
loop_body.order.add_edge(rr, ia)
loop_body.order.add_edge(ia, pl)

# Define the loop: do Idea Sprint, then either exit or repeat the body
loop = OperatorPOWL(operator=Operator.LOOP, children=[isprint, loop_body])

# Assemble the overall process as a partial order
root = StrictPartialOrder(nodes=[
    ts, om, eg, isprint, loop, pb, rr, ia, pl, sm, rs, su, iaa, ks, mt
])

# Define the control-flow dependencies
root.order.add_edge(ts, om)
root.order.add_edge(om, eg)
root.order.add_edge(eg, isprint)
root.order.add_edge(isprint, loop)
root.order.add_edge(loop, pb)
root.order.add_edge(pb, rr)
root.order.add_edge(pb, ia)
root.order.add_edge(pb, pl)
root.order.add_edge(rr, sm)
root.order.add_edge(ia, sm)
root.order.add_edge(pl, sm)
root.order.add_edge(sm, rs)
root.order.add_edge(rs, su)
root.order.add_edge(su, iaa)
root.order.add_edge(iaa, ks)
root.order.add_edge(ks, mt)