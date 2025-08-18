import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
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

# Define exclusive choices
exclusive_choice_1 = OperatorPOWL(operator=OperatorPOWL.XOR, children=[milk_sourcing, quality_testing])
exclusive_choice_2 = OperatorPOWL(operator=OperatorPOWL.XOR, children=[starter_culture, milk_pasteurize])
exclusive_choice_3 = OperatorPOWL(operator=OperatorPOWL.XOR, children=[curd_cutting, whey_draining])
exclusive_choice_4 = OperatorPOWL(operator=OperatorPOWL.XOR, children=[pressing_cheese, salting_stage])
exclusive_choice_5 = OperatorPOWL(operator=OperatorPOWL.XOR, children=[fermentation, aging_control])
exclusive_choice_6 = OperatorPOWL(operator=OperatorPOWL.XOR, children=[flavor_tasting, packaging_artisanal])
exclusive_choice_7 = OperatorPOWL(operator=OperatorPOWL.XOR, children=[label_printing, order_processing])
exclusive_choice_8 = OperatorPOWL(operator=OperatorPOWL.XOR, children=[direct_delivery, customer_feedback])

# Define loops
loop_1 = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[exclusive_choice_1])
loop_2 = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[exclusive_choice_2])
loop_3 = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[exclusive_choice_3])
loop_4 = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[exclusive_choice_4])
loop_5 = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[exclusive_choice_5])
loop_6 = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[exclusive_choice_6])
loop_7 = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[exclusive_choice_7])
loop_8 = OperatorPOWL(operator=OperatorPOWL.LOOP, children=[exclusive_choice_8])

# Construct the root partial order
root = StrictPartialOrder(
    nodes=[
        loop_1,
        exclusive_choice_2,
        exclusive_choice_3,
        exclusive_choice_4,
        exclusive_choice_5,
        exclusive_choice_6,
        exclusive_choice_7,
        exclusive_choice_8
    ]
)

# Add edges to form the partial order
root.order.add_edge(loop_1, exclusive_choice_2)
root.order.add_edge(exclusive_choice_2, exclusive_choice_3)
root.order.add_edge(exclusive_choice_3, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, exclusive_choice_7)
root.order.add_edge(exclusive_choice_7, exclusive_choice_8)
root.order.add_edge(exclusive_choice_8, loop_2)
root.order.add_edge(loop_2, exclusive_choice_3)
root.order.add_edge(exclusive_choice_3, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, exclusive_choice_7)
root.order.add_edge(exclusive_choice_7, exclusive_choice_8)
root.order.add_edge(exclusive_choice_8, loop_3)
root.order.add_edge(loop_3, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, exclusive_choice_7)
root.order.add_edge(exclusive_choice_7, exclusive_choice_8)
root.order.add_edge(exclusive_choice_8, loop_4)
root.order.add_edge(loop_4, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, exclusive_choice_7)
root.order.add_edge(exclusive_choice_7, exclusive_choice_8)
root.order.add_edge(exclusive_choice_8, loop_5)
root.order.add_edge(loop_5, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, exclusive_choice_7)
root.order.add_edge(exclusive_choice_7, exclusive_choice_8)
root.order.add_edge(exclusive_choice_8, loop_6)
root.order.add_edge(loop_6, exclusive_choice_7)
root.order.add_edge(exclusive_choice_7, exclusive_choice_8)
root.order.add_edge(exclusive_choice_8, loop_7)
root.order.add_edge(loop_7, exclusive_choice_8)
root.order.add_edge(exclusive_choice_8, loop_8)

print("POWL model defined successfully.")