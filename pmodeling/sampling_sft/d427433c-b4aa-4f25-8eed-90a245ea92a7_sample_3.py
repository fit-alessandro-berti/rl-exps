import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
mc = Transition(label='Milk Collection')
qt = Transition(label='Quality Testing')
mb = Transition(label='Milk Blending')
sc = Transition(label='Starter Culture')
fc = Transition(label='Fermentation Check')
cc = Transition(label='Curd Cutting')
ws = Transition(label='Whey Separation')
mp = Transition(label='Molding Press')
ss = Transition(label='Salting Stage')
ac = Transition(label='Aging Control')
pd = Transition(label='Packaging Design')
cs = Transition(label='Cold Shipping')
ca = Transition(label='Compliance Audit')
bl = Transition(label='Blockchain Log')
mpm = Transition(label='Market Pricing')
of = Transition(label='Order Fulfillment')
fr = Transition(label='Feedback Review')

# Loop for aging and compliance
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ac, ca]
)

# Loop for packaging and pricing
pricing_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pd, mpm]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    mc, qt, mb, sc, fc, cc, ws, mp, ss, aging_loop,
    cs, bl, pricing_loop, of, fr
])

# Define the control-flow dependencies
root.order.add_edge(mc, qt)
root.order.add_edge(qt, mb)
root.order.add_edge(mb, sc)
root.order.add_edge(sc, fc)
root.order.add_edge(fc, cc)
root.order.add_edge(cc, ws)
root.order.add_edge(ws, mp)
root.order.add_edge(mp, ss)
root.order.add_edge(ss, aging_loop)

# After aging, parallelize compliance and packaging
root.order.add_edge(aging_loop, cs)
root.order.add_edge(aging_loop, bl)

# After compliance, parallelize pricing and packaging
root.order.add_edge(cs, pricing_loop)
root.order.add_edge(bl, pricing_loop)

# After pricing, fulfillment and feedback
root.order.add_edge(pricing_loop, of)
root.order.add_edge(of, fr)

print(root)