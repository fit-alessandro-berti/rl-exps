import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
loop_curd_formation = OperatorPOWL(operator=Operator.LOOP, children=[curd_formation, whey_removal, pressing_cheese, salt_application, aging_control])
xor_quality_check = OperatorPOWL(operator=Operator.XOR, children=[quality_check, skip])
xor_eco_packaging = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, skip])
xor_inventory_log = OperatorPOWL(operator=Operator.XOR, children=[inventory_log, skip])
xor_temp_monitoring = OperatorPOWL(operator=Operator.XOR, children=[temp_monitoring, skip])
xor_carrier_booking = OperatorPOWL(operator=Operator.XOR, children=[carrier_booking, skip])
xor_trace_recording = OperatorPOWL(operator=Operator.XOR, children=[trace_recording, skip])
xor_feedback_review = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, skip])
xor_compliance_audit = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, batch_adjustment])

root = StrictPartialOrder(nodes=[
    milk_sourcing,
    loop_curd_formation,
    xor_quality_check,
    xor_eco_packaging,
    xor_inventory_log,
    xor_temp_monitoring,
    xor_carrier_booking,
    xor_trace_recording,
    xor_feedback_review,
    xor_compliance_audit
])
root.order.add_edge(loop_curd_formation, xor_quality_check)
root.order.add_edge(loop_curd_formation, xor_eco_packaging)
root.order.add_edge(loop_curd_formation, xor_inventory_log)
root.order.add_edge(loop_curd_formation, xor_temp_monitoring)
root.order.add_edge(loop_curd_formation, xor_carrier_booking)
root.order.add_edge(loop_curd_formation, xor_trace_recording)
root.order.add_edge(loop_curd_formation, xor_feedback_review)
root.order.add_edge(loop_curd_formation, xor_compliance_audit)

print(root)