import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sa = Transition(label='Site Analysis')
ps = Transition(label='Permit Securing')
ud = Transition(label='Unit Designing')
led = Transition(label='LED Sourcing')
hs = Transition(label='Hydroponic Setup')
sh = Transition(label='Staff Hiring')
pc = Transition(label='Pilot Cultivation')
di = Transition(label='Data Integration')
wr = Transition(label='Waste Recycling')
ld = Transition(label='Local Distribution')
ss = Transition(label='Subscription Setup')
iot = Transition(label='IoT Deployment')
sauc = Transition(label='Sustainability Audit')
mt = Transition(label='Market Testing')
pr = Transition(label='Process Refinement')

# Loop for continuous improvement: do Site Analysis, then either exit or do Process Refinement and repeat
improvement_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sa, pr]
)

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    sa, ps, ud, led, hs, pc, di, wr, ld, ss, iot, sauc, mt, improvement_loop
])

# Define the control‐flow dependencies
root.order.add_edge(sa, ps)
root.order.add_edge(ps, ud)
root.order.add_edge(ud, led)
root.order.add_edge(led, hs)
root.order.add_edge(hs, pc)
root.order.add_edge(pc, di)
root.order.add_edge(di, wr)
root.order.add_edge(wr, ld)
root.order.add_edge(ld, ss)
root.order.add_edge(ss, iot)
root.order.add_edge(iot, sauc)
root.order.add_edge(sauc, mt)
root.order.add_edge(mt, improvement_loop)

# Final loop node connects the improvement loop to itself (indirectly repeating the process)
root.order.add_edge(improvement_loop, improvement_loop)

print(root)