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

# Define the root of the POWL model
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

# Define the dependencies between activities (if any)
# For example, assuming the order of activities is Milk Sourcing -> Curd Preparation -> ...
# You would define the dependencies as follows:
# root.order.add_edge(milk_sourcing, curd_preparation)
# root.order.add_edge(curd_preparation, starter_culture)
# ...
# Add all necessary dependencies here

# The final POWL model is stored in the 'root' variable
print(root)