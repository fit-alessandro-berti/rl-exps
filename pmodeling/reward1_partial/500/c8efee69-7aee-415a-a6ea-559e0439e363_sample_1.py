from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define a loop for the cheese-making process
cheese_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, starter_prep, curd_cutting, molding_cheese, salting_process, aging_control, humidity_check])

# Define a choice for packaging and cold storage
package_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_printing])
storage_choice = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, inventory_audit])

# Define a choice for logistics and order processing
logistics_choice = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning, order_processing])

# Define a choice for retail delivery and consumer feedback
delivery_choice = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, consumer_feedback])

# Define a choice for batch adjustment and event coordination
batch_choice = OperatorPOWL(operator=Operator.XOR, children=[batch_adjustment, event_coordination])

# Create the root POWL model
root = StrictPartialOrder(nodes=[cheese_loop, package_choice, storage_choice, logistics_choice, delivery_choice, batch_choice])
root.order.add_edge(cheese_loop, package_choice)
root.order.add_edge(cheese_loop, storage_choice)
root.order.add_edge(package_choice, logistics_choice)
root.order.add_edge(storage_choice, logistics_choice)
root.order.add_edge(logistics_choice, delivery_choice)
root.order.add_edge(logistics_choice, batch_choice)
root.order.add_edge(delivery_choice, batch_choice)

print(root)