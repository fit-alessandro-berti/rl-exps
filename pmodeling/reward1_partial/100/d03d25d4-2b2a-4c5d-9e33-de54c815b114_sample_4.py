from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the coffee supply chain process
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

# Define the relationships between the activities using the POWL model
farm_registration_choice = OperatorPOWL(operator=Operator.XOR, children=[farm_registration, lot_tagging])
soil_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[soil_testing, harvest_logging])
coffee_sorting_choice = OperatorPOWL(operator=Operator.XOR, children=[coffee_sorting, sensory_profiling])
quality_scoring_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_scoring, blockchain_entry])
environmental_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[environmental_audit, farmer_feedback])
dynamic_pricing_choice = OperatorPOWL(operator=Operator.XOR, children=[dynamic_pricing, roast_scheduling])
batch_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[batch_testing, certification_review])
distribution_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[distribution_prep, consumer_feedback])

# Define the loop structure for the process
loop = OperatorPOWL(operator=Operator.LOOP, children=[farm_registration_choice, soil_testing_choice, coffee_sorting_choice, quality_scoring_choice, environmental_audit_choice, dynamic_pricing_choice, batch_testing_choice, distribution_prep_choice])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, farm_registration_choice, soil_testing_choice, coffee_sorting_choice, quality_scoring_choice, environmental_audit_choice, dynamic_pricing_choice, batch_testing_choice, distribution_prep_choice])
root.order.add_edge(loop, farm_registration_choice)
root.order.add_edge(loop, soil_testing_choice)
root.order.add_edge(loop, coffee_sorting_choice)
root.order.add_edge(loop, quality_scoring_choice)
root.order.add_edge(loop, environmental_audit_choice)
root.order.add_edge(loop, dynamic_pricing_choice)
root.order.add_edge(loop, batch_testing_choice)
root.order.add_edge(loop, distribution_prep_choice)

print(root)