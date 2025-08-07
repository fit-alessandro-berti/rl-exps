import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
inq    = Transition(label='Inquiry Review')
onb    = Transition(label='Client Onboard')
con    = Transition(label='Concept Draft')
fb     = Transition(label='Feedback Cycle')
cs     = Transition(label='Contract Setup')
ps     = Transition(label='Payment Schedule')
ms     = Transition(label='Material Sourcing')
ac     = Transition(label='Artwork Create')
qc     = Transition(label='Quality Check')
fs     = Transition(label='Frame Selection')
pp     = Transition(label='Packaging Prep')
sa     = Transition(label='Shipment Arrange')
dc     = Transition(label='Delivery Confirm')
post   = Transition(label='Post-Sale Support')
rm     = Transition(label='Revision Manage')
dm     = Transition(label='Delay Mitigate')

# Loop for iterative feedback cycle: do Feedback Cycle, then optionally Revision Manage and Feedback Cycle again
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[fb, rm, fb])

# Build the partial order
root = StrictPartialOrder(nodes=[
    inq, onb, con, feedback_loop,
    cs, ms, ac, qc,
    fs, pp, sa, dm, dc,
    post
])

# Define the control-flow dependencies
root.order.add_edge(inq, onb)
root.order.add_edge(onb, con)
root.order.add_edge(con, feedback_loop)

# After feedback, either do revisions or proceed directly to material sourcing
root.order.add_edge(feedback_loop, cs)
root.order.add_edge(feedback_loop, ms)

# Material sourcing and artwork creation can run in parallel
root.order.add_edge(cs, ac)
root.order.add_edge(ms, ac)

# Both finish to Quality Check
root.order.add_edge(ac, qc)

# Quality check then optionally revision manage, then do frame selection
root.order.add_edge(qc, fs)
root.order.add_edge(qc, feedback_loop)

# After frame selection, do packaging preparation
root.order.add_edge(fs, pp)

# Packaging prep then either shipment arrange or delay mitigation
root.order.add_edge(pp, sa)
root.order.add_edge(pp, dm)

# After shipment, either confirm delivery or post-sale support
root.order.add_edge(sa, dc)
root.order.add_edge(sa, post)

# Finally, after delivery, do post-sale support
root.order.add_edge(dc, post)