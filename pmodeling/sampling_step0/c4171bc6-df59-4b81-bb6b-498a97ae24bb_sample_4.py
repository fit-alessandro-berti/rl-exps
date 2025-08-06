import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasturize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
press_cheese = Transition(label='Press Cheese')
salt_application = Transition(label='Salt Application')
controlled_aging = Transition(label='Controlled Aging')
sensory_check = Transition(label='Sensory Check')
batch_packaging = Transition(label='Batch Packaging')
label_printing = Transition(label='Label Printing')
cold_storage = Transition(label='Cold Storage')
logistics_plan = Transition(label='Logistics Plan')
retail_delivery = Transition(label='Retail Delivery')
feedback_review = Transition(label='Feedback Review')
demand_forecast = Transition(label='Demand Forecast')
provenance_track = Transition(label='Provenance Track')

# Define the operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_pasturize, quality_testing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[press_cheese, salt_application])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[batch_packaging, label_printing])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, retail_delivery])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, provenance_track])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, provenance_track])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, xor1])

# Define the partial order
root = StrictPartialOrder(nodes=[loop, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)
root.order.add_edge(loop, xor7)
root.order.add_edge(loop, xor8)

# Print the root POWL model
print(root)