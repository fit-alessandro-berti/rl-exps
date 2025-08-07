import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
milk_sourcing    = Transition(label='Milk Sourcing')
quality_testing  = Transition(label='Quality Testing')
starter_prep     = Transition(label='Starter Prep')
curd_cutting     = Transition(label='Curd Cutting')
molding_cheese   = Transition(label='Molding Cheese')
salting_process  = Transition(label='Salting Process')
aging_control    = Transition(label='Aging Control')
humidity_check   = Transition(label='Humidity Check')
packaging_design = Transition(label='Packaging Design')
label_printing   = Transition(label='Label Printing')
inventory_audit  = Transition(label='Inventory Audit')
cold_storage     = Transition(label='Cold Storage')
order_processing = Transition(label='Order Processing')
logistics_planning = Transition(label='Logistics Planning')
retail_delivery  = Transition(label='Retail Delivery')
consumer_feedback = Transition(label='Consumer Feedback')
batch_adjustment = Transition(label='Batch Adjustment')
event_coordination = Transition(label='Event Coordination')

# Build the loop body for the production cycle: after quality testing, repeat
# the milk sourcing, starter prep, curd cutting, molding, salting, aging,
# humidity check, packaging, and label printing steps
body = StrictPartialOrder(nodes=[
    starter_prep, curd_cutting, molding_cheese, salting_process,
    aging_control, humidity_check, packaging_design, label_printing
])
body.order.add_edge(starter_prep, curd_cutting)
body.order.add_edge(curd_cutting, molding_cheese)
body.order.add_edge(molding_cheese, salting_process)
body.order.add_edge(salting_process, aging_control)
body.order.add_edge(aging_control, humidity_check)
body.order.add_edge(humidity_check, packaging_design)
body.order.add_edge(packaging_design, label_printing)

# Loop: perform quality testing, then either exit or do the body and repeat
production_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, body])

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, quality_testing, production_loop,
    inventory_audit, cold_storage, order_processing,
    logistics_planning, retail_delivery, consumer_feedback,
    batch_adjustment, event_coordination
])

# Sequential control-flow: milk sourcing -> quality testing
root.order.add_edge(milk_sourcing, quality_testing)

# After quality testing, either exit or start the production loop
root.order.add_edge(quality_testing, production_loop)

# After the production loop, do the rest of the steps in sequence
root.order.add_edge(production_loop, inventory_audit)
root.order.add_edge(inventory_audit, cold_storage)
root.order.add_edge(cold_storage, order_processing)
root.order.add_edge(order_processing, logistics_planning)
root.order.add_edge(logistics_planning, retail_delivery)
root.order.add_edge(retail_delivery, consumer_feedback)
root.order.add_edge(consumer_feedback, batch_adjustment)
root.order.add_edge(batch_adjustment, event_coordination)