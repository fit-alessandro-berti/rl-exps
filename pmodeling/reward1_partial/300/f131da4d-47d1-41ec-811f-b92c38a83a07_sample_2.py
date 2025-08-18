from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop for fermentation and aging
fermentation_aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    fermentation_start,
    temperature_control,
    pH_monitoring,
    curd_cutting,
    whey_draining,
    molding_cheese,
    salting_process,
    aging_setup
])

# Define the exclusive choice for quality check and packaging prep
quality_check_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[
    quality_check,
    packaging_prep
])

# Define the partial order with the loop and exclusive choice
root = StrictPartialOrder(nodes=[
    fermentation_aging_loop,
    quality_check_packaging_choice
])
root.order.add_edge(fermentation_aging_loop, quality_check_packaging_choice)

print(root)