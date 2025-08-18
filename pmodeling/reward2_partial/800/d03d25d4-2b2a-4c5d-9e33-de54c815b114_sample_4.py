import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
farm_registration = Transition(label='Farm Registration')
lot_tagging = Transition(label='Lot Tagging')
soil_testing = Transition(label='Soil Testing')
harvest_logging = Transition(label='Harvest Logging')
coffee_sorting = Transition(label='Coffee Sorting')
sensory_profiling = Transition(label='Sensory Profiling')
quality_scoring = Transition(label='Quality Scoring')
blockchain_entry = Transition(label='Blockchain Entry')
environmental_audit = Transition(label='Environmental Audit')
farmer_feedback = Transition(label='Farmer Feedback')
dynamic_pricing = Transition(label='Dynamic Pricing')
roast_scheduling = Transition(label='Roast Scheduling')
batch_testing = Transition(label='Batch Testing')
certification_review = Transition(label='Certification Review')
distribution_prep = Transition(label='Distribution Prep')
consumer_feedback = Transition(label='Consumer Feedback')

# Define the partial order
root = StrictPartialOrder(nodes=[
    farm_registration, 
    lot_tagging, 
    soil_testing, 
    harvest_logging, 
    coffee_sorting, 
    sensory_profiling, 
    quality_scoring, 
    blockchain_entry, 
    environmental_audit, 
    farmer_feedback, 
    dynamic_pricing, 
    roast_scheduling, 
    batch_testing, 
    certification_review, 
    distribution_prep, 
    consumer_feedback
])

# Define the order dependencies
root.order.add_edge(farm_registration, lot_tagging)
root.order.add_edge(lot_tagging, soil_testing)
root.order.add_edge(soil_testing, harvest_logging)
root.order.add_edge(harvest_logging, coffee_sorting)
root.order.add_edge(coffee_sorting, sensory_profiling)
root.order.add_edge(sensory_profiling, quality_scoring)
root.order.add_edge(quality_scoring, blockchain_entry)
root.order.add_edge(blockchain_entry, environmental_audit)
root.order.add_edge(environmental_audit, farmer_feedback)
root.order.add_edge(farmer_feedback, dynamic_pricing)
root.order.add_edge(dynamic_pricing, roast_scheduling)
root.order.add_edge(roast_scheduling, batch_testing)
root.order.add_edge(batch_testing, certification_review)
root.order.add_edge(certification_review, distribution_prep)
root.order.add_edge(distribution_prep, consumer_feedback)

# Print the root model
print(root)