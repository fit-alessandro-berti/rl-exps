import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Loop for adaptive AI training: do AI Training, then optionally repeat
loop_ai = OperatorPOWL(operator=Operator.LOOP, children=[at, at])

# Build the partial order
root = StrictPartialOrder(nodes=[
    cb, sa, ms, cv, fa, si, ps, cal, sl, ft, loop_ai, qr, mp, ct, ds
])

# Sequence: Client Brief -> Spec Analysis -> Material Sourcing -> Component Vetting
root.order.add_edge(cb, sa)
root.order.add_edge(sa, ms)
root.order.add_edge(ms, cv)

# Parallel: Frame Assembly and its supporting activities
root.order.add_edge(cv, fa)
root.order.add_edge(cv, si)
root.order.add_edge(cv, ps)
root.order.add_edge(cv, cal)
root.order.add_edge(cv, sl)

# After assembly, perform flight test and then the adaptive AI loop
root.order.add_edge(fa, ft)
root.order.add_edge(ft, loop_ai)

# Finally, perform QA review, mission packaging, client training, and deployment support
root.order.add_edge(loop_ai, qr)
root.order.add_edge(qr, mp)
root.order.add_edge(mp, ct)
root.order.add_edge(ct, ds)