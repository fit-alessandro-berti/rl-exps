import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the artisan cheese process
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

# Define the partial order structure of the process
root = StrictPartialOrder(nodes=[
    milk_sourcing, culture_selection, milk_testing, fermentation_start,
    temperature_control, pH_monitoring, curd_cutting, whey_draining,
    molding_cheese, salting_process, aging_setup, quality_check, packaging_prep,
    label_design, distribution_plan, retail_delivery, customer_feedback
])

# Define the dependencies between the activities
root.order.add_edge(milk_sourcing, culture_selection)
root.order.add_edge(culture_selection, milk_testing)
root.order.add_edge(milk_testing, fermentation_start)
root.order.add_edge(fermentation_start, temperature_control)
root.order.add_edge(temperature_control, pH_monitoring)
root.order.add_edge(pH_monitoring, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, molding_cheese)
root.order.add_edge(molding_cheese, salting_process)
root.order.add_edge(salting_process, aging_setup)
root.order.add_edge(aging_setup, quality_check)
root.order.add_edge(quality_check, packaging_prep)
root.order.add_edge(packaging_prep, label_design)
root.order.add_edge(label_design, distribution_plan)
root.order.add_edge(distribution_plan, retail_delivery)
root.order.add_edge(retail_delivery, customer_feedback)

# Print the root node to verify the model
print(root)