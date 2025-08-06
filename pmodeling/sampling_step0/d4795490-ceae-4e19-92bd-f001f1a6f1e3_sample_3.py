import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the operators
xor = OperatorPOWL(operator=Operator.XOR, children=[drying_process, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_control, xor])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[roast_profiling, eco_packaging])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[cold_transport, env_monitoring])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, subscription_adjust])

# Define the root POWL model
root = StrictPartialOrder(nodes=[farm_sourcing, lot_selection, bean_sorting, fermentation, loop, xor2, xor3, xor4])
root.order.add_edge(farm_sourcing, lot_selection)
root.order.add_edge(lot_selection, bean_sorting)
root.order.add_edge(bean_sorting, fermentation)
root.order.add_edge(fermentation, loop)
root.order.add_edge(loop, quality_control)
root.order.add_edge(quality_control, xor)
root.order.add_edge(xor, drying_process)
root.order.add_edge(drying_process, xor2)
root.order.add_edge(xor2, roast_profiling)
root.order.add_edge(roast_profiling, eco_packaging)
root.order.add_edge(eco_packaging, xor3)
root.order.add_edge(xor3, cold_transport)
root.order.add_edge(cold_transport, env_monitoring)
root.order.add_edge(env_monitoring, xor4)
root.order.add_edge(xor4, customer_feedback)
root.order.add_edge(customer_feedback, subscription_adjust)

print(root)