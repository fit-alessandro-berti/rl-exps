import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
comp_sourcing      = Transition(label='Component Sourcing')
frame_assembly     = Transition(label='Frame Assembly')
sensor_mounting    = Transition(label='Sensor Mounting')
wiring_harness     = Transition(label='Wiring Harness')
circuit_testing    = Transition(label='Circuit Testing')
firmware_loading   = Transition(label='Firmware Loading')
initial_calibration= Transition(label='Initial Calibration')
software_integration= Transition(label='Software Integration')
flight_testing     = Transition(label='Flight Testing')
data_logging       = Transition(label='Data Logging')
performance_tuning = Transition(label='Performance Tuning')
packaging_prep     = Transition(label='Packaging Prep')
custom_labeling    = Transition(label='Custom Labeling')
documentation_print= Transition(label='Documentation Print')
quality_review     = Transition(label='Quality Review')
client_training    = Transition(label='Client Training')
remote_monitoring  = Transition(label='Remote Monitoring')
firmware_update    = Transition(label='Firmware Update')

# Define the optional remote monitoring and firmware update branch
remote_branch = StrictPartialOrder(nodes=[remote_monitoring, firmware_update])
# No edges here means they are concurrent

# Build the main assembly & calibration branch
main_branch = StrictPartialOrder(nodes=[
    comp_sourcing, frame_assembly, sensor_mounting,
    wiring_harness, circuit_testing, firmware_loading,
    initial_calibration, software_integration,
    flight_testing, data_logging, performance_tuning
])
# Define the control-flow dependencies
main_branch.order.add_edge(comp_sourcing, frame_assembly)
main_branch.order.add_edge(frame_assembly, sensor_mounting)
main_branch.order.add_edge(frame_assembly, wiring_harness)
main_branch.order.add_edge(sensor_mounting, circuit_testing)
main_branch.order.add_edge(wiring_harness, circuit_testing)
main_branch.order.add_edge(circuit_testing, firmware_loading)
main_branch.order.add_edge(firmware_loading, initial_calibration)
main_branch.order.add_edge(initial_calibration, software_integration)
main_branch.order.add_edge(software_integration, flight_testing)
main_branch.order.add_edge(flight_testing, data_logging)
main_branch.order.add_edge(data_logging, performance_tuning)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    main_branch, packaging_prep, custom_labeling, documentation_print,
    quality_review, client_training, remote_branch
])
# Define the control-flow dependencies
root.order.add_edge(main_branch, packaging_prep)
root.order.add_edge(main_branch, custom_labeling)
root.order.add_edge(main_branch, documentation_print)
root.order.add_edge(packaging_prep, quality_review)
root.order.add_edge(custom_labeling, quality_review)
root.order.add_edge(documentation_print, quality_review)
root.order.add_edge(quality_review, client_training)
root.order.add_edge(client_training, remote_branch)