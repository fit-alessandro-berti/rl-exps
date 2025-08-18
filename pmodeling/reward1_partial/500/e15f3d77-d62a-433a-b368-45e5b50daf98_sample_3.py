import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
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

# Define loops and choices
# Gather Specs, Adapt Design, Source Parts, Component Test, Assemble Frame, Install Firmware, Calibrate Sensors
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[gather_specs, adapt_design, source_parts, component_test, assemble_frame, install_firmware, calibrate_sensors])

# Stress Test, Flight Simulate, Validate Battery, Check Accuracy
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[stress_test, flight_simulate, validate_battery, check_accuracy])

# Package Units, Create Manuals, Ship Drones
xor1 = OperatorPOWL(operator=Operator.XOR, children=[package_units, create_manuals, ship_drones])

# Collect Feedback
skip = SilentTransition()
xor2 = OperatorPOWL(operator=Operator.XOR, children=[xor1, skip])

# Define the root node
root = StrictPartialOrder(nodes=[loop1, loop2, xor2])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor2)

# Print the root node
print(root)