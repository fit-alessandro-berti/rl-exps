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

# Define silent transitions (tau)
tau1 = SilentTransition()
tau2 = SilentTransition()
tau3 = SilentTransition()

# Define loops and XORs
farm_loop = OperatorPOWL(operator=Operator.LOOP, children=[farm_registration, lot_tagging])
soil_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_testing, tau1])
harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_logging, coffee_sorting])
sensory_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensory_profiling, quality_scoring])
blockchain_loop = OperatorPOWL(operator=Operator.LOOP, children=[blockchain_entry, environmental_audit])
farmer_loop = OperatorPOWL(operator=Operator.LOOP, children=[farmer_feedback, dynamic_pricing])
roast_loop = OperatorPOWL(operator=Operator.LOOP, children=[roast_scheduling, batch_testing])
certification_loop = OperatorPOWL(operator=Operator.LOOP, children=[certification_review, distribution_prep])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[consumer_feedback, tau2])

# Define the root partial order
root = StrictPartialOrder(nodes=[
    farm_loop,
    soil_test_loop,
    harvest_loop,
    sensory_loop,
    blockchain_loop,
    farmer_loop,
    roast_loop,
    certification_loop,
    feedback_loop
])

# Add dependencies
root.order.add_edge(farm_loop, soil_test_loop)
root.order.add_edge(soil_test_loop, harvest_loop)
root.order.add_edge(harvest_loop, sensory_loop)
root.order.add_edge(sensory_loop, blockchain_loop)
root.order.add_edge(blockchain_loop, farmer_loop)
root.order.add_edge(farmer_loop, roast_loop)
root.order.add_edge(roast_loop, certification_loop)
root.order.add_edge(certification_loop, feedback_loop)

print(root)