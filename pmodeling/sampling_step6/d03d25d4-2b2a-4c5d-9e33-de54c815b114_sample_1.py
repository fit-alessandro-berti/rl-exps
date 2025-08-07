import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the root process
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

# Optionally, if there are any dependencies, you can add them here
# For example, if some activities depend on others, you can add edges to the 'order' attribute of 'root'

# You can print the root to see its structure
print(root)