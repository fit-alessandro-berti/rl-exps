from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL nodes for each activity
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

# Define the control-flow operators for choice and loop structures
xor_choice = OperatorPOWL(operator=Operator.XOR, children=[stress_test, flight_simulate])
loop = OperatorPOWL(operator=Operator.LOOP, children=[validate_battery, check_accuracy])

# Construct the POWL model
root = StrictPartialOrder(nodes=[gather_specs, adapt_design, source_parts, component_test, assemble_frame, install_firmware, calibrate_sensors, xor_choice, package_units, create_manuals, ship_drones, collect_feedback, loop])
root.order.add_edge(gather_specs, adapt_design)
root.order.add_edge(adapt_design, source_parts)
root.order.add_edge(source_parts, component_test)
root.order.add_edge(component_test, assemble_frame)
root.order.add_edge(assemble_frame, install_firmware)
root.order.add_edge(install_firmware, calibrate_sensors)
root.order.add_edge(calibrate_sensors, xor_choice)
root.order.add_edge(xor_choice, package_units)
root.order.add_edge(package_units, create_manuals)
root.order.add_edge(create_manuals, ship_drones)
root.order.add_edge(ship_drones, collect_feedback)
root.order.add_edge(collect_feedback, loop)
root.order.add_edge(loop, validate_battery)
root.order.add_edge(loop, check_accuracy)

print(root)