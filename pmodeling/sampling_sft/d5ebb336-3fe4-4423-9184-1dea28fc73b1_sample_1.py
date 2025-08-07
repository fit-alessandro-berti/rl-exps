import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
dc = Transition(label='Data Collection')
pa = Transition(label='Point Aggregation')
cc = Transition(label='Conflict Check')
fs = Transition(label='Fraud Scan')
ra = Transition(label='Reward Adjust')
rv = Transition(label='Redemption Verify')
ps = Transition(label='Partner Sync')
ba = Transition(label='Behavior Analyze')
au = Transition(label='Async Update')
rt = Transition(label='Rollback Trigger')
ccom = Transition(label='Compliance Check')
ns = Transition(label='Notification Send')
uf = Transition(label='User Feedback')
rg = Transition(label='Report Generate')
sa = Transition(label='System Audit')

# Build the loop body for the conflict-checking process
body = StrictPartialOrder(nodes=[cc, fs, ra, rv])
body.order.add_edge(cc, fs)
body.order.add_edge(fs, ra)
body.order.add_edge(ra, rv)

# Define the main loop: do Data Collection, then do the body and optionally do Async Update then back to Data Collection
loop_body = StrictPartialOrder(nodes=[dc, body, au])
loop_body.order.add_edge(dc, body)
loop_body.order.add_edge(body, au)
loop_body.order.add_edge(au, dc)

# Define the main process as a strict partial order
root = StrictPartialOrder(nodes=[
    dc, pa, cc, fs, ra, rv, ps, ba, au, rt, ccom, ns, uf, rg, sa
])

# Add the loop body to the root
root.order.add_edge(dc, loop_body)

# Add the loop for conflict-checking
root.order.add_edge(loop_body, body)

# Add the optional Async Update and rollback trigger
root.order.add_edge(body, au)
root.order.add_edge(au, rt)

# Add the compliance and feedback reporting
root.order.add_edge(rt, ccom)
root.order.add_edge(ccom, ns)
root.order.add_edge(ns, uf)
root.order.add_edge(uf, rg)
root.order.add_edge(rg, sa)