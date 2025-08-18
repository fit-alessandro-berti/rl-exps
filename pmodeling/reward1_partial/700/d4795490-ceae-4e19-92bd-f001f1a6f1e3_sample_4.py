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

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[quality_control, chemical_testing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[sensory_analysis, roast_profiling])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, traceability_qr])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[cold_transport, env_monitoring])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, subscription_adjust])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[
    farm_sourcing, lot_selection, bean_sorting, fermentation, drying_process,
    xor1, xor2, xor3, xor4, xor5
])

# Define the dependencies
root.order.add_edge(farm_sourcing, lot_selection)
root.order.add_edge(lot_selection, bean_sorting)
root.order.add_edge(bean_sorting, fermentation)
root.order.add_edge(bean_sorting, drying_process)
root.order.add_edge(fermentation, xor1)
root.order.add_edge(drying_process, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor4, customer_feedback)
root.order.add_edge(xor5, subscription_adjust)

# Print the POWL model
print(root)