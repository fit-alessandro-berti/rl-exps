import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    curd_preparation,
    starter_culture,
    temperature_control,
    pressing_cheese,
    salting_stage,
    aging_process,
    microbial_test,
    quality_check,
    eco_packaging,
    label_printing,
    inventory_audit,
    order_processing,
    retail_shipping,
    customer_feedback,
    recipe_update,
    market_analysis
])

# Add dependencies as per the process description
root.order.add_edge(milk_sourcing, curd_preparation)
root.order.add_edge(milk_sourcing, starter_culture)
root.order.add_edge(milk_sourcing, temperature_control)
root.order.add_edge(milk_sourcing, pressing_cheese)
root.order.add_edge(milk_sourcing, salting_stage)
root.order.add_edge(milk_sourcing, aging_process)
root.order.add_edge(milk_sourcing, microbial_test)
root.order.add_edge(milk_sourcing, quality_check)
root.order.add_edge(milk_sourcing, eco_packaging)
root.order.add_edge(milk_sourcing, label_printing)
root.order.add_edge(milk_sourcing, inventory_audit)
root.order.add_edge(milk_sourcing, order_processing)
root.order.add_edge(milk_sourcing, retail_shipping)
root.order.add_edge(milk_sourcing, customer_feedback)
root.order.add_edge(milk_sourcing, recipe_update)
root.order.add_edge(milk_sourcing, market_analysis)

# Save the root of the POWL model
print(root)