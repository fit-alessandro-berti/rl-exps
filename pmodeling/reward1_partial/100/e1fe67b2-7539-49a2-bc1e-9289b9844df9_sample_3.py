import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define silent transitions for loops
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[gather_specs, design_custom])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[source_parts, firmware_load, mechanical_fit, cable_routing, sensor_align, component_test, software_sync, flight_calibrate, enviro_test])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[remote_pair, quality_check, package_unit, register_drone, client_train])

# Define the root node as a partial order with dependencies
root = StrictPartialOrder(nodes=[loop1, loop2, loop3])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)

# Print the root node to verify the model
print(root)