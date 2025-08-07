import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
fr = Transition(label='Farm Registration')
hl = Transition(label='Harvest Logging')
st = Transition(label='Soil Testing')
so = Transition(label='Coffee Sorting')
sp = Transition(label='Sensory Profiling')
qs = Transition(label='Quality Scoring')
be = Transition(label='Blockchain Entry')
ea = Transition(label='Environmental Audit')
ff = Transition(label='Farmer Feedback')
dp = Transition(label='Dynamic Pricing')
rs = Transition(label='Roast Scheduling')
bt = Transition(label='Batch Testing')
cr = Transition(label='Certification Review')
dp2 = Transition(label='Distribution Prep')
cf = Transition(label='Consumer Feedback')

# Build the dynamic pricing loop: do Dynamic Pricing, then either exit or re-do Dynamic Pricing and back
dp_loop = OperatorPOWL(operator=Operator.LOOP, children=[dp, dp])

# Build the main sequence as a strict partial order
main_seq = StrictPartialOrder(nodes=[
    fr, hl, st, so, sp, qs, be, ea, ff,
    dp_loop, rs, bt, cr, dp2, cf
])

# Define the control-flow dependencies
main_seq.order.add_edge(fr, hl)
main_seq.order.add_edge(hl, st)
main_seq.order.add_edge(st, so)
main_seq.order.add_edge(so, sp)
main_seq.order.add_edge(sp, qs)
main_seq.order.add_edge(qs, be)
main_seq.order.add_edge(be, ea)
main_seq.order.add_edge(ea, ff)
main_seq.order.add_edge(ff, dp_loop)
main_seq.order.add_edge(dp_loop, rs)
main_seq.order.add_edge(rs, bt)
main_seq.order.add_edge(bt, cr)
main_seq.order.add_edge(cr, dp2)
main_seq.order.add_edge(dp2, cf)

# Final root model
root = main_seq