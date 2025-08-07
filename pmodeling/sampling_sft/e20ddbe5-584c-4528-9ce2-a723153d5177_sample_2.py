import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sa = Transition(label='Site Analysis')
lt = Transition(label='Load Test')
sm = Transition(label='Sunlight Map')
ms = Transition(label='Medium Select')
hd = Transition(label='Hydro Design')
ps = Transition(label='Procure Seeds')
ii = Transition(label='Install Irrigation')
sc = Transition(label='Setup Climate')
cs = Transition(label='Create Schedule')
pc = Transition(label='Pest Control')
mg = Transition(label='Monitor Growth')
asys = Transition(label='Adjust Systems')
hc = Transition(label='Harvest Crops')
pp = Transition(label='Package Produce')
ec = Transition(label='Engage Community')
hw = Transition(label='Host Workshops')

# Loop for regular monitoring and system adjustment
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[mg, asys]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    sa, lt, sm, ms, hd, ps, ii, sc, cs, pc, monitor_loop, hc, pp, ec, hw
])

# Sequence and concurrency
root.order.add_edge(sa, lt)
root.order.add_edge(sa, sm)
root.order.add_edge(lt, ms)
root.order.add_edge(sm, ms)
root.order.add_edge(ms, hd)
root.order.add_edge(hd, ps)
root.order.add_edge(ps, ii)
root.order.add_edge(ps, sc)
root.order.add_edge(ii, cs)
root.order.add_edge(sc, cs)
root.order.add_edge(cs, pc)
root.order.add_edge(pc, monitor_loop)
root.order.add_edge(monitor_loop, hc)
root.order.add_edge(monitor_loop, pp)
root.order.add_edge(hc, ec)
root.order.add_edge(pp, ec)
root.order.add_edge(ec, hw)