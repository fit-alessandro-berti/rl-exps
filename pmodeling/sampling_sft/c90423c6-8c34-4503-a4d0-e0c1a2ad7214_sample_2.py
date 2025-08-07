import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
farm_sel   = Transition(label='Farm Selection')
sample_tst = Transition(label='Sample Testing')
trade_neg  = Transition(label='Trade Negotiation')
ml_sort    = Transition(label='Micro-Lot Sorting')
ferm_ctrl  = Transition(label='Fermentation Control')
profiling  = Transition(label='Sensory Profiling')
roast_cal  = Transition(label='Roast Calibration')
blend_cr   = Transition(label='Blend Creation')
sustain_a  = Transition(label='Sustainability Audit')
pack_des   = Transition(label='Packaging Design')
q_inspect  = Transition(label='Quality Inspection')
inv_sync   = Transition(label='Inventory Sync')
log_plan   = Transition(label='Logistics Planning')
cafe_tr    = Transition(label='Cafe Training')
dp_pricing = Transition(label='Dynamic Pricing')
cf_feedback= Transition(label='Customer Feedback')
tr_logging = Transition(label='Traceability Logging')

# Loop for continuous sensory profiling and fermentation control
prof_fer_loop = OperatorPOWL(operator=Operator.LOOP, children=[profiling, ferm_ctrl])

# Build the partial order
root = StrictPartialOrder(nodes=[
    farm_sel, sample_tst, trade_neg, ml_sort,
    prof_fer_loop, roast_cal, blend_cr, sustain_a,
    pack_des, q_inspect, inv_sync, log_plan,
    cafe_tr, dp_pricing, cf_feedback, tr_logging
])

# Define the control-flow dependencies
root.order.add_edge(farm_sel, sample_tst)
root.order.add_edge(sample_tst, trade_neg)
root.order.add_edge(trade_neg, ml_sort)
root.order.add_edge(ml_sort, prof_fer_loop)
root.order.add_edge(prof_fer_loop, roast_cal)
root.order.add_edge(roast_cal, blend_cr)
root.order.add_edge(blend_cr, sustain_a)
root.order.add_edge(sustain_a, pack_des)
root.order.add_edge(pack_des, q_inspect)
root.order.add_edge(q_inspect, inv_sync)
root.order.add_edge(inv_sync, log_plan)
root.order.add_edge(log_plan, cafe_tr)
root.order.add_edge(cafe_tr, dp_pricing)
root.order.add_edge(dp_pricing, cf_feedback)
root.order.add_edge(cf_feedback, tr_logging)