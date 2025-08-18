from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the process model
loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_pasteurize, quality_testing])
xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, whey_separation])
batch_loop = OperatorPOWL(operator=Operator.LOOP, children=[press_cheese, salt_application])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[controlled_aging, sensory_check])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_packaging, label_printing])
storage_loop = OperatorPOWL(operator=Operator.LOOP, children=[cold_storage, logistics_plan])
delivery_loop = OperatorPOWL(operator=Operator.LOOP, children=[retail_delivery, feedback_review])
demand_loop = OperatorPOWL(operator=Operator.LOOP, children=[demand_forecast, provenance_track])

# Create the root process model
root = StrictPartialOrder(nodes=[milk_sourcing, loop, xor, batch_loop, aging_loop, packaging_loop, storage_loop, delivery_loop, demand_loop])
root.order.add_edge(milk_sourcing, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, batch_loop)
root.order.add_edge(batch_loop, aging_loop)
root.order.add_edge(aging_loop, packaging_loop)
root.order.add_edge(packaging_loop, storage_loop)
root.order.add_edge(storage_loop, delivery_loop)
root.order.add_edge(delivery_loop, demand_loop)