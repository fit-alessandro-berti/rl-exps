import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ts = Transition(label='Trend Scan')
ih = Transition(label='Idea Harvest')
sm = Transition(label='Sector Match')
bh = Transition(label='Brainstorm Hub')
cf = Transition(label='Concept Filter')
pb = Transition(label='Prototype Build')
ht = Transition(label='Hybrid Testing')
ss = Transition(label='Stakeholder Sync')
ra = Transition(label='Risk Assess')
sm_map = Transition(label='Scenario Map')
sa = Transition(label='Strategy Align')
pl = Transition(label='Pilot Launch')
dc = Transition(label='Data Capture')
ms = Transition(label='Market Sense')
sp = Transition(label='Scale Plan')

# Loop for iterative refinement: repeat Data Capture -> Market Sense -> Scale Plan until exit
refine_loop = OperatorPOWL(operator=Operator.LOOP, children=[dc, ms, sp])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ts, ih, sm, bh, cf, pb, ht, ss, ra, sm_map, sa, pl, refine_loop
])

# Define the control-flow dependencies
root.order.add_edge(ts, ih)
root.order.add_edge(ih, sm)
root.order.add_edge(sm, bh)
root.order.add_edge(bh, cf)
root.order.add_edge(cf, pb)
root.order.add_edge(pb, ht)
root.order.add_edge(ht, ss)
root.order.add_edge(ss, ra)
root.order.add_edge(ra, sm_map)
root.order.add_edge(sm_map, sa)
root.order.add_edge(sa, pl)
root.order.add_edge(pl, refine_loop)

# Silent transition for the exit of the loop (not shown in the control-flow)
root.order.add_edge(refine_loop, refine_loop)  # self-loop to mark the end of the loop

# Final edge from the loop to the end (optional, for completeness)
root.order.add_edge(refine_loop, None)