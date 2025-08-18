import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop for aging control
loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, quality_check])

# Define the XOR for eco packaging and inventory log
xor_eco_packaging_inventory = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, inventory_log])

# Define the XOR for temp monitoring and carrier booking
xor_temp_monitoring_carrier_booking = OperatorPOWL(operator=Operator.XOR, children=[temp_monitoring, carrier_booking])

# Define the XOR for trace recording and feedback review
xor_trace_recording_feedback_review = OperatorPOWL(operator=Operator.XOR, children=[trace_recording, feedback_review])

# Define the XOR for compliance audit and batch adjustment
xor_compliance_audit_batch_adjustment = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, batch_adjustment])

# Define the root model
root = StrictPartialOrder(nodes=[milk_sourcing, curd_formation, microbial_test, whey_removal, pressing_cheese, salt_application, loop, xor_eco_packaging_inventory, xor_temp_monitoring_carrier_booking, xor_trace_recording_feedback_review, xor_compliance_audit_batch_adjustment])
root.order.add_edge(milk_sourcing, curd_formation)
root.order.add_edge(curd_formation, microbial_test)
root.order.add_edge(microbial_test, whey_removal)
root.order.add_edge(whey_removal, pressing_cheese)
root.order.add_edge(pressing_cheese, salt_application)
root.order.add_edge(salt_application, loop)
root.order.add_edge(loop, xor_eco_packaging_inventory)
root.order.add_edge(xor_eco_packaging_inventory, xor_temp_monitoring_carrier_booking)
root.order.add_edge(xor_temp_monitoring_carrier_booking, xor_trace_recording_feedback_review)
root.order.add_edge(xor_trace_recording_feedback_review, xor_compliance_audit_batch_adjustment)