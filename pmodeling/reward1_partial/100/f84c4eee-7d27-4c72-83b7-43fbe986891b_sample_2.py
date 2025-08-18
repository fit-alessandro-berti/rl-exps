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

# Define the POWL model
# Start with the component sourcing
root = StrictPartialOrder(nodes=[component_sourcing])

# Frame assembly depends on component sourcing
root.order.add_edge(component_sourcing, frame_assembly)

# Sensor mounting depends on frame assembly
root.order.add_edge(frame_assembly, sensor_mounting)

# Wiring harness depends on sensor mounting
root.order.add_edge(sensor_mounting, wiring_harness)

# Circuit testing depends on wiring harness
root.order.add_edge(wiring_harness, circuit_testing)

# Firmware loading depends on circuit testing
root.order.add_edge(circuit_testing, firmware_loading)

# Initial calibration depends on firmware loading
root.order.add_edge(firmware_loading, initial_calibration)

# Software integration depends on initial calibration
root.order.add_edge(initial_calibration, software_integration)

# Flight testing depends on software integration
root.order.add_edge(software_integration, flight_testing)

# Data logging depends on flight testing
root.order.add_edge(flight_testing, data_logging)

# Performance tuning depends on data logging
root.order.add_edge(data_logging, performance_tuning)

# Packaging prep depends on performance tuning
root.order.add_edge(performance_tuning, packaging_prep)

# Custom labeling depends on packaging prep
root.order.add_edge(packaging_prep, custom_labeling)

# Documentation print depends on custom labeling
root.order.add_edge(custom_labeling, documentation_print)

# Quality review depends on documentation print
root.order.add_edge(documentation_print, quality_review)

# Client training depends on quality review
root.order.add_edge(quality_review, client_training)

# Remote monitoring depends on client training
root.order.add_edge(client_training, remote_monitoring)

# Firmware update depends on remote monitoring
root.order.add_edge(remote_monitoring, firmware_update)

# Now, the model is complete, and 'root' is the final POWL model.