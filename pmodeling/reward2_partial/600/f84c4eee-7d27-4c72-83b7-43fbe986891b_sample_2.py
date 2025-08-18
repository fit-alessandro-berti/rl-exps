import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the partial order model
root = StrictPartialOrder(nodes=[
    component_sourcing,
    frame_assembly,
    sensor_mounting,
    wiring_harness,
    circuit_testing,
    firmware_loading,
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

# Add dependencies to the partial order model
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

print(root)