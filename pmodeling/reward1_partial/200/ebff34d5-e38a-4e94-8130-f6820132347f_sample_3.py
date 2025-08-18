from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Define the process tree
milk_process = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
fermentation_process = OperatorPOWL(operator=Operator.XOR, children=[starter_culture, milk_pasteurize])
aging_process = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_draining])
packaging_process = OperatorPOWL(operator=Operator.XOR, children=[pressing_cheese, salting_stage])
tasting_process = OperatorPOWL(operator=Operator.XOR, children=[fermentation, aging_control])
label_printing_process = OperatorPOWL(operator=Operator.XOR, children=[packaging_artisanal, label_printing])
order_processing_process = OperatorPOWL(operator=Operator.XOR, children=[tasting_process, label_printing_process])
delivery_process = OperatorPOWL(operator=Operator.XOR, children=[order_processing, direct_delivery])
feedback_process = OperatorPOWL(operator=Operator.XOR, children=[delivery_process, customer_feedback])

# Define the partial order
root = StrictPartialOrder(nodes=[milk_process, fermentation_process, aging_process, packaging_process, tasting_process, label_printing_process, order_processing_process, delivery_process, feedback_process])
root.order.add_edge(milk_process, fermentation_process)
root.order.add_edge(fermentation_process, aging_process)
root.order.add_edge(aging_process, packaging_process)
root.order.add_edge(packaging_process, tasting_process)
root.order.add_edge(tasting_process, label_printing_process)
root.order.add_edge(label_printing_process, order_processing_process)
root.order.add_edge(order_processing_process, delivery_process)
root.order.add_edge(delivery_process, feedback_process)

print(root)