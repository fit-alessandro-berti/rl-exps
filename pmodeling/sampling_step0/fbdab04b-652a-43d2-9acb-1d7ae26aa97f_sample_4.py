import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define partial orders and control flow operators
partial_order_1 = OperatorPOWL(operator=Operator.LOOP, children=[client_consult, spec_analysis])
partial_order_2 = OperatorPOWL(operator=Operator.LOOP, children=[module_select, component_order])
partial_order_3 = OperatorPOWL(operator=Operator.LOOP, children=[parts_inspect, frame_assemble])
partial_order_4 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, motor_attach, wiring_connect, software_upload])
partial_order_5 = OperatorPOWL(operator=Operator.LOOP, children=[calibration_test, flight_simulate, quality_review])
partial_order_6 = OperatorPOWL(operator=Operator.LOOP, children=[user_train, remote_setup])
partial_order_7 = OperatorPOWL(operator=Operator.LOOP, children=[feedback_collect, support_schedule])

# Define exclusive choices
choice_1 = OperatorPOWL(operator=Operator.XOR, children=[partial_order_1, skip])
choice_2 = OperatorPOWL(operator=Operator.XOR, children=[partial_order_2, skip])
choice_3 = OperatorPOWL(operator=Operator.XOR, children=[partial_order_3, skip])
choice_4 = OperatorPOWL(operator=Operator.XOR, children=[partial_order_4, skip])
choice_5 = OperatorPOWL(operator=Operator.XOR, children=[partial_order_5, skip])
choice_6 = OperatorPOWL(operator=Operator.XOR, children=[partial_order_6, skip])
choice_7 = OperatorPOWL(operator=Operator.XOR, children=[partial_order_7, skip])

# Define root
root = StrictPartialOrder(nodes=[choice_1, choice_2, choice_3, choice_4, choice_5, choice_6, choice_7])
root.order.add_edge(choice_1, choice_2)
root.order.add_edge(choice_2, choice_3)
root.order.add_edge(choice_3, choice_4)
root.order.add_edge(choice_4, choice_5)
root.order.add_edge(choice_5, choice_6)
root.order.add_edge(choice_6, choice_7)