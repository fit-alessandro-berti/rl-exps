import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the iterative testing loop: Flight Simulate -> Quality Review
loop_body = StrictPartialOrder(nodes=[fs, qr])
loop_body.order.add_edge(fs, qr)

# Define the training‐support loop: User Train -> Remote Setup -> Feedback Collect -> Support Schedule
training_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ut, OperatorPOWL(operator=Operator.LOOP, children=[rs, fc])]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    cc, sa, ms, co, pi, fa, si, ma, wc, su, ct, loop_body, training_loop
])

# Add the control-flow edges
root.order.add_edge(cc, sa)
root.order.add_edge(sa, ms)
root.order.add_edge(ms, co)
root.order.add_edge(co, pi)
root.order.add_edge(pi, fa)
root.order.add_edge(fa, si)
root.order.add_edge(fa, ma)
root.order.add_edge(fa, wc)
root.order.add_edge(fa, su)
root.order.add_edge(si, ct)
root.order.add_edge(ma, ct)
root.order.add_edge(wc, ct)
root.order.add_edge(su, ct)
root.order.add_edge(ct, loop_body)
root.order.add_edge(loop_body, training_loop)
root.order.add_edge(training_loop, ut)