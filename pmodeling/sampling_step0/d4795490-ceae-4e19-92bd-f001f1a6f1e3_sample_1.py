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

# Define the partial order structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[farm_sourcing, lot_selection, bean_sorting, fermentation, drying_process])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[quality_control, chemical_testing, sensory_analysis])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[roast_profiling, eco_packaging])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[cold_transport, env_monitoring])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[traceability_qr, customer_feedback])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[subscription_adjust, xor3])

root = StrictPartialOrder(nodes=[loop1, xor1, xor2, loop2, xor3, xor4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, loop2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, loop2)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor3)

print(root)