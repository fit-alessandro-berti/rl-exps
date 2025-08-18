import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the POWL model
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

# Define the control-flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, curd_formation])
microbial_test_choice = OperatorPOWL(operator=Operator.XOR, children=[microbial_test, whey_removal])
aging_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, quality_check])
eco_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, inventory_log])
temp_monitoring_choice = OperatorPOWL(operator=Operator.XOR, children=[temp_monitoring, carrier_booking])
trace_recording_loop = OperatorPOWL(operator=Operator.LOOP, children=[trace_recording, feedback_review])
compliance_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, batch_adjustment])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[exclusive_choice, microbial_test_choice, aging_control_loop, eco_packaging_choice, temp_monitoring_choice, trace_recording_loop, compliance_audit_choice])
root.order.add_edge(exclusive_choice, microbial_test_choice)
root.order.add_edge(microbial_test_choice, aging_control_loop)
root.order.add_edge(aging_control_loop, eco_packaging_choice)
root.order.add_edge(eco_packaging_choice, temp_monitoring_choice)
root.order.add_edge(temp_monitoring_choice, trace_recording_loop)
root.order.add_edge(trace_recording_loop, compliance_audit_choice)

# Print the root of the POWL model
print(root)