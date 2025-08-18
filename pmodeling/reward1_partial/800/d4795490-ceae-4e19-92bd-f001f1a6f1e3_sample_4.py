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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    farm_sourcing,
    lot_selection,
    bean_sorting,
    fermentation,
    drying_process,
    quality_control,
    chemical_testing,
    sensory_analysis,
    roast_profiling,
    eco_packaging,
    traceability_qr,
    cold_transport,
    env_monitoring,
    customer_feedback,
    subscription_adjust
])

# Define dependencies between transitions
root.order.add_edge(farm_sourcing, lot_selection)
root.order.add_edge(lot_selection, bean_sorting)
root.order.add_edge(bean_sorting, fermentation)
root.order.add_edge(fermentation, drying_process)
root.order.add_edge(drying_process, quality_control)
root.order.add_edge(quality_control, chemical_testing)
root.order.add_edge(chemical_testing, sensory_analysis)
root.order.add_edge(sensory_analysis, roast_profiling)
root.order.add_edge(roast_profiling, eco_packaging)
root.order.add_edge(eco_packaging, traceability_qr)
root.order.add_edge(traceability_qr, cold_transport)
root.order.add_edge(cold_transport, env_monitoring)
root.order.add_edge(env_monitoring, customer_feedback)
root.order.add_edge(customer_feedback, subscription_adjust)

# Optionally, add a loop node for customer feedback
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback])
root.order.add_edge(feedback_loop, customer_feedback)

# Print the root of the POWL model
print(root)