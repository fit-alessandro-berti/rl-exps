from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop and choice operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[firmware_integrate, software_load, quality_inspect])
choice = OperatorPOWL(operator=Operator.XOR, children=[flight_testing, data_analyze])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[design_consult, component_sourcing, sensor_calibrate, loop, choice, payload_configure, assembly_setup, wiring_connect, chassis_build, packaging_prep, logistics_plan, client_review])

# Add edges to the partial order
root.order.add_edge(design_consult, component_sourcing)
root.order.add_edge(component_sourcing, sensor_calibrate)
root.order.add_edge(sensor_calibrate, firmware_integrate)
root.order.add_edge(firmware_integrate, software_load)
root.order.add_edge(software_load, quality_inspect)
root.order.add_edge(quality_inspect, flight_testing)
root.order.add_edge(flight_testing, data_analyze)
root.order.add_edge(data_analyze, regulation_check)
root.order.add_edge(regulation_check, quality_inspect)
root.order.add_edge(quality_inspect, payload_configure)
root.order.add_edge(payload_configure, assembly_setup)
root.order.add_edge(assembly_setup, wiring_connect)
root.order.add_edge(wiring_connect, chassis_build)
root.order.add_edge(chassis_build, packaging_prep)
root.order.add_edge(packaging_prep, logistics_plan)
root.order.add_edge(logistics_plan, client_review)