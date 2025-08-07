import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
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

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    ts, om, eg, isprint, pb, uf,
    rr, ia, pl, sm, rs, su, iaa,
    ks, mt
])

# Define the control‐flow dependencies
root.order.add_edge(ts, om)
root.order.add_edge(om, eg)
root.order.add_edge(eg, isprint)
root.order.add_edge(isprint, pb)
root.order.add_edge(pb, uf)
root.order.add_edge(uf, rr)
root.order.add_edge(rr, ia)
root.order.add_edge(ia, pl)
root.order.add_edge(pl, sm)
root.order.add_edge(sm, rs)
root.order.add_edge(rs, su)
root.order.add_edge(su, iaa)
root.order.add_edge(iaa, ks)
root.order.add_edge(ks, mt)

# The loop for monitoring trends
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[mt, mt]
)

# Add the monitoring loop to the partial‐order
root.order.add_edge(su, monitor_loop)
root.order.add_edge(monitor_loop, mt)

print(root)