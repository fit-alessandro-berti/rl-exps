import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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
root = StrictPartialOrder(
    nodes=[
        milk_sourcing, curd_preparation, starter_culture, temperature_control, pressing_cheese,
        salting_stage, aging_process, microbial_test, quality_check, eco_packaging, label_printing,
        inventory_audit, order_processing, retail_shipping, customer_feedback, recipe_update,
        market_analysis
    ],
    order=[
        (milk_sourcing, curd_preparation),
        (curd_preparation, starter_culture),
        (starter_culture, temperature_control),
        (temperature_control, pressing_cheese),
        (pressing_cheese, salting_stage),
        (salting_stage, aging_process),
        (aging_process, microbial_test),
        (microbial_test, quality_check),
        (quality_check, eco_packaging),
        (eco_packaging, label_printing),
        (label_printing, inventory_audit),
        (inventory_audit, order_processing),
        (order_processing, retail_shipping),
        (retail_shipping, customer_feedback),
        (customer_feedback, recipe_update),
        (recipe_update, market_analysis)
    ]
)