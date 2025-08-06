import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[source_parts, adapt_design])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[component_test, assemble_frame])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[install_firmware, calibrate_sensors])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[stress_test, flight_simulate])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[validate_battery, check_accuracy])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[package_units, create_manuals])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[ship_drones, collect_feedback])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)
root.order.add_edge(loop, xor7)