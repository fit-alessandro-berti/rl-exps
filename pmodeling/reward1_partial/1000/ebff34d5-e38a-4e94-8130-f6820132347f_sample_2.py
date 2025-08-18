import pm4py
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

# Define the process structure
milk_flow = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
fermentation_stage = OperatorPOWL(operator=Operator.XOR, children=[starter_culture, milk_pasteurize])
curd_draining = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_draining])
pressing = OperatorPOWL(operator=Operator.XOR, children=[pressing_cheese, salting_stage])
aging = OperatorPOWL(operator=Operator.XOR, children=[fermentation, aging_control])
tasting = OperatorPOWL(operator=Operator.XOR, children=[flavor_tasting, packaging_artisanal])
labeling = OperatorPOWL(operator=Operator.XOR, children=[label_printing, order_processing])
delivery = OperatorPOWL(operator=Operator.XOR, children=[direct_delivery, customer_feedback])

# Define the partial order
root = StrictPartialOrder(nodes=[milk_flow, fermentation_stage, curd_draining, pressing, aging, tasting, labeling, delivery])
root.order.add_edge(milk_flow, fermentation_stage)
root.order.add_edge(fermentation_stage, curd_draining)
root.order.add_edge(curd_draining, pressing)
root.order.add_edge(pressing, aging)
root.order.add_edge(aging, tasting)
root.order.add_edge(tasting, labeling)
root.order.add_edge(labeling, delivery)

print(root)