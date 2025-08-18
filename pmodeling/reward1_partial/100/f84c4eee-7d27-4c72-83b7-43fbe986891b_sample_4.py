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

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define loops and exclusive choices
assembly_loop = OperatorPOWL(operator=Operator.LOOP, children=[frame_assembly, sensor_mounting, wiring_harness])
testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[circuit_testing, firmware_loading])
initial_calibration_loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_calibration, software_integration])
flight_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_testing, data_logging])
performance_tuning_loop = OperatorPOWL(operator=Operator.LOOP, children=[performance_tuning, quality_review])
training_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_training, remote_monitoring])

# Define exclusive choice for final steps
final_steps = OperatorPOWL(operator=Operator.XOR, children=[firmware_update, documentation_print])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    component_sourcing,
    assembly_loop,
    testing_loop,
    initial_calibration_loop,
    flight_testing_loop,
    performance_tuning_loop,
    training_loop,
    final_steps
])

# Define dependencies (order of execution)
root.order.add_edge(component_sourcing, assembly_loop)
root.order.add_edge(assembly_loop, testing_loop)
root.order.add_edge(testing_loop, initial_calibration_loop)
root.order.add_edge(initial_calibration_loop, flight_testing_loop)
root.order.add_edge(flight_testing_loop, performance_tuning_loop)
root.order.add_edge(performance_tuning_loop, training_loop)
root.order.add_edge(training_loop, final_steps)

# Print the root model
print(root)