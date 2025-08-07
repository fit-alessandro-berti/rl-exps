import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
vp = Transition(label='Verify Provenance')
ac = Transition(label='Assess Condition')
nt = Transition(label='Negotiate Terms')
at = Transition(label='Arrange Transport')
cc = Transition(label='Customs Clearance')
si = Transition(label='Secure Insurance')
sh = Transition(label='Schedule Handlers')
ia = Transition(label='Install Artwork')
mc = Transition(label='Monitor Climate')
ms = Transition(label='Manage Security')
fa = Transition(label='Facilitate Access')
dd = Transition(label='Document Display')
ce = Transition(label='Coordinate Events')
ip = Transition(label='Inspect Periodically')
pr = Transition(label='Plan Return')
da = Transition(label='Deinstall Artwork')
fr = Transition(label='Finalize Reports')

# Loop for periodic inspections: do an inspection, then choose to exit or repeat
inspection_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ip, ip]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    vp, ac, nt, at, cc, si, sh, ia, mc, ms, fa, dd, ce, inspection_loop,
    pr, da, fr
])

# Define the control-flow dependencies
root.order.add_edge(vp, ac)
root.order.add_edge(vp, nt)
root.order.add_edge(ac, at)
root.order.add_edge(nt, at)
root.order.add_edge(at, cc)
root.order.add_edge(cc, si)
root.order.add_edge(si, sh)
root.order.add_edge(sh, ia)
root.order.add_edge(ia, mc)
root.order.add_edge(mc, ms)
root.order.add_edge(ms, fa)
root.order.add_edge(fa, dd)
root.order.add_edge(dd, ce)
root.order.add_edge(ce, inspection_loop)
root.order.add_edge(inspection_loop, pr)
root.order.add_edge(pr, da)
root.order.add_edge(da, fr)