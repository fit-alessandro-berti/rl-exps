import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
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

# Define the partial order
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
# No additional dependencies specified in the problem description, so no edges are added in this case.

# Print the root node
print(root)