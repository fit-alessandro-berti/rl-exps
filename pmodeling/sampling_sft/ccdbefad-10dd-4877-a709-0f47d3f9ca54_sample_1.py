import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Material Scout')
sv = Transition(label='Supplier Vetting')
sa = Transition(label='Skill Audit')
of = Transition(label='Order Forecast')
cs = Transition(label='Custom Scheduling')
ir = Transition(label='Impact Review')
pi = Transition(label='Product Inspect')
er = Transition(label='Eco Packaging')
mt = Transition(label='Multi Transport')
ro = Transition(label='Route Optimize')
fl = Transition(label='Feedback Loop')
cr = Transition(label='Craft Refine')
ib = Transition(label='Inventory Balance')
sm = Transition(label='Story Marketing')
hs = Transition(label='Heritage Share')
da = Transition(label='Demand Adjust')
csync = Transition(label='Community Sync')

# Build the loop body: Impact Review -> Craft Refine -> Inventory Balance
body = StrictPartialOrder(nodes=[ir, cr, ib])
body.order.add_edge(ir, cr)
body.order.add_edge(cr, ib)

# Loop: after Feedback Loop, execute the body then optionally Feedback Loop again
loop = OperatorPOWL(operator=Operator.LOOP, children=[fl, body])

# Assemble the full process
root = StrictPartialOrder(nodes=[
    ms, sv, sa, of, cs, ir, pi, er, mt, ro, loop,
    sm, hs, da, csync
])

# Define the control-flow dependencies
root.order.add_edge(ms, sv)
root.order.add_edge(sv, sa)
root.order.add_edge(sa, of)
root.order.add_edge(of, cs)
root.order.add_edge(cs, ir)
root.order.add_edge(ir, pi)
root.order.add_edge(pi, er)
root.order.add_edge(er, mt)
root.order.add_edge(mt, ro)
root.order.add_edge(ro, loop)
root.order.add_edge(loop, sm)
root.order.add_edge(loop, hs)
root.order.add_edge(loop, da)
root.order.add_edge(loop, csync)

print(root)