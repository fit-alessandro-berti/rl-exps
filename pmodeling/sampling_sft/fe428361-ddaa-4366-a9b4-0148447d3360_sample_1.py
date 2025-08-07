import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Silent transition for loop continuation
skip = SilentTransition()

# Loop for weather monitoring and flight control
loop_flight = OperatorPOWL(
    operator=Operator.LOOP,
    children=[wm, StrictPartialOrder(nodes=[ld, ft, dcf, da, fc, ir, wr, pr])]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    cc, pa, dc, rc, fs, ro, ps, pi, loop_flight
])

# Define the control-flow dependencies
root.order.add_edge(cc, pa)
root.order.add_edge(pa, dc)
root.order.add_edge(dc, rc)
root.order.add_edge(rc, fs)
root.order.add_edge(fs, ro)
root.order.add_edge(ro, ps)
root.order.add_edge(ps, pi)
root.order.add_edge(pi, loop_flight)