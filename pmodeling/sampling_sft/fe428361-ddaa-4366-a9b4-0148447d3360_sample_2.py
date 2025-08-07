import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
cc = Transition(label='Client Consult')
pa = Transition(label='Payload Assess')
dc = Transition(label='Drone Configure')
rc = Transition(label='Regulation Check')
fs = Transition(label='Flight Simulate')
ro = Transition(label='Route Optimize')
ps = Transition(label='Package Secure')
pi = Transition(label='Pre-Flight Inspect')
wm = Transition(label='Weather Monitor')
ld = Transition(label='Launch Drone')
ft = Transition(label='Flight Track')
dcf = Transition(label='Delivery Confirm')
da = Transition(label='Data Analyze')
fc = Transition(label='Feedback Collect')
wr = Transition(label='Warranty Register')
ir = Transition(label='Issue Resolve')
pr = Transition(label='Package Return')
skip = SilentTransition()

# Define the loop for monitoring and resolving issues
issue_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[wm, ir]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    cc, pa, dc, rc, fs, ro, ps, pi, issue_loop,
    ld, ft, dcf, da, fc, wr, pr
])

# Define the control-flow dependencies
root.order.add_edge(cc, pa)
root.order.add_edge(pa, dc)
root.order.add_edge(dc, rc)
root.order.add_edge(rc, fs)
root.order.add_edge(fs, ro)
root.order.add_edge(ro, ps)
root.order.add_edge(ps, pi)
root.order.add_edge(pi, ld)
root.order.add_edge(ld, ft)
root.order.add_edge(ft, dcf)
root.order.add_edge(dcf, da)
root.order.add_edge(da, fc)
root.order.add_edge(fc, wr)
root.order.add_edge(wr, pr)

# The issue loop branches after flight track
root.order.add_edge(ft, issue_loop)
# After resolving issues, go back to flight monitoring
root.order.add_edge(issue_loop, wm)
# After flight monitoring, either exit or continue with data analysis
root.order.add_edge(wm, da)
root.order.add_edge(wm, skip)
# Skip edge goes directly to data analysis
root.order.add_edge(skip, da)
# After data analysis, return to flight tracking
root.order.add_edge(da, ft)
# Finally, after all flights, return the package
root.order.add_edge(ft, pr)