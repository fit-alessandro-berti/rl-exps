import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
cs = Transition(label='Colony Sourcing')
hd = Transition(label='Hive Design')
ss = Transition(label='Site Survey')
ip = Transition(label='Installation Prep')
hs = Transition(label='Hive Setup')
si = Transition(label='Sensor Install')
hm = Transition(label='Health Monitor')
pc = Transition(label='Pest Control')
hh = Transition(label='Honey Harvest')
wp = Transition(label='Wax Processing')
pp = Transition(label='Product Packaging')
od = Transition(label='Order Dispatch')
ws = Transition(label='Workshop Setup')
co = Transition(label='Community Outreach')
rc = Transition(label='Regulation Check')
da = Transition(label='Data Analysis')
mp = Transition(label='Maintenance Plan')

# Silent transition for loop body
skip = SilentTransition()

# Loop: monitor then optionally pest control and repeat
loop_body = StrictPartialOrder(nodes=[hm, pc])
loop_body.order.add_edge(hm, pc)
loop = OperatorPOWL(operator=Operator.LOOP, children=[skip, loop_body])

# Exclusive choice for optional workshop setup vs community outreach
workshop_xor = OperatorPOWL(operator=Operator.XOR, children=[ws, co])

# Build the partial order
root = StrictPartialOrder(nodes=[
    cs, hd, ss, ip, hs, si, loop, hh, wp, pp, od, workshop_xor, rc, da, mp
])

# Sequence edges
root.order.add_edge(cs, hd)
root.order.add_edge(hd, ss)
root.order.add_edge(ss, ip)
root.order.add_edge(ip, hs)
root.order.add_edge(hs, si)
root.order.add_edge(si, loop)
root.order.add_edge(loop, hh)
root.order.add_edge(hh, wp)
root.order.add_edge(wp, pp)
root.order.add_edge(pp, od)
root.order.add_edge(od, workshop_xor)
root.order.add_edge(workshop_xor, rc)
root.order.add_edge(rc, da)
root.order.add_edge(da, mp)

# Optional edges
root.order.add_edge(ss, loop)
root.order.add_edge(ip, loop)
root.order.add_edge(hs, loop)
root.order.add_edge(si, loop)

# Print the root model for verification
print(root)