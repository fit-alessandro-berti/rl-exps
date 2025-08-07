import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
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
cc2 = Transition(label='Compliance Check')
ns = Transition(label='Notification Send')
uf = Transition(label='User Feedback')
rg = Transition(label='Report Generate')
sa = Transition(label='System Audit')

# Define the rollback loop: if a rollback is needed (Async Update), redo Async Update then rollback
rollback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[au, rt]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    dc, pa, cc, fs, ra, rv, ps, ba, au, rollback_loop, cc2, ns, uf, rg, sa
])

# Sequential flow from Data Collection to Async Update
root.order.add_edge(dc, pa)
root.order.add_edge(pa, cc)
root.order.add_edge(cc, fs)
root.order.add_edge(fs, ra)
root.order.add_edge(ra, rv)
root.order.add_edge(rv, ps)
root.order.add_edge(ps, ba)
root.order.add_edge(ba, au)

# After Async Update, either Compliance Check or go directly to Notification Send
root.order.add_edge(au, cc2)
root.order.add_edge(au, ns)

# After Compliance Check, feedback and reporting
root.order.add_edge(cc2, uf)
root.order.add_edge(cc2, rg)

# System audit is always at the end
root.order.add_edge(uf, sa)
root.order.add_edge(rg, sa)

# For rollback, go through the loop first
root.order.add_edge(rollback_loop, cc2)
root.order.add_edge(rollback_loop, uf)
root.order.add_edge(rollback_loop, rg)
root.order.add_edge(rollback_loop, sa)