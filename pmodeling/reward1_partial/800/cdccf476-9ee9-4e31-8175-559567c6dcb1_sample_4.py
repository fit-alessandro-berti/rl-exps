import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the process structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    milk_sourcing,
    curd_formation,
    microbial_test,
    whey_removal,
    pressing_cheese,
    salt_application,
    aging_control,
    quality_check,
    eco_packaging,
    inventory_log,
    temp_monitoring
])

xor = OperatorPOWL(operator=Operator.XOR, children=[
    trace_recording,
    feedback_review,
    compliance_audit,
    batch_adjustment
])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)