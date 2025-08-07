import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_culture = Transition(label='Starter Culture')
milk_past = Transition(label='Milk Pasteurize')
curd_cut = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Draining')
press_cheese = Transition(label='Pressing Cheese')
salting_stage = Transition(label='Salting Stage')
fermentation = Transition(label='Fermentation')
aging_control = Transition(label='Aging Control')
flavor_tasting = Transition(label='Flavor Tasting')
packaging_artisanal = Transition(label='Packaging Artisanal')
label_printing = Transition(label='Label Printing')
order_processing = Transition(label='Order Processing')
direct_delivery = Transition(label='Direct Delivery')
customer_feedback = Transition(label='Customer Feedback')

# Define the loop for seasonal adjustments
# The loop will be executed after quality testing and starter culture,
# repeating until exit or an adjustment is made
loop_adjust = OperatorPOWL(
    operator=Operator.LOOP,
    children=[quality_testing, starter_culture]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    loop_adjust,
    milk_past,
    curd_cut,
    whey_drain,
    press_cheese,
    salting_stage,
    fermentation,
    aging_control,
    flavor_tasting,
    packaging_artisanal,
    label_printing,
    order_processing,
    direct_delivery,
    customer_feedback
])

# Add sequential edges
root.order.add_edge(milk_sourcing, loop_adjust)
root.order.add_edge(loop_adjust, milk_past)
root.order.add_edge(milk_past, curd_cut)
root.order.add_edge(curd_cut, whey_drain)
root.order.add_edge(whey_drain, press_cheese)
root.order.add_edge(press_cheese, salting_stage)
root.order.add_edge(salting_stage, fermentation)
root.order.add_edge(fermentation, aging_control)
root.order.add_edge(aging_control, flavor_tasting)
root.order.add_edge(flavor_tasting, packaging_artisanal)
root.order.add_edge(packaging_artisanal, label_printing)
root.order.add_edge(label_printing, order_processing)
root.order.add_edge(order_processing, direct_delivery)
root.order.add_edge(direct_delivery, customer_feedback)

# Print the root model (optional)
print(root)