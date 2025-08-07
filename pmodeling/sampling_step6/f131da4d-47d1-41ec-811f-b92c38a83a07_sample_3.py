import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_testing = Transition(label='Milk Testing')
fermentation_start = Transition(label='Fermentation Start')
temperature_control = Transition(label='Temperature Control')
pH_monitoring = Transition(label='pH Monitoring')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
molding_cheese = Transition(label='Molding Cheese')
salting_process = Transition(label='Salting Process')
aging_setup = Transition(label='Aging Setup')
quality_check = Transition(label='Quality Check')
packaging_prep = Transition(label='Packaging Prep')
label_design = Transition(label='Label Design')
distribution_plan = Transition(label='Distribution Plan')
retail_delivery = Transition(label='Retail Delivery')
customer_feedback = Transition(label='Customer Feedback')

# Define the root node as a strict partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_selection,
    milk_testing,
    fermentation_start,
    temperature_control,
    pH_monitoring,
    curd_cutting,
    whey_draining,
    molding_cheese,
    salting_process,
    aging_setup,
    quality_check,
    packaging_prep,
    label_design,
    distribution_plan,
    retail_delivery,
    customer_feedback
])
# Define the dependencies between activities (if any)
# For example, if there are dependencies, you would add them like this:
# root.order.add_edge(milk_sourcing, culture_selection)
# root.order.add_edge(milk_sourcing, milk_testing)
# root.order.add_edge(milk_sourcing, fermentation_start)
# root.order.add_edge(milk_sourcing, temperature_control)
# root.order.add_edge(milk_sourcing, pH_monitoring)
# root.order.add_edge(milk_sourcing, curd_cutting)
# root.order.add_edge(milk_sourcing, whey_draining)
# root.order.add_edge(milk_sourcing, molding_cheese)
# root.order.add_edge(milk_sourcing, salting_process)
# root.order.add_edge(milk_sourcing, aging_setup)
# root.order.add_edge(milk_sourcing, quality_check)
# root.order.add_edge(milk_sourcing, packaging_prep)
# root.order.add_edge(milk_sourcing, label_design)
# root.order.add_edge(milk_sourcing, distribution_plan)
# root.order.add_edge(milk_sourcing, retail_delivery)
# root.order.add_edge(milk_sourcing, customer_feedback)

# Print the root node to verify
print(root)