import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
cb  = Transition(label='Client Brief')
sa  = Transition(label='Spec Analysis')
ms  = Transition(label='Material Sourcing')
cv  = Transition(label='Component Vetting')
fa  = Transition(label='Frame Assembly')
si  = Transition(label='Sensor Install')
ps  = Transition(label='Propulsion Setup')
cal = Transition(label='Calibration')
sl  = Transition(label='Software Load')
ft  = Transition(label='Flight Test')
at  = Transition(label='AI Training')
qr  = Transition(label='QA Review')
mp  = Transition(label='Mission Pack')
ct  = Transition(label='Client Training')
ds  = Transition(label='Deployment Support')

# Loop for continuous feedback and refinement
loop = OperatorPOWL(operator=Operator.LOOP, children=[sa, cv])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    cb, loop,
    ms, cv,
    fa, si, ps,
    cal, sl,
    ft, at,
    qr, mp,
    ct, ds
])

# Sequential control-flow edges
root.order.add_edge(cb, loop)
root.order.add_edge(loop, ms)
root.order.add_edge(ms, cv)
root.order.add_edge(cv, fa)
root.order.add_edge(fa, si)
root.order.add_edge(si, ps)
root.order.add_edge(ps, cal)
root.order.add_edge(cal, sl)
root.order.add_edge(sl, ft)
root.order.add_edge(ft, at)
root.order.add_edge(at, qr)
root.order.add_edge(qr, mp)
root.order.add_edge(mp, ct)
root.order.add_edge(ct, ds)