import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
curd_preparation = Transition(label='Curd Preparation')
starter_culture = Transition(label='starter Culture')
temperature_control = Transition(label='Temperature Control')
pressing_cheese = Transition(label='Pressing Cheese')
salting_stage = Transition(label='Salting Stage')
aging_process = Transition(label='Aging Process')
microbial_test = Transition(label='Microbial Test')
quality_check = Transition(label='Quality Check')
eco_packaging = Transition(label='Eco Packaging')
label_printing = Transition(label='Label Printing')
inventory_audit = Transition(label='Inventory Audit')
order_processing = Transition(label='Order Processing')
retail_shipping = Transition(label='Retail Shipping')
customer_feedback = Transition(label='Customer Feedback')
recipe_update = Transition(label='Recipe Update')
market_analysis = Transition(label='Market Analysis')

# Define silent transitions for no-operation
skip = SilentTransition()

# Define loops and choices
sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing])
preparation_loop = OperatorPOWL(operator=Operator.LOOP, children=[curd_preparation, starter_culture, temperature_control, pressing_cheese, salting_stage, aging_process])
test_loop = OperatorPOWL(operator=Operator.LOOP, children=[microbial_test, quality_check])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[eco_packaging, label_printing])
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_audit])
order_loop = OperatorPOWL(operator=Operator.LOOP, children=[order_processing, retail_shipping, customer_feedback])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[recipe_update, market_analysis])

# Define root POWL model
root = StrictPartialOrder(nodes=[sourcing_loop, preparation_loop, test_loop, packaging_loop, audit_loop, order_loop, feedback_loop])
root.order.add_edge(sourcing_loop, preparation_loop)
root.order.add_edge(preparation_loop, test_loop)
root.order.add_edge(test_loop, packaging_loop)
root.order.add_edge(packaging_loop, audit_loop)
root.order.add_edge(audit_loop, order_loop)
root.order.add_edge(order_loop, feedback_loop)

print(root)