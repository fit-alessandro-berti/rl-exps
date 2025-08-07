from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions based on the given activities
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

# Define the partial order structure
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

# Define dependencies between transitions (if any)
# In this case, there are no explicit dependencies mentioned, so we assume they are concurrent
# If dependencies were provided, they would be added here, e.g., root.order.add_edge(transition1, transition2)

# The root variable now contains the POWL model for the process