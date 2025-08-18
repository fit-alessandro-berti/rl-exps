from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the workflow model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, starter_culture])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, xor1])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_draining])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[pressing_cheese, salting_stage])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[fermentation, aging_control])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[flavor_tasting, packaging_artisanal])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[label_printing, order_processing])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[direct_delivery, customer_feedback])
root = StrictPartialOrder(nodes=[milk_sourcing, xor2, xor3, xor4, xor5, xor6, xor7, xor8])

# Define the partial order dependencies
root.order.add_edge(milk_sourcing, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)

# Print the final POWL model
print(root)