import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL transitions
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

# Define the POWL operators
choice = OperatorPOWL(operator=Operator.XOR)
loop = OperatorPOWL(operator=Operator.LOOP)

# Construct the POWL model
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    starter_culture,
    milk_pasteurize,
    curd_cutting,
    whey_draining,
    pressing_cheese,
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

# Define the dependencies (edges)
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_culture)
root.order.add_edge(starter_culture, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, pressing_cheese)
root.order.add_edge(pressing_cheese, salting_stage)
root.order.add_edge(salting_stage, fermentation)
root.order.add_edge(fermentation, aging_control)
root.order.add_edge(aging_control, flavor_tasting)
root.order.add_edge(flavor_tasting, packaging_artisanal)
root.order.add_edge(packaging_artisanal, label_printing)
root.order.add_edge(label_printing, order_processing)
root.order.add_edge(order_processing, direct_delivery)
root.order.add_edge(direct_delivery, customer_feedback)

print(root)