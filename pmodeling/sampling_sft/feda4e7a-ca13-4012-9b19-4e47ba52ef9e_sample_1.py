import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sa = Transition(label='Site Analysis')
es = Transition(label='Env Scanning')
fd = Transition(label='Farm Design')
nm = Transition(label='Nutrient Mix')
sa1 = Transition(label='Seed Automation')
gm = Transition(label='Growth Monitor')
pc = Transition(label='Pest Control')
ad = Transition(label='AI Diagnostics')
hp = Transition(label='Harvest Plan')
rs = Transition(label='Robotic Sort')
pl = Transition(label='Packaging Line')
ci = Transition(label='Community Input')
da = Transition(label='Data Aggregation')
wr = Transition(label='Waste Recycle')
cs = Transition(label='Sustainability')

# Loop for continuous monitoring & pest control
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[gm, pc])

# Build the partial order
root = StrictPartialOrder(nodes=[
    sa, es, fd, nm, sa1, monitor_loop,
    ad, hp, ci, da, wr, cs
])

# Define the control-flow dependencies
root.order.add_edge(sa, es)
root.order.add_edge(es, fd)
root.order.add_edge(fd, nm)
root.order.add_edge(nm, sa1)
root.order.add_edge(sa1, monitor_loop)
root.order.add_edge(monitor_loop, ad)
root.order.add_edge(ad, ci)
root.order.add_edge(ci, da)
root.order.add_edge(da, wr)
root.order.add_edge(wr, cs)
root.order.add_edge(cs, hp)