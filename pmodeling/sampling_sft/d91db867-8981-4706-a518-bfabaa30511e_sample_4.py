import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
cr = Transition(label='Context Review')
ec = Transition(label='Expert Consult')
ic = Transition(label='Image Capture')
ct = Transition(label='Condition Test')
fr = Transition(label='Forgery Risk')
rc = Transition(label='Registry Crosscheck')
lv = Transition(label='Legal Verify')
er = Transition(label='Ethics Review')
rd = Transition(label='Report Draft')
ci = Transition(label='Certificate Issue')
da = Transition(label='Digital Archive')
ts = Transition(label='Transfer Setup')
fa = Transition(label='Final Approval')

# Silent transition for optional loops
skip = SilentTransition()

# Loop: Image Capture -> Condition Test -> Forgery Risk
image_loop = OperatorPOWL(operator=Operator.LOOP, children=[ic, StrictPartialOrder(nodes=[ct, fr])])

# Loop: Legal Verify -> Ethics Review
legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[lv, er])

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, ms, cr, ec, image_loop,
    legal_loop, rc, da, ts, fa
])

# Define the control-flow dependencies
root.order.add_edge(pc, ms)
root.order.add_edge(ms, cr)
root.order.add_edge(cr, ec)
root.order.add_edge(ec, image_loop)

root.order.add_edge(image_loop, legal_loop)
root.order.add_edge(legal_loop, da)

root.order.add_edge(da, ts)
root.order.add_edge(ts, fa)