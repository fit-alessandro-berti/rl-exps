import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
df = Transition(label='Demand Forecast')
cm = Transition(label='Courier Match')
cc = Transition(label='Credential Check')
rd = Transition(label='Route Design')
la = Transition(label='Load Assign')
ts = Transition(label='Traffic Scan')
ps = Transition(label='Package Secure')
da = Transition(label='Dispatch Alert')
rt = Transition(label='Real-time Track')
ii = Transition(label='Incentive Issue')
dr = Transition(label='Dispute Review')
cn = Transition(label='Customer Notify')
fc = Transition(label='Feedback Collect')
pl = Transition(label='Performance Log')
lu = Transition(label='Ledger Update')
hs = Transition(label='Hub Sync')

# Define the loop for continuous data collection and ledger update
loop_data = StrictPartialOrder(nodes=[pl, lu])
loop_data.order.add_edge(pl, lu)

# Define the loop for dispute review and customer notification
loop_dispute = StrictPartialOrder(nodes=[dr, cn])
loop_dispute.order.add_edge(dr, cn)

# Build the root partial order
root = StrictPartialOrder(nodes=[
    df, cm, cc, rd, la, ts, ps, da, rt,
    ii, loop_data, loop_dispute,
    hs
])

# Add the control-flow edges
root.order.add_edge(df, cm)
root.order.add_edge(cm, cc)
root.order.add_edge(cc, rd)
root.order.add_edge(rd, la)
root.order.add_edge(la, ts)
root.order.add_edge(ts, ps)
root.order.add_edge(ps, da)
root.order.add_edge(da, rt)

# Add the loop for continuous data collection
root.order.add_edge(rt, loop_data)
root.order.add_edge(loop_data, rt)

# Add the loop for dispute review and customer notification
root.order.add_edge(da, loop_dispute)
root.order.add_edge(loop_dispute, da)

# Add the final hub synchronization
root.order.add_edge(da, hs)

# Print the root model for verification
print(root)