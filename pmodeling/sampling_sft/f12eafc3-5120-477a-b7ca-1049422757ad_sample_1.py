import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms = Transition(label='Milk Selection')
qt = Transition(label='Quality Testing')
mp = Transition(label='Milk Pasteurize')
cc = Transition(label='Cheese Crafting')
ca = Transition(label='Controlled Aging')
sr = Transition(label='Sensory Review')
cp = Transition(label='Custom Packaging')
lp = Transition(label='Label Printing')
el = Transition(label='Export Licensing')
dp = Transition(label='Documentation Prep')
ccs = Transition(label='Customs Clearance')
cs = Transition(label='Cold Shipping')
dt = Transition(label='Delivery Tracking')
fr = Transition(label='Feedback Review')
ma = Transition(label='Market Analysis')

# Define the loop for aging and sensory review
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ca, sr]
)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    ms, qt, mp,
    cc, aging_loop,
    cp, lp, dp,
    ccs, cs, dt,
    fr, ma
])

# Define the control-flow edges
root.order.add_edge(ms, qt)
root.order.add_edge(qt, mp)
root.order.add_edge(mp, cc)
root.order.add_edge(cc, aging_loop)
root.order.add_edge(aging_loop, cp)
root.order.add_edge(cp, lp)
root.order.add_edge(lp, dp)
root.order.add_edge(dp, ccs)
root.order.add_edge(ccs, cs)
root.order.add_edge(cs, dt)
root.order.add_edge(dt, fr)
root.order.add_edge(fr, ma)