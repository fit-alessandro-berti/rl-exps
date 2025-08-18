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

# Define the loops and XORs in the POWL model
fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[pH_monitoring, curd_cutting, whey_draining, molding_cheese, salting_process])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, quality_check])
distribution_xor = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, customer_feedback])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[milk_sourcing, culture_selection, milk_testing, fermentation_loop, temperature_control, pH_monitoring, curd_cutting, whey_draining, molding_cheese, salting_process, aging_loop, quality_check, packaging_prep, label_design, distribution_xor, distribution_plan])
root.order.add_edge(milk_sourcing, culture_selection)
root.order.add_edge(culture_selection, milk_testing)
root.order.add_edge(milk_testing, fermentation_loop)
root.order.add_edge(fermentation_loop, temperature_control)
root.order.add_edge(temperature_control, pH_monitoring)
root.order.add_edge(pH_monitoring, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, molding_cheese)
root.order.add_edge(molding_cheese, salting_process)
root.order.add_edge(salting_process, aging_loop)
root.order.add_edge(aging_loop, quality_check)
root.order.add_edge(quality_check, packaging_prep)
root.order.add_edge(packaging_prep, label_design)
root.order.add_edge(label_design, distribution_xor)
root.order.add_edge(distribution_xor, distribution_plan)