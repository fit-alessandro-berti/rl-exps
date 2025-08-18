from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define nodes and operators
sourcing_quality = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
starter_prep_cutting = OperatorPOWL(operator=Operator.XOR, children=[starter_prep, curd_cutting])
molding_salting = OperatorPOWL(operator=Operator.XOR, children=[molding_cheese, salting_process])
aging_humidity = OperatorPOWL(operator=Operator.XOR, children=[aging_control, humidity_check])
packaging_label = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_printing])
inventory_audit_storage = OperatorPOWL(operator=Operator.XOR, children=[inventory_audit, cold_storage])
order_processing_logistics = OperatorPOWL(operator=Operator.XOR, children=[order_processing, logistics_planning])
retail_delivery_feedback = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, consumer_feedback])
batch_adjustment_event = OperatorPOWL(operator=Operator.XOR, children=[batch_adjustment, event_coordination])

# Define the root node with dependencies
root = StrictPartialOrder(nodes=[sourcing_quality, starter_prep_cutting, molding_salting, aging_humidity, packaging_label, inventory_audit_storage, order_processing_logistics, retail_delivery_feedback, batch_adjustment_event])
root.order.add_edge(sourcing_quality, starter_prep_cutting)
root.order.add_edge(starter_prep_cutting, molding_salting)
root.order.add_edge(molding_salting, aging_humidity)
root.order.add_edge(aging_humidity, packaging_label)
root.order.add_edge(packaging_label, inventory_audit_storage)
root.order.add_edge(inventory_audit_storage, order_processing_logistics)
root.order.add_edge(order_processing_logistics, retail_delivery_feedback)
root.order.add_edge(retail_delivery_feedback, batch_adjustment_event)