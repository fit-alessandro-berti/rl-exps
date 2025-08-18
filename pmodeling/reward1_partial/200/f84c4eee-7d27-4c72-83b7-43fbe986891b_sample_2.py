import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Sequence of activities for component sourcing
sourcing_seq = StrictPartialOrder(nodes=[component_sourcing])

# Sequence of activities for frame assembly and electronics integration
frame_assembly_seq = StrictPartialOrder(nodes=[frame_assembly, sensor_mounting, wiring_harness, circuit_testing, firmware_loading])

# Sequence of activities for software loading and initial calibration
software_seq = StrictPartialOrder(nodes=[software_integration, initial_calibration])

# Sequence of activities for flight testing and data logging
flight_seq = StrictPartialOrder(nodes=[flight_testing, data_logging, performance_tuning])

# Loop for quality review and client training
quality_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_review, client_training])
quality_loop.order.add_edge(quality_loop, client_training)

# Parallel activities for packaging prep, custom labeling, and documentation print
packaging_parallel = StrictPartialOrder(nodes=[packaging_prep, custom_labeling, documentation_print])
packaging_parallel.order.add_edge(packaging_prep, custom_labeling)
packaging_parallel.order.add_edge(packaging_prep, documentation_print)
packaging_parallel.order.add_edge(custom_labeling, documentation_print)

# Sequence for remote monitoring and firmware update
monitoring_seq = StrictPartialOrder(nodes=[remote_monitoring, firmware_update])

# Root model representing the entire process
root = StrictPartialOrder(nodes=[sourcing_seq, frame_assembly_seq, software_seq, flight_seq, quality_loop, packaging_parallel, monitoring_seq])
root.order.add_edge(sourcing_seq, frame_assembly_seq)
root.order.add_edge(frame_assembly_seq, software_seq)
root.order.add_edge(software_seq, flight_seq)
root.order.add_edge(flight_seq, quality_loop)
root.order.add_edge(quality_loop, packaging_parallel)
root.order.add_edge(packaging_parallel, monitoring_seq)