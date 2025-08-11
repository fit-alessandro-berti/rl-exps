from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) with their labels
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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[curd_preparation, starter_culture, temperature_control, pressing_cheese, salting_stage, aging_process, microbial_test, quality_check, eco_packaging, label_printing, inventory_audit])
xor = OperatorPOWL(operator=Operator.XOR, children=[retail_shipping, customer_feedback])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[order_processing, market_analysis])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[recipe_update, market_analysis])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, customer_feedback])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, retail_shipping])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, order_processing])

root = StrictPartialOrder(nodes=[loop, xor, xor_2, xor_3, xor_4, xor_5, xor_6])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor_2)
root.order.add_edge(loop, xor_3)
root.order.add_edge(loop, xor_4)
root.order.add_edge(loop, xor_5)
root.order.add_edge(loop, xor_6)

print(root)