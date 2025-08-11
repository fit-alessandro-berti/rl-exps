import pm4py
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
aging_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, humidity_check])
inventory_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_audit, skip])

# Define exclusive choice nodes
raw_milk_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
starter_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[starter_prep, skip])
curd_cutting_choice = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, skip])
molding_cheese_choice = OperatorPOWL(operator=Operator.XOR, children=[molding_cheese, skip])
salting_process_choice = OperatorPOWL(operator=Operator.XOR, children=[salting_process, skip])
packaging_design_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_printing])
order_processing_choice = OperatorPOWL(operator=Operator.XOR, children=[order_processing, logistics_planning])
retail_delivery_choice = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, skip])
consumer_feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[consumer_feedback, skip])
batch_adjustment_choice = OperatorPOWL(operator=Operator.XOR, children=[batch_adjustment, skip])
event_coordination_choice = OperatorPOWL(operator=Operator.XOR, children=[event_coordination, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[raw_milk_choice, starter_prep_choice, curd_cutting_choice, molding_cheese_choice, salting_process_choice, packaging_design_choice, order_processing_choice, retail_delivery_choice, consumer_feedback_choice, batch_adjustment_choice, event_coordination_choice, aging_control_loop, inventory_audit_loop])
root.order.add_edge(raw_milk_choice, starter_prep_choice)
root.order.add_edge(starter_prep_choice, curd_cutting_choice)
root.order.add_edge(curd_cutting_choice, molding_cheese_choice)
root.order.add_edge(molding_cheese_choice, salting_process_choice)
root.order.add_edge(salting_process_choice, packaging_design_choice)
root.order.add_edge(packaging_design_choice, order_processing_choice)
root.order.add_edge(order_processing_choice, retail_delivery_choice)
root.order.add_edge(retail_delivery_choice, consumer_feedback_choice)
root.order.add_edge(consumer_feedback_choice, batch_adjustment_choice)
root.order.add_edge(batch_adjustment_choice, event_coordination_choice)
root.order.add_edge(event_coordination_choice, aging_control_loop)
root.order.add_edge(event_coordination_choice, inventory_audit_loop)