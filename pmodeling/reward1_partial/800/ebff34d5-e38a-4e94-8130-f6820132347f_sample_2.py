import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define operators
xor_quality = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, starter_culture])
xor_pasturize = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, curd_cutting])
xor_drain = OperatorPOWL(operator=Operator.XOR, children=[whey_draining, pressing_cheese])
xor_salt = OperatorPOWL(operator=Operator.XOR, children=[salting_stage, fermentation])
xor_age = OperatorPOWL(operator=Operator.XOR, children=[aging_control, flavor_tasting])
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[packaging_artisanal, label_printing])
xor_order = OperatorPOWL(operator=Operator.XOR, children=[order_processing, direct_delivery])
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, None])  # None represents a silent transition

# Define root
root = StrictPartialOrder(nodes=[
    xor_quality,
    xor_pasturize,
    xor_drain,
    xor_salt,
    xor_age,
    xor_packaging,
    xor_order,
    xor_feedback
])

# Define edges
root.order.add_edge(xor_quality, xor_pasturize)
root.order.add_edge(xor_pasturize, xor_drain)
root.order.add_edge(xor_drain, xor_salt)
root.order.add_edge(xor_salt, xor_age)
root.order.add_edge(xor_age, xor_packaging)
root.order.add_edge(xor_packaging, xor_order)
root.order.add_edge(xor_order, xor_feedback)

# Print the root POWL model
print(root)