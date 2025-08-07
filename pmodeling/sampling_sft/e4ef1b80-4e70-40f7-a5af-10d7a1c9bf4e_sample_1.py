import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
os = Transition(label='Opportunity Scan')
iw = Transition(label='Idea Workshop')
cm = Transition(label='Concept Merge')
ra = Transition(label='Resource Align')
pb = Transition(label='Prototype Build')
ft = Transition(label='Feasibility Test')
pl = Transition(label='Pilot Launch')
fg = Transition(label='Feedback Gather')
da = Transition(label='Design Adapt')
cc = Transition(label='Compliance Check')
sp = Transition(label='Scaling Plan')
ipm = Transition(label='IP Management')
ms = Transition(label='Market Sync')
pr = Transition(label='Partner Review')
es = Transition(label='Exit Strategy')

# Build the adaptation loop: Design Adapt -> Compliance Check -> Scaling Plan
adapt_loop = StrictPartialOrder(nodes=[da, cc, sp])
adapt_loop.order.add_edge(da, cc)
adapt_loop.order.add_edge(cc, sp)

# Build the feedback-driven adaptation cycle:
# Feedback Gather -> Adaptation Loop -> IP Management -> Market Sync
feedback_cycle = StrictPartialOrder(nodes=[fg, adapt_loop, ipm, ms])
feedback_cycle.order.add_edge(fg, adapt_loop)
feedback_cycle.order.add_edge(adapt_loop, ipm)
feedback_cycle.order.add_edge(ipm, ms)

# Build the overall process as a partial order
root = StrictPartialOrder(nodes=[
    os, iw, cm, ra, pb, ft, pl,
    feedback_cycle,
    pr, es
])

# Define the control-flow dependencies
root.order.add_edge(os, iw)
root.order.add_edge(iw, cm)
root.order.add_edge(cm, ra)
root.order.add_edge(ra, pb)
root.order.add_edge(pb, ft)
root.order.add_edge(ft, pl)
root.order.add_edge(pl, feedback_cycle)
root.order.add_edge(feedback_cycle, pr)
root.order.add_edge(pr, es)