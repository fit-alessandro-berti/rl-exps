import pm4py
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

# Define silent transitions
skip = SilentTransition()

# Define loop and choice nodes
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[fermentation_start, pH_monitoring, curd_cutting, whey_draining, molding_cheese, salting_process, aging_setup])
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_check])
distribution_choice = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, retail_delivery])
retail_loop = OperatorPOWL(operator=Operator.LOOP, children=[retail_delivery])
customer_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback])

# Define root node
root = StrictPartialOrder(nodes=[milk_sourcing, culture_selection, milk_testing, fermentation_loop, quality_loop, distribution_choice, retail_loop, customer_loop])
root.order.add_edge(milk_sourcing, culture_selection)
root.order.add_edge(culture_selection, milk_testing)
root.order.add_edge(milk_testing, fermentation_loop)
root.order.add_edge(fermentation_loop, quality_loop)
root.order.add_edge(quality_loop, distribution_choice)
root.order.add_edge(distribution_choice, retail_loop)
root.order.add_edge(retail_loop, customer_loop)