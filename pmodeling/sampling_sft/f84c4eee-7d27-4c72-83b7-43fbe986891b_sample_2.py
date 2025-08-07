import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
comp_sourcing    = Transition(label='Component Sourcing')
frame_assembly   = Transition(label='Frame Assembly')
sensor_mounting  = Transition(label='Sensor Mounting')
wiring_harness   = Transition(label='Wiring Harness')
circuit_testing  = Transition(label='Circuit Testing')
firmware_loading = Transition(label='Firmware Loading')
initial_calib    = Transition(label='Initial Calibration')
software_int     = Transition(label='Software Integration')
flight_testing   = Transition(label='Flight Testing')
data_logging     = Transition(label='Data Logging')
performance_tun  = Transition(label='Performance Tuning')
packaging_prep   = Transition(label='Packaging Prep')
custom_labeling  = Transition(label='Custom Labeling')
documentation    = Transition(label='Documentation Print')
quality_review   = Transition(label='Quality Review')
client_training  = Transition(label='Client Training')
remote_monitor   = Transition(label='Remote Monitoring')
firmware_update  = Transition(label='Firmware Update')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    comp_sourcing, frame_assembly, sensor_mounting, wiring_harness, circuit_testing,
    firmware_loading, initial_calib, software_int, flight_testing, data_logging,
    performance_tun, packaging_prep, custom_labeling, documentation, quality_review,
    client_training, remote_monitor, firmware_update
])

# Define the control‐flow dependencies
root.order.add_edge(comp_sourcing,    frame_assembly)
root.order.add_edge(frame_assembly,   sensor_mounting)
root.order.add_edge(frame_assembly,   wiring_harness)
root.order.add_edge(sensor_mounting,  circuit_testing)
root.order.add_edge(wiring_harness,   circuit_testing)
root.order.add_edge(circuit_testing,  firmware_loading)
root.order.add_edge(firmware_loading, initial_calib)
root.order.add_edge(initial_calib,    software_int)
root.order.add_edge(software_int,     flight_testing)
root.order.add_edge(flight_testing,   data_logging)
root.order.add_edge(flight_testing,   performance_tun)
root.order.add_edge(data_logging,     packaging_prep)
root.order.add_edge(data_logging,     custom_labeling)
root.order.add_edge(data_logging,     documentation)
root.order.add_edge(performance_tun,  quality_review)
root.order.add_edge(quality_review,   client_training)
root.order.add_edge(client_training,  remote_monitor)
root.order.add_edge(client_training,  firmware_update)

# Final loop: after training, clients can optionally schedule firmware updates
loop = OperatorPOWL(operator=Operator.LOOP, children=[firmware_update, client_training])
root.order.add_edge(client_training, loop)