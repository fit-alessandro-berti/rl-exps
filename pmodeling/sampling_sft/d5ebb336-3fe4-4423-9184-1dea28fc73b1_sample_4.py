import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
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
ccp = Transition(label='Compliance Check')
ns = Transition(label='Notification Send')
uf = Transition(label='User Feedback')
rg = Transition(label='Report Generate')
sa = Transition(label='System Audit')

# Loop for asynchronous updates: do Async Update, then optionally do Rollback Trigger, then repeat
async_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[au, rt]
)

# Main process partial order
root = StrictPartialOrder(nodes=[
    dc, pa, cc, fs, ra, rv,
    ba, ps,
    ccp, ns, uf, rg, sa
])

# Sequential dependencies
root.order.add_edge(dc, pa)
root.order.add_edge(pa, cc)
root.order.add_edge(cc, fs)
root.order.add_edge(fs, ra)
root.order.add_edge(ra, rv)
root.order.add_edge(rv, ba)
root.order.add_edge(ba, ps)

# After reward adjustment and redemption verification, do the compliance check
root.order.add_edge(ra, ccp)
root.order.add_edge(rv, ccp)

# After compliance check, do all post-process activities in parallel
post_seq = StrictPartialOrder(nodes=[
    ccp, ns, uf, rg, sa
])
root.order.add_edge(ccp, post_seq)

# Parallel post-process activities
for post in [ns, uf, rg, sa]:
    root.order.add_edge(post_seq, post)

# After all post-process activities, do the asynchronous update loop
root.order.add_edge(post_seq, async_loop)