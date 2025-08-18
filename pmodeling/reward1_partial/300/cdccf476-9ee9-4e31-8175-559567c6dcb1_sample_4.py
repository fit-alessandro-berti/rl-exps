import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
milk_sourcing = Transition(label='Milk Sourcing')
curd_formation = Transition(label='Curd Formation')
microbial_test = Transition(label='Microbial Test')
whey_removal = Transition(label='Whey Removal')
pressing_cheese = Transition(label='Pressing Cheese')
salt_application = Transition(label='Salt Application')
aging_control = Transition(label='Aging Control')
quality_check = Transition(label='Quality Check')
eco_packaging = Transition(label='Eco Packaging')
inventory_log = Transition(label='Inventory Log')
temp_monitoring = Transition(label='Temp Monitoring')
carrier_booking = Transition(label='Carrier Booking')
trace_recording = Transition(label='Trace Recording')
feedback_review = Transition(label='Feedback Review')
compliance_audit = Transition(label='Compliance Audit')
batch_adjustment = Transition(label='Batch Adjustment')

# Define silent transitions
skip = SilentTransition()

# Define loops and exclusive choices
milk_supply_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, skip])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, skip])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_review, skip])
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_audit, skip])
batch_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_adjustment, skip])

# Define exclusive choices
microbial_test_choice = OperatorPOWL(operator=Operator.XOR, children=[microbial_test, skip])
quality_check_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_check, skip])
inventory_choice = OperatorPOWL(operator=Operator.XOR, children=[inventory_log, skip])
temp_monitoring_choice = OperatorPOWL(operator=Operator.XOR, children=[temp_monitoring, skip])
carrier_booking_choice = OperatorPOWL(operator=Operator.XOR, children=[carrier_booking, skip])
trace_recording_choice = OperatorPOWL(operator=Operator.XOR, children=[trace_recording, skip])
feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, skip])
audit_choice = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, skip])
batch_choice = OperatorPOWL(operator=Operator.XOR, children=[batch_adjustment, skip])

# Define the root model
root = StrictPartialOrder(nodes=[
    milk_supply_loop,
    aging_loop,
    microbial_test_choice,
    quality_check_choice,
    inventory_choice,
    temp_monitoring_choice,
    carrier_booking_choice,
    trace_recording_choice,
    feedback_choice,
    audit_choice,
    batch_choice,
    eco_packaging,
    whey_removal,
    pressing_cheese,
    salt_application,
    feedback_review,
    compliance_audit,
    batch_adjustment
])

# Define dependencies between nodes
root.order.add_edge(milk_supply_loop, microbial_test_choice)
root.order.add_edge(microbial_test_choice, quality_check_choice)
root.order.add_edge(quality_check_choice, inventory_choice)
root.order.add_edge(inventory_choice, temp_monitoring_choice)
root.order.add_edge(temp_monitoring_choice, carrier_booking_choice)
root.order.add_edge(carrier_booking_choice, trace_recording_choice)
root.order.add_edge(trace_recording_choice, feedback_choice)
root.order.add_edge(feedback_choice, audit_choice)
root.order.add_edge(audit_choice, batch_choice)
root.order.add_edge(milk_supply_loop, eco_packaging)
root.order.add_edge(eco_packaging, whey_removal)
root.order.add_edge(whey_removal, pressing_cheese)
root.order.add_edge(pressing_cheese, salt_application)
root.order.add_edge(salt_application, aging_loop)
root.order.add_edge(aging_loop, feedback_review)
root.order.add_edge(feedback_review, compliance_audit)
root.order.add_edge(compliance_audit, batch_adjustment)

print(root)