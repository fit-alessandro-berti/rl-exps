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

loop_milk_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing])
loop_starter_prep = OperatorPOWL(operator=Operator.LOOP, children=[starter_prep, curd_cutting])
loop_molding_cheese = OperatorPOWL(operator=Operator.LOOP, children=[molding_cheese, salting_process])
loop_aging_control = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, humidity_check])
loop_packaging_design = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, label_printing])
loop_inventory_audit = OperatorPOWL(operator=Operator.LOOP, children=[inventory_audit, cold_storage])
loop_order_processing = OperatorPOWL(operator=Operator.LOOP, children=[order_processing, logistics_planning])
loop_retail_delivery = OperatorPOWL(operator=Operator.LOOP, children=[retail_delivery, consumer_feedback])
loop_batch_adjustment = OperatorPOWL(operator=Operator.LOOP, children=[batch_adjustment, event_coordination])

root = StrictPartialOrder(nodes=[
    loop_milk_sourcing,
    loop_starter_prep,
    loop_molding_cheese,
    loop_aging_control,
    loop_packaging_design,
    loop_inventory_audit,
    loop_order_processing,
    loop_retail_delivery,
    loop_batch_adjustment
])
root.order.add_edge(loop_milk_sourcing, loop_starter_prep)
root.order.add_edge(loop_starter_prep, loop_molding_cheese)
root.order.add_edge(loop_molding_cheese, loop_aging_control)
root.order.add_edge(loop_aging_control, loop_packaging_design)
root.order.add_edge(loop_packaging_design, loop_inventory_audit)
root.order.add_edge(loop_inventory_audit, loop_order_processing)
root.order.add_edge(loop_order_processing, loop_retail_delivery)
root.order.add_edge(loop_retail_delivery, loop_batch_adjustment)