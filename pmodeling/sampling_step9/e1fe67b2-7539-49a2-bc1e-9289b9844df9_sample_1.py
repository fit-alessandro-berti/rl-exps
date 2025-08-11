import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define silent transitions
skip = SilentTransition()

# Define exclusive choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[component_test, skip])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[flight_calibrate, skip])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[enviro_test, skip])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[remote_pair, skip])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, skip])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[package_unit, skip])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[register_drone, skip])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[client_train, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[gather_specs, design_custom, source_parts, firmware_load, mechanical_fit, cable_routing, sensor_align, loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])
root.order.add_edge(gather_specs, design_custom)
root.order.add_edge(design_custom, source_parts)
root.order.add_edge(source_parts, firmware_load)
root.order.add_edge(firmware_load, mechanical_fit)
root.order.add_edge(mechanical_fit, cable_routing)
root.order.add_edge(cable_routing, sensor_align)
root.order.add_edge(sensor_align, component_test)
root.order.add_edge(component_test, loop1)
root.order.add_edge(flight_calibrate, loop2)
root.order.add_edge(enviro_test, loop3)
root.order.add_edge(remote_pair, loop4)
root.order.add_edge(quality_check, loop5)
root.order.add_edge(package_unit, loop6)
root.order.add_edge(register_drone, loop7)
root.order.add_edge(client_train, loop8)

# Add edges between the loop nodes
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)

# Add edges from the loop nodes to the final activities
root.order.add_edge(loop1, software_sync)
root.order.add_edge(loop2, flight_calibrate)
root.order.add_edge(loop3, enviro_test)
root.order.add_edge(loop4, remote_pair)
root.order.add_edge(loop5, quality_check)
root.order.add_edge(loop6, package_unit)
root.order.add_edge(loop7, register_drone)
root.order.add_edge(loop8, client_train)