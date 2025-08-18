import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loops and choices
raw_milk_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing, starter_prep])
aging_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[molding_cheese, salting_process, aging_control, humidity_check])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, label_printing, inventory_audit, cold_storage])
order_loop = OperatorPOWL(operator=Operator.LOOP, children=[order_processing, logistics_planning, retail_delivery, consumer_feedback, batch_adjustment, event_coordination])

# Define the partial order
root = StrictPartialOrder(nodes=[raw_milk_loop, aging_control_loop, packaging_loop, order_loop])
root.order.add_edge(raw_milk_loop, aging_control_loop)
root.order.add_edge(aging_control_loop, packaging_loop)
root.order.add_edge(packaging_loop, order_loop)