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

gather_specs_to_adapt_design = OperatorPOWL(operator=Operator.XOR, children=[gather_specs, adapt_design])
adapt_design_to_source_parts = OperatorPOWL(operator=Operator.XOR, children=[adapt_design, source_parts])
source_parts_to_component_test = OperatorPOWL(operator=Operator.XOR, children=[source_parts, component_test])
component_test_to_assemble_frame = OperatorPOWL(operator=Operator.XOR, children=[component_test, assemble_frame])
assemble_frame_to_install_firmware = OperatorPOWL(operator=Operator.XOR, children=[assemble_frame, install_firmware])
install_firmware_to_calibrate_sensors = OperatorPOWL(operator=Operator.XOR, children=[install_firmware, calibrate_sensors])
calibrate_sensors_to_stress_test = OperatorPOWL(operator=Operator.XOR, children=[calibrate_sensors, stress_test])
stress_test_to_flight_simulate = OperatorPOWL(operator=Operator.XOR, children=[stress_test, flight_simulate])
flight_simulate_to_validate_battery = OperatorPOWL(operator=Operator.XOR, children=[flight_simulate, validate_battery])
validate_battery_to_check_accuracy = OperatorPOWL(operator=Operator.XOR, children=[validate_battery, check_accuracy])
check_accuracy_to_package_units = OperatorPOWL(operator=Operator.XOR, children=[check_accuracy, package_units])
package_units_to_create_manuals = OperatorPOWL(operator=Operator.XOR, children=[package_units, create_manuals])
create_manuals_to_ship_drones = OperatorPOWL(operator=Operator.XOR, children=[create_manuals, ship_drones])
ship_drones_to_collect_feedback = OperatorPOWL(operator=Operator.XOR, children=[ship_drones, collect_feedback])

root = StrictPartialOrder(nodes=[
    gather_specs_to_adapt_design,
    adapt_design_to_source_parts,
    source_parts_to_component_test,
    component_test_to_assemble_frame,
    assemble_frame_to_install_firmware,
    install_firmware_to_calibrate_sensors,
    calibrate_sensors_to_stress_test,
    stress_test_to_flight_simulate,
    flight_simulate_to_validate_battery,
    validate_battery_to_check_accuracy,
    check_accuracy_to_package_units,
    package_units_to_create_manuals,
    create_manuals_to_ship_drones,
    ship_drones_to_collect_feedback
])

root.order.add_edge(gather_specs_to_adapt_design, adapt_design_to_source_parts)
root.order.add_edge(adapt_design_to_source_parts, source_parts_to_component_test)
root.order.add_edge(source_parts_to_component_test, component_test_to_assemble_frame)
root.order.add_edge(component_test_to_assemble_frame, assemble_frame_to_install_firmware)
root.order.add_edge(assemble_frame_to_install_firmware, install_firmware_to_calibrate_sensors)
root.order.add_edge(install_firmware_to_calibrate_sensors, calibrate_sensors_to_stress_test)
root.order.add_edge(calibrate_sensors_to_stress_test, stress_test_to_flight_simulate)
root.order.add_edge(stress_test_to_flight_simulate, flight_simulate_to_validate_battery)
root.order.add_edge(flight_simulate_to_validate_battery, validate_battery_to_check_accuracy)
root.order.add_edge(validate_battery_to_check_accuracy, check_accuracy_to_package_units)
root.order.add_edge(check_accuracy_to_package_units, package_units_to_create_manuals)
root.order.add_edge(package_units_to_create_manuals, create_manuals_to_ship_drones)
root.order.add_edge(create_manuals_to_ship_drones, ship_drones_to_collect_feedback)

root