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

# Define silent transitions for empty labels
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, curd_preparation])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[starter_culture, temperature_control])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[pressing_cheese, salting_stage])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[aging_process, microbial_test])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, eco_packaging])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[label_printing, inventory_audit])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[order_processing, retail_shipping])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, market_analysis])

# Define the root node with the defined loops and silent transitions
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8, skip])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)
root.order.add_edge(loop8, skip)

print(root)