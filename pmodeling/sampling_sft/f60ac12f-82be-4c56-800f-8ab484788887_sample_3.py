import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Milk Sourcing')
cb = Transition(label='Culture Blending')
mp = Transition(label='Milk Pasteurize')
cc = Transition(label='Curd Cutting')
wd = Transition(label='Whey Drain')
mi = Transition(label='Mold Inoculate')
pc = Transition(label='Press Cheese')
sb = Transition(label='Salt Brine')
am = Transition(label='Age Monitor')
qt = Transition(label='Quality Test')
pp = Transition(label='Packaging Prep')
ld = Transition(label='Label Design')
oa = Transition(label='Order Allocation')
ta = Transition(label='Transport Arrange')
rs = Transition(label='Retail Sync')
cr = Transition(label='Customer Review')
fa = Transition(label='Feedback Analyze')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for continuous aging and monitoring
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[am, qt])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ms, cb, mp, cc, wd, mi, pc, sb, loop_aging,
    pp, ld, oa, ta, rs, cr, fa
])

# Define the control-flow dependencies
root.order.add_edge(ms, cb)
root.order.add_edge(ms, mp)
root.order.add_edge(mp, cc)
root.order.add_edge(cc, wd)
root.order.add_edge(wd, mi)
root.order.add_edge(mi, pc)
root.order.add_edge(pc, sb)
root.order.add_edge(sb, loop_aging)
root.order.add_edge(loop_aging, pp)
root.order.add_edge(loop_aging, qt)
root.order.add_edge(pp, ld)
root.order.add_edge(ld, oa)
root.order.add_edge(oa, ta)
root.order.add_edge(ta, rs)
root.order.add_edge(rs, cr)
root.order.add_edge(cr, fa)