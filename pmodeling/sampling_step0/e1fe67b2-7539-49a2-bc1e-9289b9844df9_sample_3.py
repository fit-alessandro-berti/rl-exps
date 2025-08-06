import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transition (skip)
skip = SilentTransition()

# Define the loop (Mechanical Fit, Cable Routing, Sensor Align)
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[mechanical_fit, cable_routing, sensor_align])

# Define the loop (Component Test, Software Sync, Flight Calibrate, Enviro Test)
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[component_test, software_sync, flight_calibrate, enviro_test])

# Define the XOR (Remote Pair, Quality Check)
xor = OperatorPOWL(operator=Operator.XOR, children=[remote_pair, quality_check])

# Define the root POWL model
root = StrictPartialOrder(nodes=[gather_specs, design_custom, source_parts, firmware_load, loop1, loop2, xor, package_unit, register_drone, client_train])
root.order.add_edge(gather_specs, design_custom)
root.order.add_edge(design_custom, source_parts)
root.order.add_edge(source_parts, firmware_load)
root.order.add_edge(firmware_load, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor)
root.order.add_edge(xor, package_unit)
root.order.add_edge(package_unit, register_drone)
root.order.add_edge(register_drone, client_train)

print(root)