import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Define the maintenance loop: do Data Analysis, then either exit or do Maintenance Plan and repeat
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[da, mp]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    cs, hd, ss, ip, hs, si, hm, pc, hh, wp, pp, od, ws, co, rc, maintenance_loop
])

# Add control-flow dependencies
root.order.add_edge(cs, hd)
root.order.add_edge(hd, ss)
root.order.add_edge(ss, ip)
root.order.add_edge(ip, hs)
root.order.add_edge(hs, si)
root.order.add_edge(si, hm)
root.order.add_edge(hm, pc)
root.order.add_edge(pc, hh)
root.order.add_edge(hh, wp)
root.order.add_edge(wp, pp)
root.order.add_edge(pp, od)
root.order.add_edge(od, ws)
root.order.add_edge(ws, co)
root.order.add_edge(co, rc)
root.order.add_edge(rc, maintenance_loop)
root.order.add_edge(maintenance_loop, rc)  # loop back to regulation check