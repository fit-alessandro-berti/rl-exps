from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the process as a StrictPartialOrder model
root = StrictPartialOrder(
    nodes=[
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
    ],
    order={
        farm_registration: [lot_tagging],
        lot_tagging: [soil_testing, harvest_logging],
        soil_testing: [harvest_logging],
        harvest_logging: [coffee_sorting],
        coffee_sorting: [sensory_profiling],
        sensory_profiling: [quality_scoring, blockchain_entry],
        quality_scoring: [blockchain_entry],
        blockchain_entry: [environmental_audit, dynamic_pricing, roast_scheduling, batch_testing],
        environmental_audit: [dynamic_pricing, roast_scheduling, batch_testing],
        dynamic_pricing: [roast_scheduling, batch_testing],
        roast_scheduling: [batch_testing],
        batch_testing: [certification_review],
        certification_review: [distribution_prep],
        distribution_prep: [consumer_feedback]
    }
)