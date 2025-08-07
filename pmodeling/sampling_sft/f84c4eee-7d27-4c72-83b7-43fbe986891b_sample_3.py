import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
cs = Transition(label='Component Sourcing')
fa = Transition(label='Frame Assembly')
sm = Transition(label='Sensor Mounting')
wh = Transition(label='Wiring Harness')
ct = Transition(label='Circuit Testing')
fl = Transition(label='Firmware Loading')
ic = Transition(label='Initial Calibration')
si = Transition(label='Software Integration')
ft = Transition(label='Flight Testing')
dl = Transition(label='Data Logging')
pt = Transition(label='Performance Tuning')
pp = Transition(label='Packaging Prep')
cl = Transition(label='Custom Labeling')
dp = Transition(label='Documentation Print')
qr = Transition(label='Quality Review')
ctr = Transition(label='Client Training')
rm = Transition(label='Remote Monitoring')
fu = Transition(label='Firmware Update')

# Build the partial order model
root = StrictPartialOrder(nodes=[
    cs, fa, sm, wh, ct, fl, ic, si, ft, dl, pt, pp, cl, dp, qr, ctr, rm, fu
])

# Define the sequence of activities
root.order.add_edge(cs, fa)
root.order.add_edge(fa, sm)
root.order.add_edge(fa, wh)
root.order.add_edge(sm, ct)
root.order.add_edge(wh, ct)
root.order.add_edge(ct, fl)
root.order.add_edge(fl, ic)
root.order.add_edge(ic, si)
root.order.add_edge(si, ft)
root.order.add_edge(ft, dl)
root.order.add_edge(dl, pt)
root.order.add_edge(pt, pp)
root.order.add_edge(pp, cl)
root.order.add_edge(cl, dp)
root.order.add_edge(dp, qr)
root.order.add_edge(qr, ctr)
root.order.add_edge(ctr, rm)
root.order.add_edge(rm, fu)

# Optional loop for remote monitoring and firmware update
# This can be modeled as a loop where the body is the monitoring and firmware update sequence
# Loop(children=[rm, fu]) would be equivalent to a single node representing the loop
# However, for clarity in the partial order model, we maintain the explicit sequence
# In a real-world system, you might want to use a loop to repeat the monitoring and update process indefinitely or until completion
# For example, to repeat until a condition is met, you could use a loop with a condition-based exit
# Here, we assume the loop is infinite for simplicity

print(root)