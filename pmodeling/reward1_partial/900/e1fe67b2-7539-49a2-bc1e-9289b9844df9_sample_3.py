import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Gather_Specs = Transition(label='Gather Specs')
Design_Custom = Transition(label='Design Custom')
Source_Parts = Transition(label='Source Parts')
Firmware_Load = Transition(label='Firmware Load')
Mechanical_Fit = Transition(label='Mechanical Fit')
Cable_Routing = Transition(label='Cable Routing')
Sensor_Align = Transition(label='Sensor Align')
Component_Test = Transition(label='Component Test')
Software_Sync = Transition(label='Software Sync')
Flight_Calibrate = Transition(label='Flight Calibrate')
Enviro_Test = Transition(label='Enviro Test')
Remote_Pair = Transition(label='Remote Pair')
Quality_Check = Transition(label='Quality Check')
Package_Unit = Transition(label='Package Unit')
Register_Drone = Transition(label='Register Drone')
Client_Train = Transition(label='Client Train')

# Define the workflow
gather_specs = OperatorPOWL(operator=Operator.XOR, children=[Gather_Specs, Design_Custom])
design_custom = OperatorPOWL(operator=Operator.XOR, children=[Source_Parts, Firmware_Load])
source_parts = OperatorPOWL(operator=Operator.XOR, children=[Mechanical_Fit, Cable_Routing])
firmware_load = OperatorPOWL(operator=Operator.XOR, children=[Sensor_Align, Component_Test])
mechanical_fit = OperatorPOWL(operator=Operator.XOR, children=[Software_Sync, Flight_Calibrate])
cable_routing = OperatorPOWL(operator=Operator.XOR, children=[Enviro_Test, Remote_Pair])
sensor_align = OperatorPOWL(operator=Operator.XOR, children=[Quality_Check, Package_Unit])
software_sync = OperatorPOWL(operator=Operator.XOR, children=[Register_Drone, Client_Train])
flight_calibrate = OperatorPOWL(operator=Operator.XOR, children=[Enviro_Test, Remote_Pair])
enviro_test = OperatorPOWL(operator=Operator.XOR, children=[Quality_Check, Package_Unit])
remote_pair = OperatorPOWL(operator=Operator.XOR, children=[Register_Drone, Client_Train])
quality_check = OperatorPOWL(operator=Operator.XOR, children=[Package_Unit, Client_Train])
package_unit = OperatorPOWL(operator=Operator.XOR, children=[Register_Drone, Client_Train])
register_drone = OperatorPOWL(operator=Operator.XOR, children=[Client_Train, Client_Train])
client_train = OperatorPOWL(operator=Operator.XOR, children=[Client_Train, Client_Train])

# Define the root node
root = StrictPartialOrder(nodes=[gather_specs, design_custom, source_parts, firmware_load, mechanical_fit, cable_routing, sensor_align, software_sync, flight_calibrate, enviro_test, remote_pair, quality_check, package_unit, register_drone, client_train])

# Define the partial order
root.order.add_edge(gather_specs, design_custom)
root.order.add_edge(design_custom, source_parts)
root.order.add_edge(source_parts, firmware_load)
root.order.add_edge(firmware_load, mechanical_fit)
root.order.add_edge(mechanical_fit, cable_routing)
root.order.add_edge(cable_routing, sensor_align)
root.order.add_edge(sensor_align, software_sync)
root.order.add_edge(software_sync, flight_calibrate)
root.order.add_edge(flight_calibrate, enviro_test)
root.order.add_edge(enviro_test, remote_pair)
root.order.add_edge(remote_pair, quality_check)
root.order.add_edge(quality_check, package_unit)
root.order.add_edge(package_unit, register_drone)
root.order.add_edge(register_drone, client_train)

print(root)