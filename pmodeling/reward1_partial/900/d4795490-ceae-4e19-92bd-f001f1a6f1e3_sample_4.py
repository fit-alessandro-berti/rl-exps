import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
farm_sourcing = Transition(label='Farm Sourcing')
lot_selection = Transition(label='Lot Selection')
bean_sorting = Transition(label='Bean Sorting')
fermentation = Transition(label='Fermentation')
drying_process = Transition(label='Drying Process')
quality_control = Transition(label='Quality Control')
chemical_testing = Transition(label='Chemical Testing')
sensory_analysis = Transition(label='Sensory Analysis')
roast_profiling = Transition(label='Roast Profiling')
eco_packaging = Transition(label='Eco Packaging')
traceability_qr = Transition(label='Traceability QR')
cold_transport = Transition(label='Cold Transport')
env_monitoring = Transition(label='Env Monitoring')
customer_feedback = Transition(label='Customer Feedback')
subscription_adjust = Transition(label='Subscription Adjust')

# Define the loop and choice nodes
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[farm_sourcing, lot_selection, bean_sorting, fermentation, drying_process, quality_control, chemical_testing, sensory_analysis, roast_profiling, eco_packaging, traceability_qr, cold_transport, env_monitoring])
xor_node = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, subscription_adjust])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_node, xor_node])
root.order.add_edge(loop_node, xor_node)

print(root)