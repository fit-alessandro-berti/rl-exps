from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
sourcing = Transition(label='Component Sourcing')
assembly = Transition(label='Frame Assembly')
mounting = Transition(label='Sensor Mounting')
wiring = Transition(label='Wiring Harness')
testing = Transition(label='Circuit Testing')
loading = Transition(label='Firmware Loading')
initial_calibration = Transition(label='Initial Calibration')
integration = Transition(label='Software Integration')
flight_testing = Transition(label='Flight Testing')
data_logging = Transition(label='Data Logging')
tuning = Transition(label='Performance Tuning')
packaging_prep = Transition(label='Packaging Prep')
labeling = Transition(label='Custom Labeling')
documentation = Transition(label='Documentation Print')
quality_review = Transition(label='Quality Review')
client_training = Transition(label='Client Training')
remote_monitoring = Transition(label='Remote Monitoring')
firmware_update = Transition(label='Firmware Update')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    sourcing, assembly, mounting, wiring, testing, loading, initial_calibration, integration, flight_testing, data_logging, tuning, packaging_prep, labeling, documentation, quality_review, client_training, remote_monitoring, firmware_update
])

# Define the order of activities
root.order.add_edge(sourcing, assembly)
root.order.add_edge(assembly, mounting)
root.order.add_edge(mounting, wiring)
root.order.add_edge(wiring, testing)
root.order.add_edge(testing, loading)
root.order.add_edge(loading, initial_calibration)
root.order.add_edge(initial_calibration, integration)
root.order.add_edge(integration, flight_testing)
root.order.add_edge(flight_testing, data_logging)
root.order.add_edge(data_logging, tuning)
root.order.add_edge(tuning, packaging_prep)
root.order.add_edge(packaging_prep, labeling)
root.order.add_edge(labeling, documentation)
root.order.add_edge(documentation, quality_review)
root.order.add_edge(quality_review, client_training)
root.order.add_edge(client_training, remote_monitoring)
root.order.add_edge(remote_monitoring, firmware_update)