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

# Define the process
gather_specs_to_design_custom = OperatorPOWL(operator=Operator.XOR, children=[gather_specs, design_custom])
design_custom_to_source_parts = OperatorPOWL(operator=Operator.XOR, children=[design_custom, source_parts])
source_parts_to_firmware_load = OperatorPOWL(operator=Operator.XOR, children=[source_parts, firmware_load])
firmware_load_to_mechanical_fit = OperatorPOWL(operator=Operator.XOR, children=[firmware_load, mechanical_fit])
mechanical_fit_to_cable_routing = OperatorPOWL(operator=Operator.XOR, children=[mechanical_fit, cable_routing])
cable_routing_to_sensor_align = OperatorPOWL(operator=Operator.XOR, children=[cable_routing, sensor_align])
sensor_align_to_component_test = OperatorPOWL(operator=Operator.XOR, children=[sensor_align, component_test])
component_test_to_software_sync = OperatorPOWL(operator=Operator.XOR, children=[component_test, software_sync])
software_sync_to_flight_calibrate = OperatorPOWL(operator=Operator.XOR, children=[software_sync, flight_calibrate])
flight_calibrate_to_enviro_test = OperatorPOWL(operator=Operator.XOR, children=[flight_calibrate, enviro_test])
enviro_test_to_remote_pair = OperatorPOWL(operator=Operator.XOR, children=[enviro_test, remote_pair])
remote_pair_to_quality_check = OperatorPOWL(operator=Operator.XOR, children=[remote_pair, quality_check])
quality_check_to_package_unit = OperatorPOWL(operator=Operator.XOR, children=[quality_check, package_unit])
package_unit_to_register_drone = OperatorPOWL(operator=Operator.XOR, children=[package_unit, register_drone])
register_drone_to_client_train = OperatorPOWL(operator=Operator.XOR, children=[register_drone, client_train])

# Define the partial order
root = StrictPartialOrder(nodes=[
    gather_specs_to_design_custom,
    design_custom_to_source_parts,
    source_parts_to_firmware_load,
    firmware_load_to_mechanical_fit,
    mechanical_fit_to_cable_routing,
    cable_routing_to_sensor_align,
    sensor_align_to_component_test,
    component_test_to_software_sync,
    software_sync_to_flight_calibrate,
    flight_calibrate_to_enviro_test,
    enviro_test_to_remote_pair,
    remote_pair_to_quality_check,
    quality_check_to_package_unit,
    package_unit_to_register_drone,
    register_drone_to_client_train
])

# Define the dependencies
root.order.add_edge(gather_specs_to_design_custom, design_custom_to_source_parts)
root.order.add_edge(design_custom_to_source_parts, source_parts_to_firmware_load)
root.order.add_edge(source_parts_to_firmware_load, firmware_load_to_mechanical_fit)
root.order.add_edge(firmware_load_to_mechanical_fit, mechanical_fit_to_cable_routing)
root.order.add_edge(mechanical_fit_to_cable_routing, cable_routing_to_sensor_align)
root.order.add_edge(cable_routing_to_sensor_align, sensor_align_to_component_test)
root.order.add_edge(sensor_align_to_component_test, component_test_to_software_sync)
root.order.add_edge(component_test_to_software_sync, software_sync_to_flight_calibrate)
root.order.add_edge(software_sync_to_flight_calibrate, flight_calibrate_to_enviro_test)
root.order.add_edge(flight_calibrate_to_enviro_test, enviro_test_to_remote_pair)
root.order.add_edge(enviro_test_to_remote_pair, remote_pair_to_quality_check)
root.order.add_edge(remote_pair_to_quality_check, quality_check_to_package_unit)
root.order.add_edge(quality_check_to_package_unit, package_unit_to_register_drone)
root.order.add_edge(package_unit_to_register_drone, register_drone_to_client_train)

print(root)