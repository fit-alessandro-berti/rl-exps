import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
cs = Transition(label='Colony Sourcing')
hs = Transition(label='Hive Design')
ss = Transition(label='Site Survey')
ip = Transition(label='Installation Prep')
hsu = Transition(label='Hive Setup')
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

# Loop for continuous monitoring and maintenance
loop = OperatorPOWL(operator=Operator.LOOP, children=[hm, pc])

# Build the partial order
root = StrictPartialOrder(nodes=[
    cs, hs, ss, ip, hsu, si, loop, wp, pp, od, ws, co, rc, da, mp
])

# Define the control-flow dependencies
root.order.add_edge(cs, hs)
root.order.add_edge(hs, ss)
root.order.add_edge(ss, ip)
root.order.add_edge(ip, hsu)
root.order.add_edge(hsu, si)
root.order.add_edge(si, loop)
root.order.add_edge(loop, wp)
root.order.add_edge(loop, pp)
root.order.add_edge(wp, od)
root.order.add_edge(pp, od)
root.order.add_edge(od, ws)
root.order.add_edge(ws, co)
root.order.add_edge(ws, rc)
root.order.add_edge(ws, da)
root.order.add_edge(ws, mp)