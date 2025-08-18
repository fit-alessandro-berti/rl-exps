from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
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

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, quality_testing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[press_cheese, salt_application])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[controlled_aging, sensory_check])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[batch_packaging, label_printing])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, logistics_plan])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, feedback_review])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, provenance_track])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[milk_sourcing, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(milk_sourcing, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)