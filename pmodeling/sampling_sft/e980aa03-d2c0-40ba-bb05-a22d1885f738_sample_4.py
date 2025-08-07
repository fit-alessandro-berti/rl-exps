import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
cb = Transition(label='Client Brief')
sa = Transition(label='Spec Analysis')
ms = Transition(label='Material Sourcing')
cv = Transition(label='Component Vetting')
fa = Transition(label='Frame Assembly')
si = Transition(label='Sensor Install')
ps = Transition(label='Propulsion Setup')
cal = Transition(label='Calibration')
sl = Transition(label='Software Load')
ft = Transition(label='Flight Test')
at = Transition(label='AI Training')
qr = Transition(label='QA Review')
mp = Transition(label='Mission Pack')
ct = Transition(label='Client Training')
ds = Transition(label='Deployment Support')

# Define the main assembly & testing sequence as a partial order
nodes = [fa, si, ps, cal, sl, ft, at, qr]
order = [
    (fa, si), (fa, ps), (si, cal), (ps, cal), (cal, sl), (sl, ft),
    (ft, at), (at, qr)
]
main_seq = StrictPartialOrder(nodes=nodes, order=set(order))

# Define the feedback loop: Client Brief -> Spec Analysis -> ...
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[cb, sa, ms, cv, fa, si, ps, cal, sl, ft, at, qr])

# Final root partial order includes the feedback loop and the mission‐pack‐deploy sequence
root = StrictPartialOrder(nodes=[feedback_loop, mp, ct, ds])
root.order.add_edge(feedback_loop, mp)
root.order.add_edge(mp, ct)
root.order.add_edge(ct, ds)