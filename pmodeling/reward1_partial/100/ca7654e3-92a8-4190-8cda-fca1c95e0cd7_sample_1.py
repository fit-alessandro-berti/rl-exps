import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the control-flow operators
choice1 = OperatorPOWL(operator=Operator.XOR, children=[microbial_test, quality_check])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[salting_stage, pressing_cheese])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[aging_process, temperature_control])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[curd_preparation, starter_culture])
loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, choice4])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[choice1, choice2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[choice3, eco_packaging])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[label_printing, inventory_audit])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[order_processing, retail_shipping])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, market_analysis])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[recipe_update, market_analysis])

# Define the root
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, loop)

# Print the root model
print(root)