import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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
aging_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, batch_adjustment])

# Define the xor for eco packaging and inventory log
eco_packaging_inventory_xor = OperatorPOWL(operator=Operator.XOR, children=[eco_packaging, inventory_log])

# Define the xor for feedback review and compliance audit
feedback_review_audit_xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_review, compliance_audit])

# Define the xor for carrier booking and trace recording
carrier_booking_trace_xor = OperatorPOWL(operator=Operator.XOR, children=[carrier_booking, trace_recording])

# Define the xor for quality check and aging control loop
quality_check_aging_control_xor = OperatorPOWL(operator=Operator.XOR, children=[quality_check, aging_control_loop])

# Define the xor for salt application and aging control loop
salt_application_aging_control_xor = OperatorPOWL(operator=Operator.XOR, children=[salt_application, aging_control_loop])

# Define the xor for press cheese and aging control loop
press_cheese_aging_control_xor = OperatorPOWL(operator=Operator.XOR, children=[pressing_cheese, aging_control_loop])

# Define the xor for whey removal and aging control loop
whey_removal_aging_control_xor = OperatorPOWL(operator=Operator.XOR, children=[whey_removal, aging_control_loop])

# Define the xor for microbial test and aging control loop
microbial_test_aging_control_xor = OperatorPOWL(operator=Operator.XOR, children=[microbial_test, aging_control_loop])

# Define the xor for curd formation and aging control loop
curd_formation_aging_control_xor = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, aging_control_loop])

# Define the xor for milk sourcing and aging control loop
milk_sourcing_aging_control_xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, aging_control_loop])

# Define the xor for aging control loop and quality check
aging_control_loop_quality_check_xor = OperatorPOWL(operator=Operator.XOR, children=[aging_control_loop, quality_check])

# Define the xor for aging control loop and salt application
aging_control_loop_salt_application_xor = OperatorPOWL(operator=Operator.XOR, children=[aging_control_loop, salt_application])

# Define the xor for aging control loop and press cheese
aging_control_loop_press_cheese_xor = OperatorPOWL(operator=Operator.XOR, children=[aging_control_loop, pressing_cheese])

# Define the xor for aging control loop and whey removal
aging_control_loop_whey_removal_xor = OperatorPOWL(operator=Operator.XOR, children=[aging_control_loop, whey_removal])

# Define the xor for aging control loop and microbial test
aging_control_loop_microbial_test_xor = OperatorPOWL(operator=Operator.XOR, children=[aging_control_loop, microbial_test])

# Define the xor for aging control loop and curd formation
aging_control_loop_curd_formation_xor = OperatorPOWL(operator=Operator.XOR, children=[aging_control_loop, curd_formation])

# Define the xor for aging control loop and milk sourcing
aging_control_loop_milk_sourcing_xor = OperatorPOWL(operator=Operator.XOR, children=[aging_control_loop, milk_sourcing])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    milk_sourcing_aging_control_xor,
    curd_formation_aging_control_xor,
    microbial_test_aging_control_xor,
    whey_removal_aging_control_xor,
    pressing_cheese_aging_control_xor,
    salt_application_aging_control_xor,
    aging_control_loop_quality_check_xor,
    aging_control_loop_salt_application_xor,
    aging_control_loop_press_cheese_xor,
    aging_control_loop_whey_removal_xor,
    aging_control_loop_microbial_test_xor,
    aging_control_loop_curd_formation_xor,
    aging_control_loop_milk_sourcing_xor,
    feedback_review_audit_xor,
    carrier_booking_trace_xor,
    eco_packaging_inventory_xor,
    aging_control_loop
])

# Define the dependencies
root.order.add_edge(milk_sourcing_aging_control_xor, curd_formation_aging_control_xor)
root.order.add_edge(curd_formation_aging_control_xor, microbial_test_aging_control_xor)
root.order.add_edge(microbial_test_aging_control_xor, whey_removal_aging_control_xor)
root.order.add_edge(whey_removal_aging_control_xor, pressing_cheese_aging_control_xor)
root.order.add_edge(pressing_cheese_aging_control_xor, salt_application_aging_control_xor)
root.order.add_edge(salt_application_aging_control_xor, aging_control_loop_quality_check_xor)
root.order.add_edge(aging_control_loop_quality_check_xor, aging_control_loop_salt_application_xor)
root.order.add_edge(aging_control_loop_salt_application_xor, aging_control_loop_press_cheese_xor)
root.order.add_edge(aging_control_loop_press_cheese_xor, aging_control_loop_whey_removal_xor)
root.order.add_edge(aging_control_loop_whey_removal_xor, aging_control_loop_microbial_test_xor)
root.order.add_edge(aging_control_loop_microbial_test_xor, aging_control_loop_curd_formation_xor)
root.order.add_edge(aging_control_loop_curd_formation_xor, aging_control_loop_milk_sourcing_xor)
root.order.add_edge(aging_control_loop_milk_sourcing_xor, feedback_review_audit_xor)
root.order.add_edge(feedback_review_audit_xor, carrier_booking_trace_xor)
root.order.add_edge(carrier_booking_trace_xor, eco_packaging_inventory_xor)
root.order.add_edge(eco_packaging_inventory_xor, aging_control_loop)