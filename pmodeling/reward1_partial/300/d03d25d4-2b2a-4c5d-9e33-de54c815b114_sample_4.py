import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

lot_tagging_to_soil_testing = OperatorPOWL(operator=Operator.XOR, children=[lot_tagging, skip])
soil_testing_to_harvest_logging = OperatorPOWL(operator=Operator.XOR, children=[soil_testing, skip])
harvest_logging_to_coffee_sorting = OperatorPOWL(operator=Operator.XOR, children=[harvest_logging, skip])
coffee_sorting_to_sensory_profiling = OperatorPOWL(operator=Operator.XOR, children=[coffee_sorting, skip])
sensory_profiling_to_quality_scoring = OperatorPOWL(operator=Operator.XOR, children=[sensory_profiling, skip])
quality_scoring_to_blockchain_entry = OperatorPOWL(operator=Operator.XOR, children=[quality_scoring, skip])
blockchain_entry_to_environmental_audit = OperatorPOWL(operator=Operator.XOR, children=[blockchain_entry, skip])
environmental_audit_to_farmer_feedback = OperatorPOWL(operator=Operator.XOR, children=[environmental_audit, skip])
farmer_feedback_to_dynamic_pricing = OperatorPOWL(operator=Operator.XOR, children=[farmer_feedback, skip])
dynamic_pricing_to_roast_scheduling = OperatorPOWL(operator=Operator.XOR, children=[dynamic_pricing, skip])
roast_scheduling_to_batch_testing = OperatorPOWL(operator=Operator.XOR, children=[roast_scheduling, skip])
batch_testing_to_certification_review = OperatorPOWL(operator=Operator.XOR, children=[batch_testing, skip])
certification_review_to_distribution_prep = OperatorPOWL(operator=Operator.XOR, children=[certification_review, skip])
distribution_prep_to_consumer_feedback = OperatorPOWL(operator=Operator.XOR, children=[distribution_prep, skip])

root = StrictPartialOrder(nodes=[
    lot_tagging_to_soil_testing,
    soil_testing_to_harvest_logging,
    harvest_logging_to_coffee_sorting,
    coffee_sorting_to_sensory_profiling,
    sensory_profiling_to_quality_scoring,
    quality_scoring_to_blockchain_entry,
    blockchain_entry_to_environmental_audit,
    environmental_audit_to_farmer_feedback,
    farmer_feedback_to_dynamic_pricing,
    dynamic_pricing_to_roast_scheduling,
    roast_scheduling_to_batch_testing,
    batch_testing_to_certification_review,
    certification_review_to_distribution_prep,
    distribution_prep_to_consumer_feedback
])

root.order.add_edge(lot_tagging_to_soil_testing, soil_testing_to_harvest_logging)
root.order.add_edge(soil_testing_to_harvest_logging, harvest_logging_to_coffee_sorting)
root.order.add_edge(harvest_logging_to_coffee_sorting, coffee_sorting_to_sensory_profiling)
root.order.add_edge(coffee_sorting_to_sensory_profiling, sensory_profiling_to_quality_scoring)
root.order.add_edge(sensory_profiling_to_quality_scoring, quality_scoring_to_blockchain_entry)
root.order.add_edge(quality_scoring_to_blockchain_entry, blockchain_entry_to_environmental_audit)
root.order.add_edge(blockchain_entry_to_environmental_audit, environmental_audit_to_farmer_feedback)
root.order.add_edge(environmental_audit_to_farmer_feedback, farmer_feedback_to_dynamic_pricing)
root.order.add_edge(farmer_feedback_to_dynamic_pricing, dynamic_pricing_to_roast_scheduling)
root.order.add_edge(dynamic_pricing_to_roast_scheduling, roast_scheduling_to_batch_testing)
root.order.add_edge(roast_scheduling_to_batch_testing, batch_testing_to_certification_review)
root.order.add_edge(batch_testing_to_certification_review, certification_review_to_distribution_prep)
root.order.add_edge(certification_review_to_distribution_prep, distribution_prep_to_consumer_feedback)