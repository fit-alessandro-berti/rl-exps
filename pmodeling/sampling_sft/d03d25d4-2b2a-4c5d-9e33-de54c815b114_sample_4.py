import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
fr_reg   = Transition(label='Farm Registration')
soil_tst = Transition(label='Soil Testing')
harvest  = Transition(label='Harvest Logging')
sort_coffee = Transition(label='Coffee Sorting')
sens_prof = Transition(label='Sensory Profiling')
qual_scoring = Transition(label='Quality Scoring')
block_entry = Transition(label='Blockchain Entry')
env_audit = Transition(label='Environmental Audit')
farmer_fb = Transition(label='Farmer Feedback')
dynamic_pr = Transition(label='Dynamic Pricing')
roast_sched = Transition(label='Roast Scheduling')
batch_test = Transition(label='Batch Testing')
cert_review = Transition(label='Certification Review')
dist_prep = Transition(label='Distribution Prep')
consumer_fb = Transition(label='Consumer Feedback')

# Build the core testing & certification partial order
core_po = StrictPartialOrder(nodes=[
    sens_prof, qual_scoring, block_entry, env_audit, farmer_fb,
    dynamic_pr, roast_sched, batch_test, cert_review, dist_prep
])
core_po.order.add_edge(sens_prof, qual_scoring)
core_po.order.add_edge(qual_scoring, block_entry)
core_po.order.add_edge(block_entry, env_audit)
core_po.order.add_edge(env_audit, farmer_fb)
core_po.order.add_edge(farmer_fb, dynamic_pr)
core_po.order.add_edge(dynamic_pr, roast_sched)
core_po.order.add_edge(roast_sched, batch_test)
core_po.order.add_edge(batch_test, cert_review)
core_po.order.add_edge(cert_review, dist_prep)

# Build the loop for continuous feedback & adaptive pricing
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[consumer_fb, dist_prep])

# Assemble the full root partial order
root = StrictPartialOrder(nodes=[
    fr_reg, soil_tst, harvest, sort_coffee, core_po, feedback_loop
])
root.order.add_edge(fr_reg, soil_tst)
root.order.add_edge(soil_tst, harvest)
root.order.add_edge(harvest, sort_coffee)
root.order.add_edge(sort_coffee, core_po)
root.order.add_edge(core_po, feedback_loop)