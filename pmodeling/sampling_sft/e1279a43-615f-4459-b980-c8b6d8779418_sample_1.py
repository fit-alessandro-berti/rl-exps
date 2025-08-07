import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
sa = Transition(label='Site Analysis')
isup = Transition(label='Infrastructure Setup')
ss = Transition(label='Seed Selection')
nm = Transition(label='Nutrient Mix')
pc = Transition(label='Planting Cycle')
ca = Transition(label='Climate Adjust')
gm = Transition(label='Growth Monitor')
pcn = Transition(label='Pest Control')
hm = Transition(label='Harvesting Mode')
qc = Transition(label='Quality Check')
pp = Transition(label='Packaging Phase')
cs = Transition(label='Cold Storage')
od = Transition(label='Order Dispatch')
wr = Transition(label='Waste Recycling')
sm = Transition(label='System Maintain')

# Loop for continuous monitoring and adjustment
loop_body = StrictPartialOrder(nodes=[gm, pcn])
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, ca])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    sa, isup, ss, nm, pc,
    loop, hm, qc, pp, cs,
    od, wr, sm
])

# Sequential setup and planting
root.order.add_edge(sa, isup)
root.order.add_edge(isup, ss)
root.order.add_edge(ss, nm)
root.order.add_edge(nm, pc)

# Continuous monitoring loop
root.order.add_edge(pc, loop)

# After harvesting, perform quality check, packaging, cold storage, dispatch, waste recycling, and system maintain
root.order.add_edge(hm, qc)
root.order.add_edge(qc, pp)
root.order.add_edge(pp, cs)
root.order.add_edge(cs, od)
root.order.add_edge(od, wr)
root.order.add_edge(wr, sm)