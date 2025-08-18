import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
design_consult = Transition(label='Design Consult')
component_sourcing = Transition(label='Component Sourcing')
sensor_calibrate = Transition(label='Sensor Calibrate')
firmware_integrate = Transition(label='Firmware Integrate')
payload_configure = Transition(label='Payload Configure')
assembly_setup = Transition(label='Assembly Setup')
wiring_connect = Transition(label='Wiring Connect')
chassis_build = Transition(label='Chassis Build')
software_load = Transition(label='Software Load')
flight_testing = Transition(label='Flight Testing')
data_analyze = Transition(label='Data Analyze')
regulation_check = Transition(label='Regulation Check')
quality_inspect = Transition(label='Quality Inspect')
packaging_prep = Transition(label='Packaging Prep')
logistics_plan = Transition(label='Logistics Plan')
client_review = Transition(label='Client Review')

# Define the process flow
design_consult_node = StrictPartialOrder(nodes=[design_consult])
component_sourcing_node = StrictPartialOrder(nodes=[component_sourcing])
sensor_calibrate_node = StrictPartialOrder(nodes=[sensor_calibrate])
firmware_integrate_node = StrictPartialOrder(nodes=[firmware_integrate])
payload_configure_node = StrictPartialOrder(nodes=[payload_configure])
assembly_setup_node = StrictPartialOrder(nodes=[assembly_setup])
wiring_connect_node = StrictPartialOrder(nodes=[wiring_connect])
chassis_build_node = StrictPartialOrder(nodes=[chassis_build])
software_load_node = StrictPartialOrder(nodes=[software_load])
flight_testing_node = StrictPartialOrder(nodes=[flight_testing])
data_analyze_node = StrictPartialOrder(nodes=[data_analyze])
regulation_check_node = StrictPartialOrder(nodes=[regulation_check])
quality_inspect_node = StrictPartialOrder(nodes=[quality_inspect])
packaging_prep_node = StrictPartialOrder(nodes=[packaging_prep])
logistics_plan_node = StrictPartialOrder(nodes=[logistics_plan])
client_review_node = StrictPartialOrder(nodes=[client_review])

# Define the dependencies
root = StrictPartialOrder(nodes=[
    design_consult_node,
    component_sourcing_node,
    sensor_calibrate_node,
    firmware_integrate_node,
    payload_configure_node,
    assembly_setup_node,
    wiring_connect_node,
    chassis_build_node,
    software_load_node,
    flight_testing_node,
    data_analyze_node,
    regulation_check_node,
    quality_inspect_node,
    packaging_prep_node,
    logistics_plan_node,
    client_review_node
])
root.order.add_edge(design_consult_node, component_sourcing_node)
root.order.add_edge(component_sourcing_node, sensor_calibrate_node)
root.order.add_edge(sensor_calibrate_node, firmware_integrate_node)
root.order.add_edge(firmware_integrate_node, payload_configure_node)
root.order.add_edge(payload_configure_node, assembly_setup_node)
root.order.add_edge(assembly_setup_node, wiring_connect_node)
root.order.add_edge(wiring_connect_node, chassis_build_node)
root.order.add_edge(chassis_build_node, software_load_node)
root.order.add_edge(software_load_node, flight_testing_node)
root.order.add_edge(flight_testing_node, data_analyze_node)
root.order.add_edge(data_analyze_node, regulation_check_node)
root.order.add_edge(regulation_check_node, quality_inspect_node)
root.order.add_edge(quality_inspect_node, packaging_prep_node)
root.order.add_edge(packaging_prep_node, logistics_plan_node)
root.order.add_edge(logistics_plan_node, client_review_node)