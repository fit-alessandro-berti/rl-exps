import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
inq    = Transition(label='Inquiry Review')
onboard= Transition(label='Client Onboard')
cd     = Transition(label='Concept Draft')
fc     = Transition(label='Feedback Cycle')
cs     = Transition(label='Contract Setup')
ps     = Transition(label='Payment Schedule')
ms     = Transition(label='Material Sourcing')
ac     = Transition(label='Artwork Create')
qc     = Transition(label='Quality Check')
fs     = Transition(label='Frame Selection')
pp     = Transition(label='Packaging Prep')
sa     = Transition(label='Shipment Arrange')
dc     = Transition(label='Delivery Confirm')
pss    = Transition(label='Post-Sale Support')
rm     = Transition(label='Revision Manage')
dm     = Transition(label='Delay Mitigate')

# Loop for iterative feedback: do Feedback Cycle, then choose to exit or Revision Manage and then Feedback Cycle again
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[fc, rm])

# Build the partial order
root = StrictPartialOrder(nodes=[
    inq, onboard, cd, feedback_loop,
    cs, ps, ms,
    ac, qc, fs, pp, sa, dc,
    pss
])

# Define the control-flow dependencies
root.order.add_edge(inq, onboard)
root.order.add_edge(onboard, cd)
root.order.add_edge(cd, feedback_loop)

# After feedback, either exit or do revision and then feedback again
root.order.add_edge(feedback_loop, cs)
root.order.add_edge(feedback_loop, rm)

# After Contract Setup, proceed with Material Sourcing and Payment Schedule in parallel
root.order.add_edge(cs, ms)
root.order.add_edge(cs, ps)

# After Material Sourcing and Payment Schedule, proceed with Artwork Create and Quality Check in parallel
root.order.add_edge(ms, ac)
root.order.add_edge(ps, qc)

# After Artwork Create and Quality Check, proceed with Frame Selection, Packaging Prep, and Shipment Arrange in parallel
root.order.add_edge(ac, fs)
root.order.add_edge(qc, pp)
root.order.add_edge(fs, sa)
root.order.add_edge(pp, sa)

# After Shipment Arrange, proceed with Delivery Confirm and Post-Sale Support in parallel
root.order.add_edge(sa, dc)
root.order.add_edge(dc, pss)