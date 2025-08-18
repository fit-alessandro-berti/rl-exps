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
aging_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, temp_monitoring])

# Define the exclusive choice for eco packaging
eco_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, carrier_booking])

# Define the exclusive choice for trace recording
trace_recording_choice = OperatorPOWL(operator=Operator.XOR, children=[trace_recording, feedback_review])

# Define the loop for compliance audit
compliance_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_audit, batch_adjustment])

# Define the root partial order
root = StrictPartialOrder(nodes=[milk_sourcing, curd_formation, microbial_test, whey_removal, pressing_cheese, salt_application, aging_control_loop, quality_check, eco_packaging_choice, inventory_log, temp_monitoring, trace_recording_choice, compliance_audit_loop])
root.order.add_edge(milk_sourcing, curd_formation)
root.order.add_edge(curd_formation, microbial_test)
root.order.add_edge(microbial_test, whey_removal)
root.order.add_edge(whey_removal, pressing_cheese)
root.order.add_edge(pressing_cheese, salt_application)
root.order.add_edge(salt_application, aging_control_loop)
root.order.add_edge(aging_control_loop, quality_check)
root.order.add_edge(quality_check, eco_packaging_choice)
root.order.add_edge(eco_packaging_choice, inventory_log)
root.order.add_edge(inventory_log, temp_monitoring)
root.order.add_edge(temp_monitoring, trace_recording_choice)
root.order.add_edge(trace_recording_choice, compliance_audit_loop)
root.order.add_edge(compliance_audit_loop, batch_adjustment)