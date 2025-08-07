import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
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

# Define the feedback loop: do Feedback Review, then either exit or do Fr -> Feedback Review again
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[fr, fr])

# Build the partial order
root = StrictPartialOrder(nodes=[
    mc, qt, mb, sc, fc, cc, ws, mp, ss, ac, pd, cs, ca, bl, mpm, feedback_loop
])

# Sequence of milk processing
root.order.add_edge(mc, qt)
root.order.add_edge(qt, mb)
root.order.add_edge(mb, sc)
root.order.add_edge(sc, fc)
root.order.add_edge(fc, cc)
root.order.add_edge(cc, ws)
root.order.add_edge(ws, mp)
root.order.add_edge(mp, ss)
root.order.add_edge(ss, ac)

# Parallel aging and packaging
root.order.add_edge(ac, pd)
root.order.add_edge(ac, cs)

# Final steps: compliance audit, blockchain log, market pricing, order fulfillment
root.order.add_edge(pd, ca)
root.order.add_edge(pd, bl)
root.order.add_edge(pd, mpm)
root.order.add_edge(ca, cs)
root.order.add_edge(bl, cs)
root.order.add_edge(mpm, cs)
root.order.add_edge(cs, of)

# Integrate the feedback loop after order fulfillment
root.order.add_edge(of, feedback_loop)