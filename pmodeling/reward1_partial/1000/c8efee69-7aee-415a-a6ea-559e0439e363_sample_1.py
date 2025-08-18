import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_prep = Transition(label='Starter Prep')
curd_cutting = Transition(label='Curd Cutting')
molding_cheese = Transition(label='Molding Cheese')
salting_process = Transition(label='Salting Process')
aging_control = Transition(label='Aging Control')
humidity_check = Transition(label='Humidity Check')
packaging_design = Transition(label='Packaging Design')
label_printing = Transition(label='Label Printing')
inventory_audit = Transition(label='Inventory Audit')
cold_storage = Transition(label='Cold Storage')
order_processing = Transition(label='Order Processing')
logistics_planning = Transition(label='Logistics Planning')
retail_delivery = Transition(label='Retail Delivery')
consumer_feedback = Transition(label='Consumer Feedback')
batch_adjustment = Transition(label='Batch Adjustment')
event_coordination = Transition(label='Event Coordination')

skip = SilentTransition()

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    starter_prep,
    curd_cutting,
    molding_cheese,
    salting_process,
    aging_control,
    humidity_check,
    packaging_design,
    label_printing,
    inventory_audit,
    cold_storage,
    order_processing,
    logistics_planning,
    retail_delivery,
    consumer_feedback,
    batch_adjustment,
    event_coordination
])

# Define dependencies (partial order)
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_prep)
root.order.add_edge(starter_prep, curd_cutting)
root.order.add_edge(curd_cutting, molding_cheese)
root.order.add_edge(molding_cheese, salting_process)
root.order.add_edge(salting_process, aging_control)
root.order.add_edge(aging_control, humidity_check)
root.order.add_edge(humidity_check, packaging_design)
root.order.add_edge(packaging_design, label_printing)
root.order.add_edge(label_printing, inventory_audit)
root.order.add_edge(inventory_audit, cold_storage)
root.order.add_edge(cold_storage, order_processing)
root.order.add_edge(order_processing, logistics_planning)
root.order.add_edge(logistics_planning, retail_delivery)
root.order.add_edge(retail_delivery, consumer_feedback)
root.order.add_edge(consumer_feedback, batch_adjustment)
root.order.add_edge(batch_adjustment, event_coordination)