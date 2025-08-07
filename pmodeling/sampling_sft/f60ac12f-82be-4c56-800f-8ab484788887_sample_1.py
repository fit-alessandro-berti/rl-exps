import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms  = Transition(label='Milk Sourcing')
cp  = Transition(label='Culture Blending')
mp  = Transition(label='Milk Pasteurize')
cc  = Transition(label='Curd Cutting')
wd  = Transition(label='Whey Drain')
mi  = Transition(label='Mold Inoculate')
pc  = Transition(label='Press Cheese')
sb  = Transition(label='Salt Brine')
am  = Transition(label='Age Monitor')
qt  = Transition(label='Quality Test')
pp  = Transition(label='Packaging Prep')
ld  = Transition(label='Label Design')
oa  = Transition(label='Order Allocation')
ta  = Transition(label='Transport Arrange')
rs  = Transition(label='Retail Sync')
cr  = Transition(label='Customer Review')
fa  = Transition(label='Feedback Analyze')

# Define the feedback loop: Customer Review then optionally Feedback Analyze
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[cr, fa]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    ms, cp, mp, cc, wd, mi, pc, sb, am, qt, pp, ld, oa, ta, feedback_loop
])

# Add sequential dependencies
root.order.add_edge(ms, cp)
root.order.add_edge(cp, mp)
root.order.add_edge(mp, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, mi)
root.order.add_edge(mi, pc)
root.order.add_edge(pc, sb)
root.order.add_edge(sb, am)
root.order.add_edge(am, qt)
root.order.add_edge(qt, pp)
root.order.add_edge(pp, ld)
root.order.add_edge(ld, oa)
root.order.add_edge(oa, ta)
root.order.add_edge(ta, feedback_loop)

# Final loop: after packaging, enter the feedback loop
root.order.add_edge(pp, feedback_loop)