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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, skip])
xor_quality = OperatorPOWL(operator=Operator.XOR, children=[quality_check, skip])
xor_compliance = OperatorPOWL(operator=Operator.XOR, children=[compliance_audit, skip])
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, skip])
xor_logistics = OperatorPOWL(operator=Operator.XOR, children=[carrier_booking, skip])
xor_trace = OperatorPOWL(operator=Operator.XOR, children=[trace_recording, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    curd_formation,
    microbial_test,
    whey_removal,
    pressing_cheese,
    salt_application,
    loop_aging,
    quality_check,
    eco_packaging,
    inventory_log,
    temp_monitoring,
    carrier_booking,
    trace_recording,
    feedback_review,
    compliance_audit,
    batch_adjustment
])

# Define the dependencies
root.order.add_edge(milk_sourcing, curd_formation)
root.order.add_edge(curd_formation, microbial_test)
root.order.add_edge(microbial_test, whey_removal)
root.order.add_edge(whey_removal, pressing_cheese)
root.order.add_edge(pressing_cheese, salt_application)
root.order.add_edge(salt_application, aging_control)
root.order.add_edge(aging_control, xor_quality)
root.order.add_edge(xor_quality, quality_check)
root.order.add_edge(quality_check, eco_packaging)
root.order.add_edge(eco_packaging, inventory_log)
root.order.add_edge(inventory_log, temp_monitoring)
root.order.add_edge(temp_monitoring, xor_logistics)
root.order.add_edge(xor_logistics, carrier_booking)
root.order.add_edge(carrier_booking, xor_trace)
root.order.add_edge(xor_trace, trace_recording)
root.order.add_edge(trace_recording, xor_feedback)
root.order.add_edge(xor_feedback, feedback_review)
root.order.add_edge(feedback_review, xor_compliance)
root.order.add_edge(xor_compliance, compliance_audit)
root.order.add_edge(compliance_audit, batch_adjustment)

print(root)