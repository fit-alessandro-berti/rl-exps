import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
dr   = Transition(label='Document Review')
mt   = Transition(label='Material Testing')
rd   = Transition(label='Radiocarbon Date')
se   = Transition(label='Stylistic Eval')
dc   = Transition(label='Database Check')
oa   = Transition(label='Ownership Audit')
ev   = Transition(label='Export Verify')
ea   = Transition(label='Expert Arbitration')
cp   = Transition(label='Conservation Plan')
ra   = Transition(label='Risk Assessment')
ar   = Transition(label='Approval Review')
isup = Transition(label='Insurance Setup')
st   = Transition(label='Secure Transport')
am   = Transition(label='Acquisitions Meet')
fd   = Transition(label='Final Documentation')

# Build the loop body for expert arbitration: Risk Assessment -> Approval Review
loop_body = StrictPartialOrder(nodes=[ra, ar])
loop_body.order.add_edge(ra, ar)

# Build the loop: do Material Testing, then either exit or do Expert Arbitration and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[mt, loop_body])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    dr, mt, rd, se, dc, oa, ev, ea,
    loop, cp, ra, ar, isup, st, am, fd
])

# Define the control-flow dependencies
root.order.add_edge(dr,  mt)
root.order.add_edge(mt,  rd)
root.order.add_edge(mt,  se)
root.order.add_edge(se,  dc)
root.order.add_edge(dc,  oa)
root.order.add_edge(oa,  ev)
root.order.add_edge(ev,  ea)
root.order.add_edge(ea,  loop)
root.order.add_edge(loop, cp)
root.order.add_edge(cp,  isup)
root.order.add_edge(isup, st)
root.order.add_edge(st,  am)
root.order.add_edge(am,  fd)

# Final result
print(root)