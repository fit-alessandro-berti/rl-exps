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

gather_specs_test = OperatorPOWL(operator=Operator.XOR, children=[gather_specs, skip])
adapt_design_test = OperatorPOWL(operator=Operator.XOR, children=[adapt_design, skip])
source_parts_test = OperatorPOWL(operator=Operator.XOR, children=[source_parts, skip])
component_test_test = OperatorPOWL(operator=Operator.XOR, children=[component_test, skip])
assemble_frame_test = OperatorPOWL(operator=Operator.XOR, children=[assemble_frame, skip])
install_firmware_test = OperatorPOWL(operator=Operator.XOR, children=[install_firmware, skip])
calibrate_sensors_test = OperatorPOWL(operator=Operator.XOR, children=[calibrate_sensors, skip])
stress_test_test = OperatorPOWL(operator=Operator.XOR, children=[stress_test, skip])
flight_simulate_test = OperatorPOWL(operator=Operator.XOR, children=[flight_simulate, skip])
validate_battery_test = OperatorPOWL(operator=Operator.XOR, children=[validate_battery, skip])
check_accuracy_test = OperatorPOWL(operator=Operator.XOR, children=[check_accuracy, skip])
package_units_test = OperatorPOWL(operator=Operator.XOR, children=[package_units, skip])
create_manuals_test = OperatorPOWL(operator=Operator.XOR, children=[create_manuals, skip])
ship_drones_test = OperatorPOWL(operator=Operator.XOR, children=[ship_drones, skip])
collect_feedback_test = OperatorPOWL(operator=Operator.XOR, children=[collect_feedback, skip])

root = StrictPartialOrder(nodes=[
    gather_specs_test,
    adapt_design_test,
    source_parts_test,
    component_test_test,
    assemble_frame_test,
    install_firmware_test,
    calibrate_sensors_test,
    stress_test_test,
    flight_simulate_test,
    validate_battery_test,
    check_accuracy_test,
    package_units_test,
    create_manuals_test,
    ship_drones_test,
    collect_feedback_test
])

root.order.add_edge(gather_specs_test, adapt_design_test)
root.order.add_edge(adapt_design_test, source_parts_test)
root.order.add_edge(source_parts_test, component_test_test)
root.order.add_edge(component_test_test, assemble_frame_test)
root.order.add_edge(assemble_frame_test, install_firmware_test)
root.order.add_edge(install_firmware_test, calibrate_sensors_test)
root.order.add_edge(calibrate_sensors_test, stress_test_test)
root.order.add_edge(stress_test_test, flight_simulate_test)
root.order.add_edge(flight_simulate_test, validate_battery_test)
root.order.add_edge(validate_battery_test, check_accuracy_test)
root.order.add_edge(check_accuracy_test, package_units_test)
root.order.add_edge(package_units_test, create_manuals_test)
root.order.add_edge(create_manuals_test, ship_drones_test)
root.order.add_edge(ship_drones_test, collect_feedback_test)