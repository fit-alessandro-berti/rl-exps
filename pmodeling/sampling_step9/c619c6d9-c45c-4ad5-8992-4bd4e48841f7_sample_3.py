import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_flight_testing = OperatorPOWL(operator=Operator.LOOP, children=[flight_testing])
loop_quality_inspect = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect])
loop_logistics_plan = OperatorPOWL(operator=Operator.LOOP, children=[logistics_plan])

# Define exclusive choice nodes
xor_flight_testing = OperatorPOWL(operator=Operator.XOR, children=[flight_testing, skip])
xor_logistics_plan = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    design_consult, component_sourcing, sensor_calibrate, firmware_integrate, payload_configure,
    assembly_setup, wiring_connect, chassis_build, software_load,
    loop_flight_testing, loop_quality_inspect, loop_logistics_plan,
    xor_flight_testing, xor_logistics_plan,
    data_analyze, regulation_check, quality_inspect, packaging_prep, logistics_plan, client_review
])

# Define dependencies between nodes
root.order.add_edge(design_consult, component_sourcing)
root.order.add_edge(component_sourcing, sensor_calibrate)
root.order.add_edge(sensor_calibrate, firmware_integrate)
root.order.add_edge(firmware_integrate, payload_configure)
root.order.add_edge(payload_configure, assembly_setup)
root.order.add_edge(assembly_setup, wiring_connect)
root.order.add_edge(wiring_connect, chassis_build)
root.order.add_edge(chassis_build, software_load)
root.order.add_edge(software_load, loop_flight_testing)
root.order.add_edge(loop_flight_testing, xor_flight_testing)
root.order.add_edge(xor_flight_testing, data_analyze)
root.order.add_edge(data_analyze, regulation_check)
root.order.add_edge(regulation_check, loop_quality_inspect)
root.order.add_edge(loop_quality_inspect, xor_logistics_plan)
root.order.add_edge(xor_logistics_plan, packaging_prep)
root.order.add_edge(packaging_prep, logistics_plan)
root.order.add_edge(logistics_plan, client_review)

# Print the root POWL model
print(root)