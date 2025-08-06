import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for component testing
loop = OperatorPOWL(operator=Operator.LOOP, children=[source_parts, component_test])

# Define the XOR for firmware installation and calibration
xor = OperatorPOWL(operator=Operator.XOR, children=[install_firmware, calibrate_sensors])

# Define the partial order with the defined activities
root = StrictPartialOrder(nodes=[gather_specs, adapt_design, loop, xor, stress_test, flight_simulate, validate_battery, check_accuracy, package_units, create_manuals, ship_drones, collect_feedback])
root.order.add_edge(gather_specs, adapt_design)
root.order.add_edge(adapt_design, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, stress_test)
root.order.add_edge(stress_test, flight_simulate)
root.order.add_edge(flight_simulate, validate_battery)
root.order.add_edge(validate_battery, check_accuracy)
root.order.add_edge(check_accuracy, package_units)
root.order.add_edge(package_units, create_manuals)
root.order.add_edge(create_manuals, ship_drones)
root.order.add_edge(ship_drones, collect_feedback)