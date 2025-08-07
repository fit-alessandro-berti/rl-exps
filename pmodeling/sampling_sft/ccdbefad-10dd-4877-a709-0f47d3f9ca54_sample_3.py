import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms = Transition(label='Material Scout')
sv = Transition(label='Supplier Vetting')
sa = Transition(label='Skill Audit')
cf = Transition(label='Custom Scheduling')
oi = Transition(label='Order Forecast')
ip = Transition(label='Product Inspect')
ir = Transition(label='Impact Review')
ep = Transition(label='Eco Packaging')
mt = Transition(label='Multi Transport')
ro = Transition(label='Route Optimize')
fl = Transition(label='Feedback Loop')
cr = Transition(label='Craft Refine')
ib = Transition(label='Inventory Balance')
sm = Transition(label='Story Marketing')
hs = Transition(label='Heritage Share')
da = Transition(label='Demand Adjust')
cs = Transition(label='Community Sync')

# Define the main production & logistics pipeline as a partial order
prod_po = StrictPartialOrder(nodes=[cf, oi, ip, ir, ep, mt, ro])
prod_po.order.add_edge(cf, oi)
prod_po.order.add_edge(oi, ip)
prod_po.order.add_edge(ip, ir)
prod_po.order.add_edge(ir, ep)
prod_po.order.add_edge(ep, mt)
prod_po.order.add_edge(mt, ro)

# Define the feedback loop as a LOOP node: do Feedback Loop, then either exit or do Craft Refine and repeat
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[fl, cr])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    ms, sv, sa,
    prod_po,
    feedback_loop,
    ib, da, cs,
    sm, hs
])

# Add ordering constraints
root.order.add_edge(ms, sv)
root.order.add_edge(sv, sa)
root.order.add_edge(sa, prod_po)
root.order.add_edge(prod_po, feedback_loop)
root.order.add_edge(feedback_loop, ib)
root.order.add_edge(ib, da)
root.order.add_edge(da, cs)
root.order.add_edge(cs, sm)
root.order.add_edge(sm, hs)