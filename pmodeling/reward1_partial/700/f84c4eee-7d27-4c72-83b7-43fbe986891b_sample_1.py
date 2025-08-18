import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
source_component = Transition(label='Component Sourcing')
assemble_frame = Transition(label='Frame Assembly')
mount_sensors = Transition(label='Sensor Mounting')
wiring_harness = Transition(label='Wiring Harness')
circuit_testing = Transition(label='Circuit Testing')
load_firmware = Transition(label='Firmware Loading')
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    source_component,
    assemble_frame,
    mount_sensors,
    wiring_harness,
    circuit_testing,
    load_firmware,
    initial_calibration,
    software_integration,
    flight_testing,
    data_logging,
    performance_tuning,
    packaging_prep,
    custom_labeling,
    documentation_print,
    quality_review,
    client_training,
    remote_monitoring,
    firmware_update
])

# Define the dependencies between activities
root.order.add_edge(source_component, assemble_frame)
root.order.add_edge(assemble_frame, mount_sensors)
root.order.add_edge(mount_sensors, wiring_harness)
root.order.add_edge(wiring_harness, circuit_testing)
root.order.add_edge(circuit_testing, load_firmware)
root.order.add_edge(load_firmware, initial_calibration)
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

print(root)