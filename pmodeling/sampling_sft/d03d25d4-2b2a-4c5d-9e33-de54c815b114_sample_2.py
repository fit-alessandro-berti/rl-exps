import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
farm_reg = Transition(label='Farm Registration')
lot_tag = Transition(label='Lot Tagging')
soil_test = Transition(label='Soil Testing')
harvest_log = Transition(label='Harvest Logging')
coffee_sort = Transition(label='Coffee Sorting')
sens_prof = Transition(label='Sensory Profiling')
quality_score = Transition(label='Quality Scoring')
blockchain_entry = Transition(label='Blockchain Entry')
env_audit = Transition(label='Environmental Audit')
farmer_feed = Transition(label='Farmer Feedback')
dynamic_pricing = Transition(label='Dynamic Pricing')
roast_sched = Transition(label='Roast Scheduling')
batch_test = Transition(label='Batch Testing')
cert_review = Transition(label='Certification Review')
dist_prep = Transition(label='Distribution Prep')
cons_feed = Transition(label='Consumer Feedback')

# Silent transition for loop exit
skip = SilentTransition()

# Build the sensory profiling & quality scoring sub-process as a partial order
profiling_po = StrictPartialOrder(nodes=[sens_prof, quality_score])
profiling_po.order.add_edge(sens_prof, quality_score)

# Build the dynamic pricing & farmer feedback sub-process as a partial order
pricing_po = StrictPartialOrder(nodes=[dynamic_pricing, farmer_feed])
pricing_po.order.add_edge(dynamic_pricing, farmer_feed)

# Build the environmental audit & certification review sub-process as a partial order
audit_po = StrictPartialOrder(nodes=[env_audit, cert_review])
audit_po.order.add_edge(env_audit, cert_review)

# Build the roast scheduling & distribution preparation sub-process as a partial order
roast_po = StrictPartialOrder(nodes=[roast_sched, dist_prep])
roast_po.order.add_edge(roast_sched, dist_prep)

# Loop: perform profiling & scoring, then optionally do pricing & feedback,
#       then repeat profiling & scoring again, repeated until exit
loop_prof = OperatorPOWL(
    operator=Operator.LOOP,
    children=[profiling_po, pricing_po]
)

# Build the complete root process as a strict partial order
root = StrictPartialOrder(
    nodes=[
        farm_reg,
        lot_tag,
        soil_test,
        harvest_log,
        coffee_sort,
        loop_prof,
        block_chain_entry,
        audit_po,
        roast_po,
        batch_test,
        cons_feed
    ]
)

# Define the control-flow dependencies
root.order.add_edge(farm_reg, lot_tag)
root.order.add_edge(lot_tag, soil_test)
root.order.add_edge(soil_test, harvest_log)
root.order.add_edge(harvest_log, coffee_sort)
root.order.add_edge(coffee_sort, loop_prof)
root.order.add_edge(loop_prof, block_chain_entry)
root.order.add_edge(block_chain_entry, audit_po)
root.order.add_edge(audit_po, roast_po)
root.order.add_edge(roast_po, batch_test)
root.order.add_edge(batch_test, cons_feed)

# Print the root model for verification
print(root)