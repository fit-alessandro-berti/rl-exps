import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk = Transition(label='Milk Sourcing')
quality = Transition(label='Quality Testing')
starter = Transition(label='Starter Prep')
curd = Transition(label='Curd Cutting')
molding = Transition(label='Molding Cheese')
salting = Transition(label='Salting Process')
aging = Transition(label='Aging Control')
humidity = Transition(label='Humidity Check')
packaging = Transition(label='Packaging Design')
label_print = Transition(label='Label Printing')
cold_storage = Transition(label='Cold Storage')
order_proc = Transition(label='Order Processing')
logistics = Transition(label='Logistics Planning')
delivery = Transition(label='Retail Delivery')
feedback = Transition(label='Consumer Feedback')
batch_adj = Transition(label='Batch Adjustment')
event_coord = Transition(label='Event Coordination')
inventory = Transition(label='Inventory Audit')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for adaptive inventory management
# After each batch, do Inventory Audit, then either exit or adjust batch and repeat
inventory_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory, skip])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    milk, quality, starter, curd, molding, salting,
    aging, humidity, packaging, label_print, cold_storage,
    order_proc, logistics, delivery, feedback, batch_adj, event_coord,
    inventory_loop
])

# Add dependencies
root.order.add_edge(milk, quality)
root.order.add_edge(quality, starter)
root.order.add_edge(starter, curd)
root.order.add_edge(curd, molding)
root.order.add_edge(molding, salting)
root.order.add_edge(salting, aging)
root.order.add_edge(aging, humidity)
root.order.add_edge(humidity, packaging)
root.order.add_edge(packaging, label_print)
root.order.add_edge(label_print, cold_storage)
root.order.add_edge(cold_storage, order_proc)
root.order.add_edge(order_proc, logistics)
root.order.add_edge(logistics, delivery)
root.order.add_edge(delivery, feedback)
root.order.add_edge(feedback, batch_adj)
root.order.add_edge(batch_adj, inventory_loop)
root.order.add_edge(inventory_loop, batch_adj)  # Loop condition back to adjust
root.order.add_edge(batch_adj, event_coord)
root.order.add_edge(event_coord, inventory_loop)