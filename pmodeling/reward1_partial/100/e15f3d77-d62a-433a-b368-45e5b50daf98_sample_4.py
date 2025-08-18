import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
gather_specs = Transition(label='Gather Specs')
adapt_design = Transition(label='Adapt Design')
source_parts = Transition(label='Source Parts')
component_test = Transition(label='Component Test')
assemble_frame = Transition(label='Assemble Frame')
install_firmware = Transition(label='Install Firmware')
calibrate_sensors = Transition(label='Calibrate Sensors')
stress_test = Transition(label='Stress Test')
flight_simulate = Transition(label='Flight Simulate')
validate_battery = Transition(label='Validate Battery')
check_accuracy = Transition(label='Check Accuracy')
package_units = Transition(label='Package Units')
create_manuals = Transition(label='Create Manuals')
ship_drones = Transition(label='Ship Drones')
collect_feedback = Transition(label='Collect Feedback')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop_stress_test = OperatorPOWL(operator=Operator.LOOP, children=[stress_test])
loop_flight_simulate = OperatorPOWL(operator=Operator.LOOP, children=[flight_simulate])
xor_test_validation = OperatorPOWL(operator=Operator.XOR, children=[validate_battery, check_accuracy])
xor_manuals = OperatorPOWL(operator=Operator.XOR, children=[create_manuals, skip])
xor_package_ship = OperatorPOWL(operator=Operator.XOR, children=[package_units, ship_drones])
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[collect_feedback, skip])

# Construct the strict partial order
root = StrictPartialOrder(nodes=[gather_specs, adapt_design, source_parts, component_test, assemble_frame, install_firmware, calibrate_sensors, loop_stress_test, loop_flight_simulate, xor_test_validation, xor_manuals, xor_package_ship, xor_feedback])
root.order.add_edge(gather_specs, adapt_design)
root.order.add_edge(adapt_design, source_parts)
root.order.add_edge(source_parts, component_test)
root.order.add_edge(component_test, assemble_frame)
root.order.add_edge(assemble_frame, install_firmware)
root.order.add_edge(install_firmware, calibrate_sensors)
root.order.add_edge(calibrate_sensors, loop_stress_test)
root.order.add_edge(loop_stress_test, loop_flight_simulate)
root.order.add_edge(loop_flight_simulate, xor_test_validation)
root.order.add_edge(xor_test_validation, xor_manuals)
root.order.add_edge(xor_manuals, xor_package_ship)
root.order.add_edge(xor_package_ship, xor_feedback)

# Print the root model
print(root)