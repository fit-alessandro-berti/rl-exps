import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
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

# Build the partial order
root = StrictPartialOrder(nodes=[
    gather_specs, adapt_design, source_parts, component_test,
    assemble_frame, install_firmware, calibrate_sensors,
    stress_test, flight_simulate, validate_battery,
    check_accuracy, package_units, create_manuals,
    ship_drones, collect_feedback
])

# Define the control-flow dependencies
root.order.add_edge(gather_specs, adapt_design)
root.order.add_edge(adapt_design, source_parts)
root.order.add_edge(source_parts, component_test)

# After component testing, assemble and install firmware in parallel
root.order.add_edge(component_test, assemble_frame)
root.order.add_edge(component_test, install_firmware)

# After assembly and firmware, calibrate sensors
root.order.add_edge(assemble_frame, calibrate_sensors)
root.order.add_edge(install_firmware, calibrate_sensors)

# After calibration, run stress and flight tests in parallel
root.order.add_edge(calibrate_sensors, stress_test)
root.order.add_edge(calibrate_sensors, flight_simulate)

# Both tests then validate battery and check accuracy in parallel
root.order.add_edge(stress_test, validate_battery)
root.order.add_edge(flight_simulate, validate_battery)
root.order.add_edge(stress_test, check_accuracy)
root.order.add_edge(flight_simulate, check_accuracy)

# After validation, package units and create manuals in parallel
root.order.add_edge(validate_battery, package_units)
root.order.add_edge(check_accuracy, package_units)
root.order.add_edge(validate_battery, create_manuals)
root.order.add_edge(check_accuracy, create_manuals)

# Finally, ship drones and collect feedback in parallel
root.order.add_edge(package_units, ship_drones)
root.order.add_edge(create_manuals, ship_drones)
root.order.add_edge(package_units, collect_feedback)
root.order.add_edge(create_manuals, collect_feedback)

# Print the root model for verification
print(root)