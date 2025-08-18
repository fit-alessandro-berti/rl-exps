import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
component_sourcing = Transition(label='Component Sourcing')
frame_assembly = Transition(label='Frame Assembly')
sensor_mouting = Transition(label='Sensor Mounting')
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[firmware_loading, circuit_testing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[firmware_update, firmware_loading])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[quality_review, client_training])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[remote_monitoring, firmware_update])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[flight_testing, data_logging, performance_tuning])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[custom_labeling, documentation_print])

# Define the POWL model structure
root = StrictPartialOrder(nodes=[component_sourcing, frame_assembly, sensor_mouting, wiring_harness, xor, xor2, xor3, xor4, loop1, loop2])

# Define the order of the POWL model
root.order.add_edge(component_sourcing, frame_assembly)
root.order.add_edge(frame_assembly, sensor_mouting)
root.order.add_edge(sensor_mouting, wiring_harness)
root.order.add_edge(wiring_harness, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, firmware_update)
root.order.add_edge(loop2, client_training)
root.order.add_edge(loop2, remote_monitoring)

# Print the POWL model
print(root)