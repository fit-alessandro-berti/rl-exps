import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the loop for the fermentation and aging process
fermentation_aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[fermentation, aging_control])

# Define the exclusive choice for flavor tasting and packaging
flavor_tasting_packaging = OperatorPOWL(operator=Operator.XOR, children=[flavor_tasting, packaging_artisanal])

# Define the root process with the defined transitions and loops
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    starter_culture,
    milk_pasturize,
    curd_cutting,
    whey_draining,
    pressing_cheese,
    salting_stage,
    fermentation_aging_loop,
    flavor_tasting_packaging,
    order_processing,
    direct_delivery,
    customer_feedback
])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_culture)
root.order.add_edge(starter_culture, milk_pasturize)
root.order.add_edge(milk_pasturize, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, pressing_cheese)
root.order.add_edge(pressing_cheese, salting_stage)
root.order.add_edge(salting_stage, fermentation_aging_loop)
root.order.add_edge(fermentation_aging_loop, flavor_tasting_packaging)
root.order.add_edge(flavor_tasting_packaging, order_processing)
root.order.add_edge(order_processing, direct_delivery)
root.order.add_edge(direct_delivery, customer_feedback)