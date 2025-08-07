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

# Define the root POWL model
root = StrictPartialOrder(nodes=[gather_specs, design_custom, source_parts, firmware_load, mechanical_fit, cable_routing, sensor_align, component_test, software_sync, flight_calibrate, enviro_test, remote_pair, quality_check, package_unit, register_drone, client_train])

# Add dependencies if any (in this case, no dependencies are specified)
# root.order.add_edge(...)

# The root POWL model is now defined and can be used for further analysis or simulation