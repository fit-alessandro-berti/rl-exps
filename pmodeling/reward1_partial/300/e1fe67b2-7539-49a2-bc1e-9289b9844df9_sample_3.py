import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
gather_specs = Transition(label='Gather Specs')
design_custom = Transition(label='Design Custom')
source_parts = Transition(label='Source Parts')
firmware_load = Transition(label='Firmware Load')
mechanical_fit = Transition(label='Mechanical Fit')
cable_routing = Transition(label='Cable Routing')
sensor_align = Transition(label='Sensor Align')
component_test = Transition(label='Component Test')
software_sync = Transition(label='Software Sync')
flight_calibrate = Transition(label='Flight Calibrate')
enviro_test = Transition(label='Enviro Test')
remote_pair = Transition(label='Remote Pair')
quality_check = Transition(label='Quality Check')
package_unit = Transition(label='Package Unit')
register_drone = Transition(label='Register Drone')
client_train = Transition(label='Client Train')

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[gather_specs, design_custom])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[source_parts, firmware_load])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[mechanical_fit, cable_routing])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[sensor_align, component_test])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[software_sync, flight_calibrate])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[enviro_test, remote_pair])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, package_unit])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[register_drone, client_train])

# Define the partial order
root = StrictPartialOrder(nodes=[xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8])

# Add dependencies between nodes
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)

# Print the POWL model
print(root)