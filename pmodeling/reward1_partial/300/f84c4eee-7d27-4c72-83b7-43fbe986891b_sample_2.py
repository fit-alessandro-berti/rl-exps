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

# Define the POWL model
root = StrictPartialOrder()

# Define the flow of activities
root.nodes.add(component_sourcing)
root.nodes.add(frame_assembly)
root.nodes.add(sensor_mounting)
root.nodes.add(wiring_harness)
root.nodes.add(circuit_testing)
root.nodes.add(firmware_loading)
root.nodes.add(initial_calibration)
root.nodes.add(software_integration)
root.nodes.add(flight_testing)
root.nodes.add(data_logging)
root.nodes.add(performance_tuning)
root.nodes.add(packaging_prep)
root.nodes.add(custom_labeling)
root.nodes.add(documentation_print)
root.nodes.add(quality_review)
root.nodes.add(client_training)
root.nodes.add(remote_monitoring)
root.nodes.add(firmware_update)

# Define the order of execution
root.order.add_edge(component_sourcing, frame_assembly)
root.order.add_edge(frame_assembly, sensor_mounting)
root.order.add_edge(sensor_mounting, wiring_harness)
root.order.add_edge(wiring_harness, circuit_testing)
root.order.add_edge(circuit_testing, firmware_loading)
root.order.add_edge(firmware_loading, initial_calibration)
root.order.add_edge(initial_calibration, software_integration)
root.order.add_edge(software_integration, flight_testing)
root.order.add_edge(flight_testing, data_logging)
root.order.add_edge(data_logging, performance_tuning)
root.order.add_edge(performance_tuning, packaging_prep)
root.order.add_edge(packaging_prep, custom_labeling)
root.order.add_edge(custom_labeling, documentation_print)
root.order.add_edge(documentation_print, quality_review)
root.order.add_edge(quality_review, client_training)
root.order.add_edge(client_training, remote_monitoring)
root.order.add_edge(remote_monitoring, firmware_update)

# Define the loop for firmware update
firmware_update_loop = OperatorPOWL(operator=Operator.LOOP, children=[firmware_update])
root.nodes.add(firmware_update_loop)
root.order.add_edge(firmware_update, firmware_update_loop)
root.order.add_edge(firmware_update_loop, firmware_update)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update, documentation_print_firmware_update_xor)

# Define the xor for client training and remote monitoring
client_training_remote_monitoring_xor = OperatorPOWL(operator=Operator.XOR, children=[client_training, remote_monitoring])
root.nodes.add(client_training_remote_monitoring_xor)
root.order.add_edge(client_training, client_training_remote_monitoring_xor)
root.order.add_edge(remote_monitoring, client_training_remote_monitoring_xor)

# Define the xor for documentation print and firmware update
documentation_print_firmware_update_xor = OperatorPOWL(operator=Operator.XOR, children=[documentation_print, firmware_update])
root.nodes.add(documentation_print_firmware_update_xor)
root.order.add_edge(documentation_print, documentation_print_firmware_update_xor)
root.order.add_edge(firmware_update