from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
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

# Define control flow operators
loop_fermentation = OperatorPOWL(operator=Operator.LOOP, children=[fermentation, aging_control, flavor_tasting])
xor_milk_sources = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing, starter_culture, milk_pasturize, curd_cutting, whey_draining, pressing_cheese, salting_stage])
xor_order_processing = OperatorPOWL(operator=Operator.XOR, children=[packaging_artisanal, label_printing, order_processing, direct_delivery, customer_feedback])

# Define the root node
root = StrictPartialOrder(nodes=[loop_fermentation, xor_milk_sources, xor_order_processing])
root.order.add_edge(loop_fermentation, xor_milk_sources)
root.order.add_edge(xor_milk_sources, xor_order_processing)

# Save the final result in the variable 'root'