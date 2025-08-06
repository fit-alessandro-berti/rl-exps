from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loops
micro_lot_loop = OperatorPOWL(operator=Operator.LOOP, children=[farm_registration, lot_tagging, soil_testing, harvest_logging, coffee_sorting, sensory_profiling, quality_scoring, blockchain_entry, environmental_audit, farmer_feedback, dynamic_pricing, roast_scheduling])
batch_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_testing, certification_review, distribution_prep, consumer_feedback])

# Define exclusive choices
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[micro_lot_loop, batch_loop])

# Define root
root = StrictPartialOrder(nodes=[exclusive_choice])
root.order.add_edge(exclusive_choice, batch_loop)

print(root)