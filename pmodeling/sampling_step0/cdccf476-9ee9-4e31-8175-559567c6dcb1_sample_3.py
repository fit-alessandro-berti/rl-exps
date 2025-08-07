import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define silent transitions for loops and choices
skip = SilentTransition()

# Define the loop for aging control
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control])

# Define the choice between Microbial Test and Quality Check
microbial_test_quality_check_choice = OperatorPOWL(operator=Operator.XOR, children=[microbial_test, quality_check])

# Define the loop for inventory log
inventory_log_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_log])

# Define the loop for carrier booking
carrier_booking_loop = OperatorPOWL(operator=Operator.LOOP, children=[carrier_booking])

# Define the loop for trace recording
trace_recording_loop = OperatorPOWL(operator=Operator.LOOP, children=[trace_recording])

# Define the loop for feedback review
feedback_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_review])

# Define the loop for compliance audit
compliance_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_audit])

# Define the loop for batch adjustment
batch_adjustment_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_adjustment])

# Define the partial order
root = StrictPartialOrder(nodes=[milk_sourcing, curd_formation, whey_removal, pressing_cheese, salt_application, aging_loop, microbial_test_quality_check_choice, eco_packaging, inventory_log_loop, temp_monitoring, carrier_booking_loop, trace_recording_loop, feedback_review_loop, compliance_audit_loop, batch_adjustment_loop])
root.order.add_edge(milk_sourcing, curd_formation)
root.order.add_edge(curd_formation, whey_removal)
root.order.add_edge(whey_removal, pressing_cheese)
root.order.add_edge(pressing_cheese, salt_application)
root.order.add_edge(salt_application, aging_control)
root.order.add_edge(aging_control, aging_loop)
root.order.add_edge(aging_loop, microbial_test_quality_check_choice)
root.order.add_edge(microbial_test_quality_check_choice, eco_packaging)
root.order.add_edge(eco_packaging, inventory_log)
root.order.add_edge(inventory_log, inventory_log_loop)
root.order.add_edge(inventory_log_loop, temp_monitoring)
root.order.add_edge(temp_monitoring, carrier_booking)
root.order.add_edge(carrier_booking, carrier_booking_loop)
root.order.add_edge(carrier_booking_loop, trace_recording)
root.order.add_edge(trace_recording, trace_recording_loop)
root.order.add_edge(trace_recording_loop, feedback_review)
root.order.add_edge(feedback_review, feedback_review_loop)
root.order.add_edge(feedback_review_loop, compliance_audit)
root.order.add_edge(compliance_audit, compliance_audit_loop)
root.order.add_edge(compliance_audit_loop, batch_adjustment)
root.order.add_edge(batch_adjustment, batch_adjustment_loop)