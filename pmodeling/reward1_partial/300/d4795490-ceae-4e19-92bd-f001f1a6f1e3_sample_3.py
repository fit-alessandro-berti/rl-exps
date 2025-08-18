import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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
loop_fermentation = OperatorPOWL(operator=Operator.LOOP, children=[fermentation])
loop_drying = OperatorPOWL(operator=Operator.LOOP, children=[drying_process])
xor_quality_control = OperatorPOWL(operator=Operator.XOR, children=[quality_control, chemical_testing])
xor_sensory_analysis = OperatorPOWL(operator=Operator.XOR, children=[sensory_analysis, roast_profiling])
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, traceability_qr])
loop_transport = OperatorPOWL(operator=Operator.LOOP, children=[cold_transport, env_monitoring])
xor_subscription = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, subscription_adjust])

# Construct the root POWL model
root = StrictPartialOrder(nodes=[
    farm_sourcing,
    lot_selection,
    bean_sorting,
    loop_fermentation,
    loop_drying,
    xor_quality_control,
    xor_sensory_analysis,
    xor_packaging,
    loop_transport,
    xor_subscription
])

# Define the dependencies (order)
root.order.add_edge(farm_sourcing, lot_selection)
root.order.add_edge(lot_selection, bean_sorting)
root.order.add_edge(bean_sorting, loop_fermentation)
root.order.add_edge(loop_fermentation, loop_drying)
root.order.add_edge(loop_drying, xor_quality_control)
root.order.add_edge(xor_quality_control, xor_sensory_analysis)
root.order.add_edge(xor_sensory_analysis, xor_packaging)
root.order.add_edge(xor_packaging, loop_transport)
root.order.add_edge(loop_transport, xor_subscription)

# Print the root POWL model
print(root)