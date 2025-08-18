import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

gather_specs_and_adapt_design = OperatorPOWL(operator=Operator.XOR, children=[gather_specs, adapt_design])
source_parts_and_component_test = OperatorPOWL(operator=Operator.XOR, children=[source_parts, component_test])
assemble_frame_and_install_firmware = OperatorPOWL(operator=Operator.XOR, children=[assemble_frame, install_firmware])
calibrate_sensors_and_stress_test = OperatorPOWL(operator=Operator.XOR, children=[calibrate_sensors, stress_test])
flight_simulate_and_validate_battery = OperatorPOWL(operator=Operator.XOR, children=[flight_simulate, validate_battery])
check_accuracy_and_package_units = OperatorPOWL(operator=Operator.XOR, children=[check_accuracy, package_units])
create_manuals_and_ship_drones = OperatorPOWL(operator=Operator.XOR, children=[create_manuals, ship_drones])
collect_feedback_and_end = OperatorPOWL(operator=Operator.XOR, children=[collect_feedback, skip])

root = StrictPartialOrder(nodes=[gather_specs_and_adapt_design, source_parts_and_component_test, assemble_frame_and_install_firmware, calibrate_sensors_and_stress_test, flight_simulate_and_validate_battery, check_accuracy_and_package_units, create_manuals_and_ship_drones, collect_feedback_and_end])
root.order.add_edge(gather_specs_and_adapt_design, source_parts_and_component_test)
root.order.add_edge(source_parts_and_component_test, assemble_frame_and_install_firmware)
root.order.add_edge(assemble_frame_and_install_firmware, calibrate_sensors_and_stress_test)
root.order.add_edge(calibrate_sensors_and_stress_test, flight_simulate_and_validate_battery)
root.order.add_edge(flight_simulate_and_validate_battery, check_accuracy_and_package_units)
root.order.add_edge(check_accuracy_and_package_units, create_manuals_and_ship_drones)
root.order.add_edge(create_manuals_and_ship_drones, collect_feedback_and_end)