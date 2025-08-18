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

# Define the loop nodes for milk testing and pH monitoring
milk_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_testing])
pH_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[pH_monitoring])

# Define the exclusive choice for curd cutting and whey draining
curd_cutting_draining_choice = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_draining])

# Define the exclusive choice for molding cheese and salting process
molding_salting_choice = OperatorPOWL(operator=Operator.XOR, children=[molding_cheese, salting_process])

# Define the exclusive choice for aging setup and quality check
aging_quality_check_choice = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, quality_check])

# Define the exclusive choice for packaging prep and label design
packaging_label_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, label_design])

# Define the exclusive choice for distribution plan and retail delivery
distribution_retail_choice = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, retail_delivery])

# Define the exclusive choice for retail delivery and customer feedback
retail_feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, customer_feedback])

# Define the root node
root = StrictPartialOrder(nodes=[
    milk_sourcing, culture_selection, milk_test_loop, pH_monitoring_loop, curd_cutting_draining_choice,
    molding_salting_choice, aging_quality_check_choice, packaging_label_choice, distribution_retail_choice,
    retail_feedback_choice
])

# Define the dependencies between nodes
root.order.add_edge(milk_sourcing, culture_selection)
root.order.add_edge(culture_selection, milk_test_loop)
root.order.add_edge(milk_test_loop, pH_monitoring_loop)
root.order.add_edge(pH_monitoring_loop, curd_cutting_draining_choice)
root.order.add_edge(curd_cutting_draining_choice, molding_salting_choice)
root.order.add_edge(molding_salting_choice, aging_quality_check_choice)
root.order.add_edge(aging_quality_check_choice, packaging_label_choice)
root.order.add_edge(packaging_label_choice, distribution_retail_choice)
root.order.add_edge(distribution_retail_choice, retail_feedback_choice)

# Print the root node
print(root)