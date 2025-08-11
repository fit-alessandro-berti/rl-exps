import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the loops and choices
loop_test = OperatorPOWL(operator=Operator.LOOP, children=[component_test, skip])
loop_calibration = OperatorPOWL(operator=Operator.LOOP, children=[calibrate_sensors, skip])
loop_flight_simulate = OperatorPOWL(operator=Operator.LOOP, children=[flight_simulate, skip])

xor_stress_test = OperatorPOWL(operator=Operator.XOR, children=[stress_test, skip])
xor_accuracy_check = OperatorPOWL(operator=Operator.XOR, children=[validate_battery, check_accuracy])

loop_collect_feedback = OperatorPOWL(operator=Operator.LOOP, children=[collect_feedback, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[gather_specs, adapt_design, source_parts, loop_test, assemble_frame, install_firmware, loop_calibration, loop_flight_simulate, xor_stress_test, xor_accuracy_check, package_units, create_manuals, ship_drones, loop_collect_feedback])
root.order.add_edge(gather_specs, adapt_design)
root.order.add_edge(adapt_design, source_parts)
root.order.add_edge(source_parts, loop_test)
root.order.add_edge(loop_test, assemble_frame)
root.order.add_edge(assemble_frame, install_firmware)
root.order.add_edge(install_firmware, loop_calibration)
root.order.add_edge(loop_calibration, loop_flight_simulate)
root.order.add_edge(loop_flight_simulate, xor_stress_test)
root.order.add_edge(xor_stress_test, package_units)
root.order.add_edge(package_units, create_manuals)
root.order.add_edge(create_manuals, ship_drones)
root.order.add_edge(ship_drones, loop_collect_feedback)
root.order.add_edge(loop_collect_feedback, collect_feedback)

print(root)