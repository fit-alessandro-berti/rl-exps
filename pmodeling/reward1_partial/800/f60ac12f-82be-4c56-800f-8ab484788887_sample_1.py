import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

milk_sourcing = Transition(label='Milk Sourcing')
culture_blending = Transition(label='Culture Blending')
milk_pasteurize = Transition(label='Milk Pasteurize')
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

skip = SilentTransition()

# Define the order of activities
loop = OperatorPOWL(operator=Operator.LOOP, children=[culture_blending, milk_pasteurize])
xor = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_drain])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculate, press_cheese])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[salt_brine, age_monitor])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[quality_test, packaging_prep])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[label_design, order_allocation])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[transport_arrange, retail_sync])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[customer_review, feedback_analyze])

root = StrictPartialOrder(nodes=[milk_sourcing, loop, xor, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(milk_sourcing, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)