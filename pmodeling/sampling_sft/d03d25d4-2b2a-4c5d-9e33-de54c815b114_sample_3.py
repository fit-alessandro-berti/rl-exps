import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
farm_reg = Transition(label='Farm Registration')
harvest_log = Transition(label='Harvest Logging')
soil_test = Transition(label='Soil Testing')
lot_tag = Transition(label='Lot Tagging')
coffee_sort = Transition(label='Coffee Sorting')
sensory_prof = Transition(label='Sensory Profiling')
quality_score = Transition(label='Quality Scoring')
blockchain_entry = Transition(label='Blockchain Entry')
farmer_feed = Transition(label='Farmer Feedback')
env_audit = Transition(label='Environmental Audit')
dynamic_price = Transition(label='Dynamic Pricing')
roast_sched = Transition(label='Roast Scheduling')
batch_test = Transition(label='Batch Testing')
cert_review = Transition(label='Certification Review')
dist_prep = Transition(label='Distribution Prep')
cons_feed = Transition(label='Consumer Feedback')

# Build the loop body: sensory profiling, quality scoring, blockchain entry
body = StrictPartialOrder(nodes=[sensory_prof, quality_score, blockchain_entry])
# no edges => concurrent execution

# Build the loop: loop over the body, then optionally do farmer feedback and environmental audit
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, farmer_feed])

# Build the dynamic pricing loop: loop over dynamic pricing, then optionally do environmental audit
dynamic_loop = OperatorPOWL(operator=Operator.LOOP, children=[dynamic_price, env_audit])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    farm_reg, harvest_log, soil_test, lot_tag, coffee_sort,
    loop, dynamic_loop,
    roast_sched, batch_test, cert_review, dist_prep, cons_feed
])

# Define the control-flow dependencies
root.order.add_edge(farm_reg, harvest_log)
root.order.add_edge(harvest_log, soil_test)
root.order.add_edge(soil_test, lot_tag)
root.order.add_edge(lot_tag, coffee_sort)
root.order.add_edge(coffee_sort, loop)
root.order.add_edge(loop, dynamic_loop)
root.order.add_edge(dynamic_loop, roast_sched)
root.order.add_edge(roast_sched, batch_test)
root.order.add_edge(batch_test, cert_review)
root.order.add_edge(cert_review, dist_prep)
root.order.add_edge(dist_prep, cons_feed)