import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
culture_prep = Transition(label='Culture Prep')
milk_pasteurize = Transition(label='Milk Pasteurize')
milk_inoculate = Transition(label='Milk Inoculate')
curd_formation = Transition(label='Curd Formation')
curd_cut = Transition(label='Curd Cut')
whey_drain = Transition(label='Whey Drain')
mold_inoculate = Transition(label='Mold Inoculate')
press_cheese = Transition(label='Press Cheese')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
temperature_monitor = Transition(label='Temperature Monitor')
quality_test = Transition(label='Quality Test')
packaging = Transition(label='Packaging')
order_fulfill = Transition(label='Order Fulfill')
retail_deliver = Transition(label='Retail Deliver')
feedback_collect = Transition(label='Feedback Collect')

# Define a silent transition
skip = SilentTransition()

# Define a loop node for aging setup
loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, temperature_monitor, humidity_control, quality_test, packaging])

# Define an exclusive choice for quality test and packaging
xor = OperatorPOWL(operator=Operator.XOR, children=[quality_test, packaging])

# Define the root node of the POWL model
root = StrictPartialOrder(nodes=[milk_sourcing, culture_prep, milk_pasteurize, milk_inoculate, curd_formation, curd_cut, whey_drain, mold_inoculate, press_cheese, loop, xor, order_fulfill, retail_deliver, feedback_collect])
root.order.add_edge(milk_sourcing, culture_prep)
root.order.add_edge(culture_prep, milk_pasteurize)
root.order.add_edge(milk_pasteurize, milk_inoculate)
root.order.add_edge(milk_inoculate, curd_formation)
root.order.add_edge(curd_formation, curd_cut)
root.order.add_edge(curd_cut, whey_drain)
root.order.add_edge(whey_drain, mold_inoculate)
root.order.add_edge(mold_inoculate, press_cheese)
root.order.add_edge(press_cheese, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, order_fulfill)
root.order.add_edge(order_fulfill, retail_deliver)
root.order.add_edge(retail_deliver, feedback_collect)