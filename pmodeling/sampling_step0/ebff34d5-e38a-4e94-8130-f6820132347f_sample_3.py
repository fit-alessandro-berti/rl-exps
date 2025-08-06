import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_culture = Transition(label='Starter Culture')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
pressing_cheese = Transition(label='Pressing Cheese')
salting_stage = Transition(label='Salting Stage')
fermentation = Transition(label='Fermentation')
aging_control = Transition(label='Aging Control')
flavor_tasting = Transition(label='Flavor Tasting')
packaging_artisanal = Transition(label='Packaging Artisanal')
label_printing = Transition(label='Label Printing')
order_processing = Transition(label='Order Processing')
direct_delivery = Transition(label='Direct Delivery')
customer_feedback = Transition(label='Customer Feedback')

# Define the silent transitions
skip = SilentTransition()

# Define the loop and XOR nodes
loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, salting_stage])
xor = OperatorPOWL(operator=Operator.XOR, children=[fermentation, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, starter_culture])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_draining])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[pressing_cheese, flavor_tasting])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[packaging_artisanal, label_printing])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[order_processing, direct_delivery])

# Define the partial order
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, xor2, xor3, xor4, xor5, xor6, loop, xor])

# Add edges
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, loop)
root.order.add_edge(loop, xor)

print(root)