import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names
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

# Define the partial order
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

# Add dependencies if necessary (not specified in the problem statement)
# For example, if Lot Selection depends on Farm Sourcing:
# root.order.add_edge(farm_sourcing, lot_selection)

# Save the final result in the variable 'root'
print(root)