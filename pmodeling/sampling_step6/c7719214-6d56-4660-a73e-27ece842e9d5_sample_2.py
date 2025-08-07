import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
milk_sourcing = Transition(label='Milk Sourcing')
diet_monitoring = Transition(label='Diet Monitoring')
culture_selection = Transition(label='Culture Selection')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
mold_inoculate = Transition(label='Mold Inoculate')
press_forming = Transition(label='Press Forming')
salt_application = Transition(label='Salt Application')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
flavor_testing = Transition(label='Flavor Testing')
packaging_design = Transition(label='Packaging Design')
order_processing = Transition(label='Order Processing')
retail_delivery = Transition(label='Retail Delivery')
event_coordination = Transition(label='Event Coordination')
feedback_review = Transition(label='Feedback Review')

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    diet_monitoring,
    culture_selection,
    milk_pasteurize,
    curd_cutting,
    whey_draining,
    mold_inoculate,
    press_forming,
    salt_application,
    aging_setup,
    humidity_control,
    flavor_testing,
    packaging_design,
    order_processing,
    retail_delivery,
    event_coordination,
    feedback_review
])

# No explicit ordering is defined in this simple example, but you can add dependencies if needed.
# For example, to ensure that 'Diet Monitoring' happens before 'Culture Selection':
# root.order.add_edge(diet_monitoring, culture_selection)

# If you need to add more complex dependencies, you can use the 'add_edge' method to specify them.
# For instance, if 'Milk Sourcing' must happen before 'Diet Monitoring':
# root.order.add_edge(milk_sourcing, diet_monitoring)

# This is the final POWL model for the artisan cheese production process.