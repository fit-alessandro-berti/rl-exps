import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

loop_farm_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[farm_sourcing, lot_selection, bean_sorting, fermentation, drying_process, quality_control, chemical_testing, sensory_analysis, roast_profiling])
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, traceability_qr])
loop_chemical_testing = OperatorPOWL(operator=Operator.LOOP, children=[cold_transport, env_monitoring])
xor_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, subscription_adjust])

root = StrictPartialOrder(nodes=[loop_farm_sourcing, xor_packaging, loop_chemical_testing, xor_customer_feedback])
root.order.add_edge(loop_farm_sourcing, xor_packaging)
root.order.add_edge(loop_farm_sourcing, loop_chemical_testing)
root.order.add_edge(xor_packaging, loop_chemical_testing)
root.order.add_edge(xor_packaging, xor_customer_feedback)
root.order.add_edge(loop_chemical_testing, xor_customer_feedback)

print(root)