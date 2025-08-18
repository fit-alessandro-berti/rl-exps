from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[environmental_audit, farmer_feedback])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[dynamic_pricing, roast_scheduling])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[batch_testing, certification_review])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[distribution_prep, consumer_feedback])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[farmer_feedback, consumer_feedback])

# Define the partial order
root = StrictPartialOrder(nodes=[
    farm_registration, lot_tagging, soil_testing, harvest_logging, coffee_sorting, sensory_profiling, quality_scoring,
    blockchain_entry, xor1, xor2, xor3, xor4, xor5, consumer_feedback
])

# Define the dependencies
root.order.add_edge(farm_registration, lot_tagging)
root.order.add_edge(lot_tagging, soil_testing)
root.order.add_edge(soil_testing, harvest_logging)
root.order.add_edge(harvest_logging, coffee_sorting)
root.order.add_edge(coffee_sorting, sensory_profiling)
root.order.add_edge(sensory_profiling, quality_scoring)
root.order.add_edge(quality_scoring, blockchain_entry)
root.order.add_edge(blockchain_entry, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, consumer_feedback)

print(root)