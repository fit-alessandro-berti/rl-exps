import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk_sourcing   = Transition(label='Milk Sourcing')
curd_formation  = Transition(label='Curd Formation')
whey_removal    = Transition(label='Whey Removal')
press_cheese    = Transition(label='Pressing Cheese')
salt_application= Transition(label='Salt Application')
microbial_test  = Transition(label='Microbial Test')
aging_control   = Transition(label='Aging Control')
quality_check   = Transition(label='Quality Check')
eco_packaging   = Transition(label='Eco Packaging')
inventory_log   = Transition(label='Inventory Log')
temp_monitoring = Transition(label='Temp Monitoring')
carrier_booking = Transition(label='Carrier Booking')
trace_recording = Transition(label='Trace Recording')
feedback_review = Transition(label='Feedback Review')
compliance_audit= Transition(label='Compliance Audit')
batch_adjustment= Transition(label='Batch Adjustment')

# Define the internal aging sub-process as a partial order
aging_po = StrictPartialOrder(nodes=[
    whey_removal, press_cheese, salt_application,
    aging_control, quality_check
])
aging_po.order.add_edge(whey_removal, press_cheese)
aging_po.order.add_edge(press_cheese, salt_application)
aging_po.order.add_edge(salt_application, aging_control)
aging_po.order.add_edge(aging_control, quality_check)

# Define the loop for iterative aging and quality checks
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_po, aging_po])

# Build the overall supply chain as a strict partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, curd_formation,
    microbial_test, aging_loop,
    eco_packaging, inventory_log,
    temp_monitoring, carrier_booking,
    trace_recording, feedback_review,
    compliance_audit, batch_adjustment
])

# Sequence all activities
root.order.add_edge(milk_sourcing, curd_formation)
root.order.add_edge(curd_formation, microbial_test)
root.order.add_edge(microbial_test, aging_loop)
root.order.add_edge(aging_loop, eco_packaging)
root.order.add_edge(eco_packaging, inventory_log)
root.order.add_edge(inventory_log, temp_monitoring)
root.order.add_edge(temp_monitoring, carrier_booking)
root.order.add_edge(carrier_booking, trace_recording)
root.order.add_edge(trace_recording, feedback_review)
root.order.add_edge(feedback_review, compliance_audit)
root.order.add_edge(compliance_audit, batch_adjustment)