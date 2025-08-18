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

# Define workflow steps
milk_sourcing_to_quality_testing = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, skip])
quality_testing_to_starter_prep = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, skip])
starter_prep_to_curd_cutting = OperatorPOWL(operator=Operator.XOR, children=[starter_prep, skip])
curd_cutting_to_molding_cheese = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, skip])
molding_cheese_to_salting_process = OperatorPOWL(operator=Operator.XOR, children=[molding_cheese, skip])
salting_process_to_aging_control = OperatorPOWL(operator=Operator.XOR, children=[salting_process, skip])
aging_control_to_humidity_check = OperatorPOWL(operator=Operator.XOR, children=[aging_control, skip])
humidity_check_to_packaging_design = OperatorPOWL(operator=Operator.XOR, children=[humidity_check, skip])
packaging_design_to_label_printing = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, skip])
label_printing_to_inventory_audit = OperatorPOWL(operator=Operator.XOR, children=[label_printing, skip])
inventory_audit_to_cold_storage = OperatorPOWL(operator=Operator.XOR, children=[inventory_audit, skip])
cold_storage_to_order_processing = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, skip])
order_processing_to_logistics_planning = OperatorPOWL(operator=Operator.XOR, children=[order_processing, skip])
logistics_planning_to_retail_delivery = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning, skip])
retail_delivery_to_consumer_feedback = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, skip])
consumer_feedback_to_batch_adjustment = OperatorPOWL(operator=Operator.XOR, children=[consumer_feedback, skip])
batch_adjustment_to_event_coordination = OperatorPOWL(operator=Operator.XOR, children=[batch_adjustment, skip])
event_coordination_to_milk_sourcing = OperatorPOWL(operator=Operator.XOR, children=[event_coordination, skip])

# Define the root node
root = StrictPartialOrder(nodes=[
    milk_sourcing_to_quality_testing,
    quality_testing_to_starter_prep,
    starter_prep_to_curd_cutting,
    curd_cutting_to_molding_cheese,
    molding_cheese_to_salting_process,
    salting_process_to_aging_control,
    aging_control_to_humidity_check,
    humidity_check_to_packaging_design,
    packaging_design_to_label_printing,
    label_printing_to_inventory_audit,
    inventory_audit_to_cold_storage,
    cold_storage_to_order_processing,
    order_processing_to_logistics_planning,
    logistics_planning_to_retail_delivery,
    retail_delivery_to_consumer_feedback,
    consumer_feedback_to_batch_adjustment,
    batch_adjustment_to_event_coordination,
    event_coordination_to_milk_sourcing
])