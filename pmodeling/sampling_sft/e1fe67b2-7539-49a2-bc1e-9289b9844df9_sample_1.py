import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
gather_specs    = Transition(label='Gather Specs')
design_custom   = Transition(label='Design Custom')
source_parts    = Transition(label='Source Parts')
firmware_load   = Transition(label='Firmware Load')
mechanical_fit  = Transition(label='Mechanical Fit')
cable_routing   = Transition(label='Cable Routing')
sensor_align    = Transition(label='Sensor Align')
component_test  = Transition(label='Component Test')
software_sync   = Transition(label='Software Sync')
flight_calibrate= Transition(label='Flight Calibrate')
enviro_test     = Transition(label='Enviro Test')
remote_pair     = Transition(label='Remote Pair')
quality_check   = Transition(label='Quality Check')
package_unit    = Transition(label='Package Unit')
register_drone  = Transition(label='Register Drone')
client_train    = Transition(label='Client Train')

# Build the loop body: Flight Calibrate -> Enviro Test -> Remote Pair -> Quality Check
body = StrictPartialOrder(nodes=[flight_calibrate, enviro_test, remote_pair, quality_check])
body.order.add_edge(flight_calibrate, enviro_test)
body.order.add_edge(enviro_test, remote_pair)
body.order.add_edge(remote_pair, quality_check)

# Loop: do Software Sync, then either exit or execute the loop body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[software_sync, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    gather_specs, design_custom, source_parts,
    firmware_load, mechanical_fit, cable_routing, sensor_align,
    component_test, loop, package_unit, register_drone, client_train
])

# Define the control-flow dependencies
root.order.add_edge(gather_specs, design_custom)
root.order.add_edge(design_custom, source_parts)
root.order.add_edge(source_parts, firmware_load)
root.order.add_edge(firmware_load, mechanical_fit)
root.order.add_edge(mechanical_fit, cable_routing)
root.order.add_edge(cable_routing, sensor_align)
root.order.add_edge(sensor_align, component_test)
root.order.add_edge(component_test, loop)
root.order.add_edge(loop, package_unit)
root.order.add_edge(package_unit, register_drone)
root.order.add_edge(register_drone, client_train)

print(root)