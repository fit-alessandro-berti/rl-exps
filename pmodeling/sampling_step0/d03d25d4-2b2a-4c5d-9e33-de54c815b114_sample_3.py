from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the process
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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
root = StrictPartialOrder()

# Define the loop nodes
micro_lot_loop = OperatorPOWL(operator=Operator.LOOP, children=[farm_registration, lot_tagging, soil_testing, harvest_logging, coffee_sorting])
sensory_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensory_profiling, quality_scoring])
blockchain_loop = OperatorPOWL(operator=Operator.LOOP, children=[blockchain_entry])
environmental_loop = OperatorPOWL(operator=Operator.LOOP, children=[environmental_audit])
farmer_loop = OperatorPOWL(operator=Operator.LOOP, children=[farmer_feedback])
dynamic_loop = OperatorPOWL(operator=Operator.LOOP, children=[dynamic_pricing])
roast_loop = OperatorPOWL(operator=Operator.LOOP, children=[roast_scheduling])
batch_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_testing])
certification_loop = OperatorPOWL(operator=Operator.LOOP, children=[certification_review])
distribution_loop = OperatorPOWL(operator=Operator.LOOP, children=[distribution_prep])
consumer_loop = OperatorPOWL(operator=Operator.LOOP, children=[consumer_feedback])

# Define the XOR nodes
xor_micro_lot = OperatorPOWL(operator=Operator.XOR, children=[micro_lot_loop, skip])
xor_sensory = OperatorPOWL(operator=Operator.XOR, children=[sensory_loop, skip])
xor_blockchain = OperatorPOWL(operator=Operator.XOR, children=[blockchain_loop, skip])
xor_environmental = OperatorPOWL(operator=Operator.XOR, children=[environmental_loop, skip])
xor_farmer = OperatorPOWL(operator=Operator.XOR, children=[farmer_loop, skip])
xor_dynamic = OperatorPOWL(operator=Operator.XOR, children=[dynamic_loop, skip])
xor_roast = OperatorPOWL(operator=Operator.XOR, children=[roast_loop, skip])
xor_batch = OperatorPOWL(operator=Operator.XOR, children=[batch_loop, skip])
xor_certification = OperatorPOWL(operator=Operator.XOR, children=[certification_loop, skip])
xor_distribution = OperatorPOWL(operator=Operator.XOR, children=[distribution_loop, skip])
xor_consumer = OperatorPOWL(operator=Operator.XOR, children=[consumer_loop, skip])

# Add the nodes to the POWL model
root.nodes = [xor_micro_lot, xor_sensory, xor_blockchain, xor_environmental, xor_farmer, xor_dynamic, xor_roast, xor_batch, xor_certification, xor_distribution, xor_consumer]

# Define the dependencies between nodes
root.order.add_edge(xor_micro_lot, xor_sensory)
root.order.add_edge(xor_sensory, xor_blockchain)
root.order.add_edge(xor_blockchain, xor_environmental)
root.order.add_edge(xor_environmental, xor_farmer)
root.order.add_edge(xor_farmer, xor_dynamic)
root.order.add_edge(xor_dynamic, xor_roast)
root.order.add_edge(xor_roast, xor_batch)
root.order.add_edge(xor_batch, xor_certification)
root.order.add_edge(xor_certification, xor_distribution)
root.order.add_edge(xor_distribution, xor_consumer)

# Save the POWL model in the variable 'root'