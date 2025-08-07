import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms   = Transition(label='Material Scout')
sv   = Transition(label='Supplier Vetting')
sa   = Transition(label='Skill Audit')
of   = Transition(label='Order Forecast')
cs   = Transition(label='Custom Scheduling')
ir   = Transition(label='Impact Review')
pi   = Transition(label='Product Inspect')
ep   = Transition(label='Eco Packaging')
mt   = Transition(label='Multi Transport')
ro   = Transition(label='Route Optimize')
fl   = Transition(label='Feedback Loop')
cr   = Transition(label='Craft Refine')
ib   = Transition(label='Inventory Balance')
sm   = Transition(label='Story Marketing')
hs   = Transition(label='Heritage Share')
da   = Transition(label='Demand Adjust')
csync= Transition(label='Community Sync')

# Loop for continuous feedback and refinement
loop = OperatorPOWL(operator=Operator.LOOP, children=[fl, cr])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, sv, sa, of, cs, ir,
    pi, ep, mt, ro,
    loop,
    ib, sm, hs, da, csync
])

# Define control-flow dependencies
root.order.add_edge(ms, sv)
root.order.add_edge(sv, sa)
root.order.add_edge(sa, of)
root.order.add_edge(of, cs)
root.order.add_edge(cs, ir)
root.order.add_edge(ir, pi)
root.order.add_edge(pi, ep)
root.order.add_edge(ep, mt)
root.order.add_edge(mt, ro)
root.order.add_edge(ro, loop)
root.order.add_edge(loop, ib)
root.order.add_edge(ib, sm)
root.order.add_edge(sm, hs)
root.order.add_edge(hs, da)
root.order.add_edge(da, csync)

print(root)