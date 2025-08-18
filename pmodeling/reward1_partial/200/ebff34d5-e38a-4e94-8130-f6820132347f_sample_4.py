from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_culture = Transition(label='Starter Culture')
milk_pasturize = Transition(label='Milk Pasteurize')
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

# Define the process structure
milk_sourcing_and_quality_testing = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
starter_culture_and_milk_pasturize = OperatorPOWL(operator=Operator.XOR, children=[starter_culture, milk_pasturize])
curd_cutting_and_whey_draining = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_draining])
pressing_cheese_and_salting_stage = OperatorPOWL(operator=Operator.XOR, children=[pressing_cheese, salting_stage])
fermentation_and_aging_control = OperatorPOWL(operator=Operator.XOR, children=[fermentation, aging_control])
flavor_tasting_and_label_printing = OperatorPOWL(operator=Operator.XOR, children=[flavor_tasting, label_printing])
order_processing_and_direct_delivery = OperatorPOWL(operator=Operator.XOR, children=[order_processing, direct_delivery])
customer_feedback_and_package = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, packaging_artisanal])

# Define the loop for the process
loop = OperatorPOWL(operator=Operator.LOOP, children=[starter_culture_and_milk_pasturize, curd_cutting_and_whey_draining, pressing_cheese_and_salting_stage, fermentation_and_aging_control, flavor_tasting_and_label_printing, order_processing_and_direct_delivery, customer_feedback_and_package])
loop.order.add_edge(loop, starter_culture_and_milk_pasturize)

# Define the root of the process
root = StrictPartialOrder(nodes=[loop, customer_feedback_and_package])
root.order.add_edge(loop, customer_feedback_and_package)

print(root)