import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loops
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[fermentation, drying_process])
cold_transport_loop = OperatorPOWL(operator=Operator.LOOP, children=[cold_transport, env_monitoring])

# Define exclusive choices
quality_control_choice = OperatorPOWL(operator=Operator.XOR, children=[chemical_testing, sensory_analysis])
roast_profile_choice = OperatorPOWL(operator=Operator.XOR, children=[roast_profiling, subscription_adjust])

# Define the root POWL model
root = StrictPartialOrder(nodes=[farm_sourcing, lot_selection, bean_sorting, fermentation_loop, quality_control_choice, roast_profile_choice, eco_packaging, traceability_qr, cold_transport_loop, customer_feedback, subscription_adjust])
root.order.add_edge(farm_sourcing, lot_selection)
root.order.add_edge(lot_selection, bean_sorting)
root.order.add_edge(bean_sorting, fermentation_loop)
root.order.add_edge(fermentation_loop, quality_control_choice)
root.order.add_edge(quality_control_choice, roast_profile_choice)
root.order.add_edge(roast_profile_choice, eco_packaging)
root.order.add_edge(eco_packaging, traceability_qr)
root.order.add_edge(traceability_qr, cold_transport_loop)
root.order.add_edge(cold_transport_loop, customer_feedback)
root.order.add_edge(customer_feedback, subscription_adjust)