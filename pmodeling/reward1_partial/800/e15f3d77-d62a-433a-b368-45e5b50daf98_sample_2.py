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

gather_adapt = OperatorPOWL(operator=Operator.XOR, children=[gather_specs, adapt_design])
source_test = OperatorPOWL(operator=Operator.XOR, children=[source_parts, component_test])
assemble_firmware = OperatorPOWL(operator=Operator.XOR, children=[assemble_frame, install_firmware])
calibrate_stress = OperatorPOWL(operator=Operator.XOR, children=[calibrate_sensors, stress_test])
flight_validate = OperatorPOWL(operator=Operator.XOR, children=[flight_simulate, validate_battery])
accuracy_package = OperatorPOWL(operator=Operator.XOR, children=[check_accuracy, package_units])
manuals_ship = OperatorPOWL(operator=Operator.XOR, children=[create_manuals, ship_drones])
feedback_collect = OperatorPOWL(operator=Operator.XOR, children=[collect_feedback, skip])

root = StrictPartialOrder(nodes=[gather_adapt, source_test, assemble_firmware, calibrate_stress, flight_validate, accuracy_package, manuals_ship, feedback_collect])
root.order.add_edge(gather_adapt, source_test)
root.order.add_edge(source_test, assemble_firmware)
root.order.add_edge(assemble_firmware, calibrate_stress)
root.order.add_edge(calibrate_stress, flight_validate)
root.order.add_edge(flight_validate, accuracy_package)
root.order.add_edge(accuracy_package, manuals_ship)
root.order.add_edge(manuals_ship, feedback_collect)