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

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define the loop for aging
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, quality_check])

# Define the XOR for packaging and distribution
packaging_distribution_xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])

# Define the loop for distribution and retail delivery
distribution_loop = OperatorPOWL(operator=Operator.LOOP, children=[distribution_plan, retail_delivery])

# Define the XOR for retail delivery and customer feedback
retail_feedback_xor = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, customer_feedback])

# Define the final POWL model
root = StrictPartialOrder(nodes=[aging_loop, packaging_distribution_xor, distribution_loop, retail_feedback_xor])

# Define the order between nodes
root.order.add_edge(aging_loop, packaging_distribution_xor)
root.order.add_edge(packaging_distribution_xor, distribution_loop)
root.order.add_edge(distribution_loop, retail_feedback_xor)

# Print the final POWL model
print(root)