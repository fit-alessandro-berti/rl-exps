import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the loop and choice
loop = OperatorPOWL(operator=Operator.LOOP, children=[age_monitor, quality_test])
xor = OperatorPOWL(operator=Operator.XOR, children=[order_allocation, transport_arrange])

# Define the root
root = StrictPartialOrder(nodes=[milk_sourcing, culture_blending, milk_pasteurize, curd_cutting, whey_drain, mold_inoculate, press_cheese, salt_brine, loop, packaging_prep, label_design, retail_sync, customer_review, feedback_analyze])
root.order.add_edge(milk_sourcing, culture_blending)
root.order.add_edge(culture_blending, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, mold_inoculate)
root.order.add_edge(mold_inoculate, press_cheese)
root.order.add_edge(press_cheese, salt_brine)
root.order.add_edge(salt_brine, loop)
root.order.add_edge(loop, packaging_prep)
root.order.add_edge(packaging_prep, label_design)
root.order.add_edge(label_design, retail_sync)
root.order.add_edge(retail_sync, customer_review)
root.order.add_edge(customer_review, feedback_analyze)