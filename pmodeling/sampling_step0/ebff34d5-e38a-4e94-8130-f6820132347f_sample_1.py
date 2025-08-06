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

# Define the transitions
quality_check = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, starter_culture, milk_pasteurize, curd_cutting, whey_draining, pressing_cheese, salting_stage, fermentation, aging_control, flavor_tasting])
packaging = OperatorPOWL(operator=Operator.XOR, children=[packaging_artisanal, label_printing])
order = OperatorPOWL(operator=Operator.XOR, children=[order_processing, direct_delivery])
customer_engagement = OperatorPOWL(operator=Operator.XOR, children=[order, customer_feedback])

# Define the root
root = StrictPartialOrder(nodes=[quality_check, packaging, order, customer_engagement])
root.order.add_edge(quality_check, packaging)
root.order.add_edge(quality_check, order)
root.order.add_edge(packaging, customer_engagement)
root.order.add_edge(order, customer_engagement)

# Print the root
print(root)