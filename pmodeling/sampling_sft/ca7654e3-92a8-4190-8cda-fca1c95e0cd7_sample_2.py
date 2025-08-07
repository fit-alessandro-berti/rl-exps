import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as transitions
milk_sourcing      = Transition(label='Milk Sourcing')
curd_preparation   = Transition(label='Curd Preparation')
starter_culture    = Transition(label='starter Culture')
temperature_control= Transition(label='Temperature Control')
pressing_cheese    = Transition(label='Pressing Cheese')
salting_stage      = Transition(label='Salting Stage')
aging_process      = Transition(label='Aging Process')
microbial_test     = Transition(label='Microbial Test')
quality_check      = Transition(label='Quality Check')
eco_packaging      = Transition(label='Eco Packaging')
label_printing     = Transition(label='Label Printing')
inventory_audit    = Transition(label='Inventory Audit')
order_processing   = Transition(label='Order Processing')
retail_shipping    = Transition(label='Retail Shipping')
customer_feedback  = Transition(label='Customer Feedback')
recipe_update      = Transition(label='Recipe Update')
market_analysis    = Transition(label='Market Analysis')

# Build the partial‐order model
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

# Sequence edges for the main production cycle
root.order.add_edge(milk_sourcing,     curd_preparation)
root.order.add_edge(curd_preparation,  starter_culture)
root.order.add_edge(starter_culture,   temperature_control)
root.order.add_edge(temperature_control, pressing_cheese)
root.order.add_edge(pressing_cheese,   salting_stage)
root.order.add_edge(salting_stage,     aging_process)
root.order.add_edge(aging_process,     microbial_test)
root.order.add_edge(microbial_test,    quality_check)

# Packaging and labeling after quality check
root.order.add_edge(quality_check,     eco_packaging)
root.order.add_edge(quality_check,     label_printing)

# Inventory audit and order processing concurrently after packaging
root.order.add_edge(eco_packaging,     inventory_audit)
root.order.add_edge(label_printing,    inventory_audit)
root.order.add_edge(inventory_audit,   order_processing)

# Retail shipping and customer feedback concurrently after order processing
root.order.add_edge(order_processing,  retail_shipping)
root.order.add_edge(order_processing,  customer_feedback)

# Feedback loop: after customer feedback, either exit or update recipe and market analysis
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, market_analysis])
root.order.add_edge(retail_shipping,   feedback_loop)

# Update recipe and market analysis sequentially
root.order.add_edge(feedback_loop,     recipe_update)
root.order.add_edge(feedback_loop,     market_analysis)

# Final edges to complete the loop
root.order.add_edge(market_analysis,   feedback_loop)