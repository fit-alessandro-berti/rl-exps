import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
component_sourcing = Transition(label='Component Sourcing')
frame_assembly = Transition(label='Frame Assembly')
sensor_mounting = Transition(label='Sensor Mounting')
wiring_harness = Transition(label='Wiring Harness')
circuit_testing = Transition(label='Circuit Testing')
firmware_loading = Transition(label='Firmware Loading')
initial_calibration = Transition(label='Initial Calibration')
software_integration = Transition(label='Software Integration')
flight_testing = Transition(label='Flight Testing')
data_logging = Transition(label='Data Logging')
performance_tuning = Transition(label='Performance Tuning')
packaging_prep = Transition(label='Packaging Prep')
custom_labeling = Transition(label='Custom Labeling')
documentation_print = Transition(label='Documentation Print')
quality_review = Transition(label='Quality Review')
client_training = Transition(label='Client Training')
remote_monitoring = Transition(label='Remote Monitoring')
firmware_update = Transition(label='Firmware Update')

# Define silent transitions for empty labels
skip = SilentTransition()

# Define loops and choices for the process
loop_initial_calibration = OperatorPOWL(operator=Operator.LOOP, children=[initial_calibration, circuit_testing])
loop_performance_tuning = OperatorPOWL(operator=Operator.LOOP, children=[performance_tuning, data_logging])
loop_remote_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[remote_monitoring, firmware_update])

choice_sensor_mounting = OperatorPOWL(operator=Operator.XOR, children=[sensor_mounting, skip])
choice_wiring_harness = OperatorPOWL(operator=Operator.XOR, children=[wiring_harness, skip])

choice_flight_testing = OperatorPOWL(operator=Operator.XOR, children=[flight_testing, skip])

choice_quality_review = OperatorPOWL(operator=Operator.XOR, children=[quality_review, skip])

choice_client_training = OperatorPOWL(operator=Operator.XOR, children=[client_training, skip])

choice_firmware_update = OperatorPOWL(operator=Operator.XOR, children=[firmware_update, skip])

root = StrictPartialOrder(nodes=[loop_initial_calibration, loop_performance_tuning, loop_remote_monitoring, choice_sensor_mounting, choice_wiring_harness, choice_flight_testing, choice_quality_review, choice_client_training, choice_firmware_update])
root.order.add_edge(loop_initial_calibration, loop_performance_tuning)
root.order.add_edge(loop_initial_calibration, loop_remote_monitoring)
root.order.add_edge(loop_performance_tuning, loop_remote_monitoring)
root.order.add_edge(choice_sensor_mounting, loop_initial_calibration)
root.order.add_edge(choice_wiring_harness, loop_initial_calibration)
root.order.add_edge(choice_flight_testing, loop_performance_tuning)
root.order.add_edge(choice_quality_review, loop_remote_monitoring)
root.order.add_edge(choice_client_training, loop_remote_monitoring)
root.order.add_edge(choice_firmware_update, loop_remote_monitoring)