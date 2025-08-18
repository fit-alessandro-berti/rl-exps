import pm4py
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

# Define the process structure
loop_fermentation = OperatorPOWL(operator=Operator.LOOP, children=[
    milk_testing,
    culture_selection,
    fermentation_start,
    temperature_control,
    pH_monitoring,
    curd_cutting,
    whey_draining,
    molding_cheese,
    salting_process
])
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[
    aging_setup,
    quality_check,
    packaging_prep,
    label_design
])
xor_distribution = OperatorPOWL(operator=Operator.XOR, children=[
    distribution_plan,
    retail_delivery
])
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[
    customer_feedback
])
root = StrictPartialOrder(nodes=[
    loop_fermentation,
    loop_aging,
    xor_distribution,
    xor_feedback
])
root.order.add_edge(loop_fermentation, loop_aging)
root.order.add_edge(loop_aging, xor_distribution)
root.order.add_edge(xor_distribution, xor_feedback)

# Save the result in the variable 'root'
root