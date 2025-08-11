import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define loops and choices
curd_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[curd_preparation, starter_culture, temperature_control, pressing_cheese, salting_stage, aging_process, microbial_test, quality_check])
eco_packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[eco_packaging, label_printing, inventory_audit])
order_processing_loop = OperatorPOWL(operator=Operator.LOOP, children=[order_processing, retail_shipping, customer_feedback])
recipe_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[recipe_update, market_analysis])

# Define root partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    curd_prep_loop,
    eco_packaging_loop,
    order_processing_loop,
    recipe_update_loop
])

# Add edges to define the partial order structure
root.order.add_edge(milk_sourcing, curd_prep_loop)
root.order.add_edge(milk_sourcing, eco_packaging_loop)
root.order.add_edge(milk_sourcing, order_processing_loop)
root.order.add_edge(milk_sourcing, recipe_update_loop)

print(root)