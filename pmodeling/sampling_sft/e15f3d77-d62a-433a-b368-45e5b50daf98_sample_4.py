import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
gather_specs    = Transition(label='Gather Specs')
adapt_design    = Transition(label='Adapt Design')
source_parts    = Transition(label='Source Parts')
component_test  = Transition(label='Component Test')
assemble_frame  = Transition(label='Assemble Frame')
install_firmware= Transition(label='Install Firmware')
calibrate_sensors=Transition(label='Calibrate Sensors')
stress_test     = Transition(label='Stress Test')
flight_simulate= Transition(label='Flight Simulate')
validate_battery= Transition(label='Validate Battery')
check_accuracy  = Transition(label='Check Accuracy')
package_units   = Transition(label='Package Units')
create_manuals  = Transition(label='Create Manuals')
ship_drones     = Transition(label='Ship Drones')
collect_feedback= Transition(label='Collect Feedback')

# Define the loop for iterative testing and validation
# Each iteration consists of Stress Test -> Flight Simulate -> Validate Battery -> Check Accuracy
test_loop_body = StrictPartialOrder(nodes=[stress_test, flight_simulate, validate_battery, check_accuracy])
test_loop_body.order.add_edge(stress_test, flight_simulate)
test_loop_body.order.add_edge(flight_simulate, validate_battery)
test_loop_body.order.add_edge(validate_battery, check_accuracy)

# The loop itself: repeat test_loop_body until exit
test_loop = OperatorPOWL(operator=Operator.LOOP, children=[test_loop_body, SilentTransition()])

# Build the overall assembly‐validation‐feedback‐ship‐collect loop
# Gather Specs -> Adapt Design -> Source Parts -> Component Test -> Assemble Frame
# -> Install Firmware -> Calibrate Sensors -> test_loop -> Package Units -> Create Manuals -> Ship Drones -> Collect Feedback
root = StrictPartialOrder(nodes=[
    gather_specs, adapt_design, source_parts, component_test, assemble_frame,
    install_firmware, calibrate_sensors, test_loop, package_units,
    create_manuals, ship_drones, collect_feedback
])
root.order.add_edge(gather_specs, adapt_design)
root.order.add_edge(adapt_design, source_parts)
root.order.add_edge(source_parts, component_test)
root.order.add_edge(component_test, assemble_frame)
root.order.add_edge(assemble_frame, install_firmware)
root.order.add_edge(install_firmware, calibrate_sensors)
root.order.add_edge(calibrate_sensors, test_loop)
root.order.add_edge(test_loop, package_units)
root.order.add_edge(package_units, create_manuals)
root.order.add_edge(create_manuals, ship_drones)
root.order.add_edge(ship_drones, collect_feedback)