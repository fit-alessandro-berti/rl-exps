import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms      = Transition(label='Material Scout')
sv      = Transition(label='Supplier Vetting')
sa      = Transition(label='Skill Audit')
of      = Transition(label='Order Forecast')
cs      = Transition(label='Custom Scheduling')
ir      = Transition(label='Impact Review')
pi      = Transition(label='Product Inspect')
ep      = Transition(label='Eco Packaging')
mt      = Transition(label='Multi Transport')
ro      = Transition(label='Route Optimize')
fl      = Transition(label='Feedback Loop')
cr      = Transition(label='Craft Refine')
ib      = Transition(label='Inventory Balance')
sm      = Transition(label='Story Marketing')
hs      = Transition(label='Heritage Share')
da      = Transition(label='Demand Adjust')
csync   = Transition(label='Community Sync')

# Build the quality control sub‐process: Impact Review -> Product Inspect -> Eco Packaging
qc = StrictPartialOrder(nodes=[ir, pi, ep])
qc.order.add_edge(ir, pi)
qc.order.add_edge(pi, ep)

# Build the feedback‐loop sub‐process: Feedback Loop -> Craft Refine
fl_loop = OperatorPOWL(operator=Operator.LOOP, children=[fl, cr])

# Build the inventory management sub‐process: Demand Adjust -> Inventory Balance
im = StrictPartialOrder(nodes=[da, ib])
im.order.add_edge(da, ib)

# Build the marketing sub‐process: Story Marketing -> Heritage Share
marketing = StrictPartialOrder(nodes=[sm, hs])
marketing.order.add_edge(sm, hs)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    ms, sv, sa, of, cs, ir, pi, ep,
    mt, ro, fl_loop, qc,
    da, ib, im,
    sm, hs, marketing,
    csync
])

# Sequential sequence: Material Scout -> Supplier Vetting -> Skill Audit -> Order Forecast -> Custom Scheduling
root.order.add_edge(ms, sv)
root.order.add_edge(sv, sa)
root.order.add_edge(sa, of)
root.order.add_edge(of, cs)

# Followed by the quality control sub‐process
root.order.add_edge(cs, qc)

# Then the feedback‐loop sub‐process
root.order.add_edge(qc, fl_loop)

# After that, Demand Adjust -> Inventory Balance
root.order.add_edge(fl_loop, da)
root.order.add_edge(da, ib)

# Parallel: Marketing -> Community Sync
root.order.add_edge(sm, marketing)
root.order.add_edge(hs, marketing)
root.order.add_edge(marketing, csync)

# Finally, multi‐transport and route optimization
root.order.add_edge(csync, mt)
root.order.add_edge(mt, ro)