import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sa = Transition(label='Site Acquisition')
ia = Transition(label='Impact Assess')
ms = Transition(label='Modular Setup')
cp = Transition(label='Crop Planting')
nc = Transition(label='Nutrient Control')
pc = Transition(label='Pest Control')
gm = Transition(label='Growth Monitor')
ce = Transition(label='Community Engage')
yf = Transition(label='Yield Forecast')
sc = Transition(label='Supply Coordinate')
cc = Transition(label='Compliance Check')
wr = Transition(label='Waste Recycle')
eo = Transition(label='Energy Optimize')
msy = Transition(label='Market Strategy')
pr = Transition(label='Performance Review')

# Loop for continuous monitoring and adjustments
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[gm, OperatorPOWL(operator=Operator.XOR, children=[ce, SilentTransition()])]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    sa, ia, ms, cp, nc, pc, monitor_loop, yf, sc, cc, wr, eo, msy, pr
])

# Sequence: Site Acquisition -> Impact Assess -> Modular Setup
root.order.add_edge(sa, ia)
root.order.add_edge(ia, ms)

# After setup, all other activities are concurrent
for act in [cp, nc, pc, yf, sc, cc, wr, eo, msy]:
    root.order.add_edge(ms, act)

# Monitor loop follows all setup activities
for act in [cp, nc, pc, yf, sc, cc, wr, eo, msy]:
    root.order.add_edge(act, monitor_loop)

# Performance review at the end
root.order.add_edge(monitor_loop, pr)