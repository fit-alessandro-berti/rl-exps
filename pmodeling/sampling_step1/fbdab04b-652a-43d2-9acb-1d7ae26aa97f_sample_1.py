from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions
client_consult = Transition(label='Client Consult')
spec_analysis = Transition(label='Spec Analysis')
module_select = Transition(label='Module Select')
component_order = Transition(label='Component Order')
parts_inspect = Transition(label='Parts Inspect')
frame_assemble = Transition(label='Frame Assemble')
sensor_install = Transition(label='Sensor Install')
motor_attach = Transition(label='Motor Attach')
wiring_connect = Transition(label='Wiring Connect')
software_upload = Transition(label='Software Upload')
calibration_test = Transition(label='Calibration Test')
flight_simulate = Transition(label='Flight Simulate')
quality_review = Transition(label='Quality Review')
user_train = Transition(label='User Train')
remote_setup = Transition(label='Remote Setup')
feedback_collect = Transition(label='Feedback Collect')
support_schedule = Transition(label='Support Schedule')

# Define the loop and exclusive choice nodes
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[
    client_consult,
    spec_analysis,
    module_select,
    component_order,
    parts_inspect,
    frame_assemble,
    sensor_install,
    motor_attach,
    wiring_connect,
    software_upload,
    calibration_test,
    flight_simulate,
    quality_review
])

exclusive_choice_node = OperatorPOWL(operator=Operator.XOR, children=[
    user_train,
    remote_setup,
    feedback_collect,
    support_schedule
])

# Create the root POWL model
root = StrictPartialOrder(nodes=[loop_node, exclusive_choice_node])
root.order.add_edge(loop_node, exclusive_choice_node)

print(root)