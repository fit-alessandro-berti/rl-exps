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

gather_specs_test = OperatorPOWL(operator=Operator.XOR, children=[gather_specs, skip])
adapt_design_test = OperatorPOWL(operator=Operator.XOR, children=[adapt_design, skip])
source_parts_test = OperatorPOWL(operator=Operator.XOR, children=[source_parts, skip])
component_test_assemble = OperatorPOWL(operator=Operator.XOR, children=[component_test, assemble_frame])
assemble_firmware_calibrate = OperatorPOWL(operator=Operator.XOR, children=[assemble_frame, install_firmware, calibrate_sensors])
stress_test_flight_simulate = OperatorPOWL(operator=Operator.XOR, children=[stress_test, flight_simulate])
validate_battery_check_accuracy = OperatorPOWL(operator=Operator.XOR, children=[validate_battery, check_accuracy])
package_units_create_manuals = OperatorPOWL(operator=Operator.XOR, children=[package_units, create_manuals])
ship_drones_collect_feedback = OperatorPOWL(operator=Operator.XOR, children=[ship_drones, collect_feedback])

root = StrictPartialOrder(nodes=[
    gather_specs_test,
    adapt_design_test,
    source_parts_test,
    component_test_assemble,
    assemble_firmware_calibrate,
    stress_test_flight_simulate,
    validate_battery_check_accuracy,
    package_units_create_manuals,
    ship_drones_collect_feedback
])
root.order.add_edge(gather_specs_test, adapt_design_test)
root.order.add_edge(adapt_design_test, source_parts_test)
root.order.add_edge(source_parts_test, component_test_assemble)
root.order.add_edge(component_test_assemble, assemble_firmware_calibrate)
root.order.add_edge(assemble_firmware_calibrate, stress_test_flight_simulate)
root.order.add_edge(stress_test_flight_simulate, validate_battery_check_accuracy)
root.order.add_edge(validate_battery_check_accuracy, package_units_create_manuals)
root.order.add_edge(package_units_create_manuals, ship_drones_collect_feedback)