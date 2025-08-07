import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
comp_sourcing   = Transition(label='Component Sourcing')
frame_assembly  = Transition(label='Frame Assembly')
sensor_mounting = Transition(label='Sensor Mounting')
wiring_harness  = Transition(label='Wiring Harness')
circuit_test    = Transition(label='Circuit Testing')
firmware_load   = Transition(label='Firmware Loading')
initial_calib   = Transition(label='Initial Calibration')
software_int    = Transition(label='Software Integration')
flight_test     = Transition(label='Flight Testing')
data_logging    = Transition(label='Data Logging')
performance_tuning = Transition(label='Performance Tuning')
packaging_prep  = Transition(label='Packaging Prep')
custom_labeling = Transition(label='Custom Labeling')
doc_print       = Transition(label='Documentation Print')
quality_review  = Transition(label='Quality Review')
client_training = Transition(label='Client Training')
remote_monitoring = Transition(label='Remote Monitoring')
firmware_update = Transition(label='Firmware Update')

# Loop for flight testing and performance tuning
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_test, data_logging, performance_tuning])

# Build the partial order
root = StrictPartialOrder(nodes=[
    comp_sourcing,
    frame_assembly,
    sensor_mounting,
    wiring_harness,
    circuit_test,
    firmware_load,
    initial_calib,
    software_int,
    flight_loop,
    packaging_prep,
    custom_labeling,
    doc_print,
    quality_review,
    client_training,
    remote_monitoring,
    firmware_update
])

# Define the control-flow dependencies
root.order.add_edge(comp_sourcing, frame_assembly)
root.order.add_edge(frame_assembly, [sensor_mounting, wiring_harness])
root.order.add_edge(sensor_mounting, circuit_test)
root.order.add_edge(wiring_harness, circuit_test)
root.order.add_edge(circuit_test, firmware_load)
root.order.add_edge(firmware_load, initial_calib)
root.order.add_edge(initial_calib, software_int)
root.order.add_edge(software_int, flight_loop)
root.order.add_edge(flight_loop, packaging_prep)
root.order.add_edge(packaging_prep, [custom_labeling, doc_print])
root.order.add_edge(custom_labeling, quality_review)
root.order.add_edge(doc_print, quality_review)
root.order.add_edge(quality_review, client_training)
root.order.add_edge(client_training, [remote_monitoring, firmware_update])
root.order.add_edge(remote_monitoring, firmware_update)
root.order.add_edge(firmware_update, firmware_update)  # Loop back for remote updates

print(root)