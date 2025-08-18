import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
culture_prep = Transition(label='Culture Prep')
milk_pasturize = Transition(label='Milk Pasteurize')
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

# Define the process structure
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, culture_prep])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, milk_inoculate])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, curd_cut])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[whey_drain, mold_inoculate])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[press_cheese, aging_setup])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[humidity_control, temperature_monitor])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[quality_test, packaging])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[order_fulfill, retail_deliver])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect])

# Define the loop for the aging process
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, loop, xor7, xor8, xor9])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, loop)
root.order.add_edge(loop, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor1)