from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (if any)
skip = SilentTransition()

# Define the loop for fermentation process
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_start, temperature_control, pH_monitoring, curd_cutting, whey_draining])

# Define the exclusive choice for quality assurance
quality_assurance = OperatorPOWL(operator=Operator.XOR, children=[quality_check, salting_process])

# Define the exclusive choice for packaging
packaging = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, label_design])

# Define the exclusive choice for distribution plan
distribution = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, retail_delivery])

# Define the exclusive choice for retail delivery
retail_delivery_choice = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, customer_feedback])

# Construct the root POWL model
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_selection,
    milk_testing,
    fermentation_loop,
    quality_assurance,
    packaging,
    distribution,
    retail_delivery_choice
])

# Add edges to represent the partial order
root.order.add_edge(milk_sourcing, culture_selection)
root.order.add_edge(culture_selection, milk_testing)
root.order.add_edge(milk_testing, fermentation_loop)
root.order.add_edge(fermentation_loop, quality_assurance)
root.order.add_edge(quality_assurance, packaging)
root.order.add_edge(packaging, distribution)
root.order.add_edge(distribution, retail_delivery_choice)
root.order.add_edge(retail_delivery_choice, retail_delivery)
root.order.add_edge(retail_delivery_choice, customer_feedback)

print(root)