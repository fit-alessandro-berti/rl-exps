from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions (activities) with exact names
milk_sourcing = Transition(label='Milk Sourcing')
culture_blending = Transition(label='Culture Blending')
milk_pasturize = Transition(label='Milk Pasteurize')
curd_cutting = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Drain')
mold_inoculate = Transition(label='Mold Inoculate')
press_cheese = Transition(label='Press Cheese')
salt_brine = Transition(label='Salt Brine')
age_monitor = Transition(label='Age Monitor')
quality_test = Transition(label='Quality Test')
packaging_prep = Transition(label='Packaging Prep')
label_design = Transition(label='Label Design')
order_allocation = Transition(label='Order Allocation')
transport_arrange = Transition(label='Transport Arrange')
retail_sync = Transition(label='Retail Sync')
customer_review = Transition(label='Customer Review')
feedback_analyze = Transition(label='Feedback Analyze')

# Define silent transitions
skip = SilentTransition()

# Define partial order structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, culture_blending])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_drain])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculate, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[press_cheese, salt_brine])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[age_monitor, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[quality_test, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, label_design])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[order_allocation, transport_arrange])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[retail_sync, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[customer_review, feedback_analyze])

# Construct the root node
root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)
root.order.add_edge(loop, xor7)
root.order.add_edge(loop, xor8)
root.order.add_edge(loop, xor9)
root.order.add_edge(loop, xor10)