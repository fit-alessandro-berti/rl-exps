import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
sa = Transition(label='Site Analysis')
dl = Transition(label='Design Layout')
ma = Transition(label='Module Assembly')
cs = Transition(label='Climate Setup')
si = Transition(label='Sensor Install')
wt = Transition(label='Water Testing')
nm = Transition(label='Nutrient Mix')
ss = Transition(label='Seed Selection')
ph = Transition(label='Planting Phase')
gm = Transition(label='Growth Monitor')
pc = Transition(label='Pest Control')
hp = Transition(label='Harvest Plan')
ya = Transition(label='Yield Audit')
pp = Transition(label='Packaging Prep')
md = Transition(label='Market Delivery')
wr = Transition(label='Waste Recycling')

# Build the partial order
root = StrictPartialOrder(nodes=[
    sa, dl, ma, cs, si, wt, nm, ss, ph, gm, pc, hp, ya, pp, md, wr
])

# Site Analysis -> Design Layout
root.order.add_edge(sa, dl)

# Design Layout -> Module Assembly
root.order.add_edge(dl, ma)

# Module Assembly -> Climate Setup
root.order.add_edge(ma, cs)

# Climate Setup -> Sensor Install
root.order.add_edge(cs, si)

# Sensor Install -> Water Testing
root.order.add_edge(si, wt)

# Water Testing -> Nutrient Mix
root.order.add_edge(wt, nm)

# Nutrient Mix -> Seed Selection
root.order.add_edge(nm, ss)

# Seed Selection -> Planting Phase
root.order.add_edge(ss, ph)

# Planting Phase -> Growth Monitor
root.order.add_edge(ph, gm)

# Growth Monitor -> Pest Control
root.order.add_edge(gm, pc)

# Pest Control -> Harvest Plan
root.order.add_edge(pc, hp)

# Harvest Plan -> Yield Audit
root.order.add_edge(hp, ya)

# Yield Audit -> Packaging Prep
root.order.add_edge(ya, pp)

# Packaging Prep -> Market Delivery
root.order.add_edge(pp, md)

# Market Delivery -> Waste Recycling
root.order.add_edge(md, wr)