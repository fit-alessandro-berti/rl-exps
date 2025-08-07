import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
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

# Build the loop for continuous monitoring and quality testing
loop_body = StrictPartialOrder(nodes=[am, qt])
loop_body.order.add_edge(am, qt)
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, loop_body])

# Build the main partial order
main = StrictPartialOrder(nodes=[
    ms, cb, mp, cc, wd, mi, pc, sb, monitor_loop,
    pp, ld, oa, ta, rs, cr, fa
])

# Define the control-flow dependencies
main.order.add_edge(ms, cb)
main.order.add_edge(ms, mp)
main.order.add_edge(mp, cc)
main.order.add_edge(cc, wd)
main.order.add_edge(wd, mi)
main.order.add_edge(mi, pc)
main.order.add_edge(pc, sb)
main.order.add_edge(sb, monitor_loop)
main.order.add_edge(monitor_loop, monitor_loop)
main.order.add_edge(monitor_loop, pp)
main.order.add_edge(pp, ld)
main.order.add_edge(ld, oa)
main.order.add_edge(oa, ta)
main.order.add_edge(ta, rs)
main.order.add_edge(rs, cr)
main.order.add_edge(cr, fa)

# Final root partial order
root = main