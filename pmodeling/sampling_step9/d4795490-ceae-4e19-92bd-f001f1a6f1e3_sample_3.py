import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()

# Define the POWL structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[farm_sourcing, lot_selection, bean_sorting, fermentation, drying_process, quality_control])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[chemical_testing, sensory_analysis])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[roast_profiling, eco_packaging, traceability_qr])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[cold_transport, env_monitoring])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, subscription_adjust])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop3, loop4])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop5, skip])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor1)

# Save the final result in the variable 'root'