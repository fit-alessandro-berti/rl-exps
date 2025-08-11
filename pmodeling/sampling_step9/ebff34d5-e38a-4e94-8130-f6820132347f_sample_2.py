import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for fermentation stages
xor_fermentation = OperatorPOWL(operator=Operator.XOR, children=[fermentation, skip])

# Define loop for aging stages
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, flavor_tasting])

# Define exclusive choice for packaging stages
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[packaging_artisanal, label_printing])

# Define loop for order processing stages
loop_order = OperatorPOWL(operator=Operator.LOOP, children=[order_processing, direct_delivery])

# Define loop for customer feedback stages
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback])

# Define root process
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, starter_culture, milk_pasturize, curd_cutting, whey_draining, pressing_cheese, salting_stage, xor_fermentation, loop_aging, xor_packaging, loop_order, loop_feedback])

# Define dependencies
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_culture)
root.order.add_edge(starter_culture, milk_pasturize)
root.order.add_edge(milk_pasturize, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, pressing_cheese)
root.order.add_edge(pressing_cheese, salting_stage)
root.order.add_edge(salting_stage, xor_fermentation)
root.order.add_edge(xor_fermentation, loop_aging)
root.order.add_edge(loop_aging, xor_packaging)
root.order.add_edge(xor_packaging, loop_order)
root.order.add_edge(loop_order, loop_feedback)
root.order.add_edge(loop_feedback, loop_order)