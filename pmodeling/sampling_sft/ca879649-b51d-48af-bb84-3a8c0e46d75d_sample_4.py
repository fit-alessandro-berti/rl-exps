import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ms = Transition(label='Milk Sourcing')
qt = Transition(label='Quality Testing')
bs = Transition(label='Batch Selection')
cp = Transition(label='Curd Preparation')
pc = Transition(label='Pressing Cheese')
ac = Transition(label='Aging Control')
fp = Transition(label='Flavor Profiling')
pp = Transition(label='Packaging Prep')
cpk = Transition(label='Climate Packing')
el = Transition(label='Export Licensing')
cf = Transition(label='Customs Filing')
fb = Transition(label='Freight Booking')
cs = Transition(label='Cold Storage')
tt = Transition(label='Transport Tracking')
rd = Transition(label='Retail Delivery')
fc = Transition(label='Feedback Collection')

# Build the aging loop: do aging control, then optionally do flavor profiling and repeat
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ac, fp]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    ms, qt, bs, cp, pc, aging_loop,
    pp, cpk, el, cf, fb, cs, tt, rd, fc
])

# Define the control-flow dependencies
root.order.add_edge(ms, qt)
root.order.add_edge(qt, bs)
root.order.add_edge(bs, cp)
root.order.add_edge(cp, pc)
root.order.add_edge(pc, aging_loop)

# After aging, do packaging prep and climate packing
root.order.add_edge(aging_loop, pp)
root.order.add_edge(aging_loop, cpk)

# Licensing, filing, and booking must happen after packaging
root.order.add_edge(pp, el)
root.order.add_edge(cpk, el)
root.order.add_edge(el, cf)
root.order.add_edge(cf, fb)
root.order.add_edge(fb, cs)

# Transport and delivery must happen after cold storage
root.order.add_edge(cs, tt)
root.order.add_edge(tt, rd)

# Feedback must happen after delivery
root.order.add_edge(rd, fc)