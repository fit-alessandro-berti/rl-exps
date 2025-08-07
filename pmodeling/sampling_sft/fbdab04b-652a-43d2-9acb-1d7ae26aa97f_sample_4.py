import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
cc = Transition(label='Client Consult')
sa = Transition(label='Spec Analysis')
ms = Transition(label='Module Select')
co = Transition(label='Component Order')
pi = Transition(label='Parts Inspect')
fa = Transition(label='Frame Assemble')
si = Transition(label='Sensor Install')
ma = Transition(label='Motor Attach')
wc = Transition(label='Wiring Connect')
su = Transition(label='Software Upload')
ct = Transition(label='Calibration Test')
fs = Transition(label='Flight Simulate')
qr = Transition(label='Quality Review')
ut = Transition(label='User Train')
rs = Transition(label='Remote Setup')
fc = Transition(label='Feedback Collect')
ss = Transition(label='Support Schedule')

# Loop for iterative testing: Flight Simulate -> Quality Review -> Flight Simulate
loop_body = StrictPartialOrder(nodes=[fs, qr])
loop_body.order.add_edge(fs, qr)
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, fs])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    cc, sa, ms, co, pi, fa, si, ma, wc, su, ct, loop,
    ut, rs, fc, ss
])

# Define the control-flow dependencies
root.order.add_edge(cc, sa)
root.order.add_edge(sa, ms)
root.order.add_edge(ms, co)
root.order.add_edge(co, pi)
root.order.add_edge(pi, fa)
root.order.add_edge(fa, si)
root.order.add_edge(fa, ma)
root.order.add_edge(fa, wc)
root.order.add_edge(wc, su)
root.order.add_edge(su, ct)
root.order.add_edge(ct, loop)
root.order.add_edge(loop, ut)
root.order.add_edge(ut, rs)
root.order.add_edge(rs, fc)
root.order.add_edge(fc, ss)