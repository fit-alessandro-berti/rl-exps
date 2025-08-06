import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the loop for the coffee processing
coffee_processing_loop = OperatorPOWL(operator=Operator.LOOP, children=[
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
    certification_review
])

# Define the XOR for the distribution preparation and consumer feedback
distribution_xor = OperatorPOWL(operator=Operator.XOR, children=[
    distribution_prep,
    consumer_feedback
])

# Define the root POWL model
root = StrictPartialOrder(nodes=[coffee_processing_loop, distribution_xor])
root.order.add_edge(coffee_processing_loop, distribution_xor)

# Print the root POWL model
print(root)