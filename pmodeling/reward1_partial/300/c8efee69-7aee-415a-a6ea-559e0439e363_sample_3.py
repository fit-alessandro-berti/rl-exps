import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[starter_prep, curd_cutting])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[molding_cheese, salting_process])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[aging_control, humidity_check])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_printing])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[inventory_audit, cold_storage])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[order_processing, logistics_planning])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, consumer_feedback])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[batch_adjustment, event_coordination])

# Define the partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)