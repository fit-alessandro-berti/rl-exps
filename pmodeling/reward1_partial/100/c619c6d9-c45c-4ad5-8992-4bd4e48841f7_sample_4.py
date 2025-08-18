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

# Define silent transitions for empty labels
skip = SilentTransition()

# Define loop for flight testing
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_testing, data_analyze, regulation_check, quality_inspect])

# Define XOR for payload configuration and assembly setup
payload_xor = OperatorPOWL(operator=Operator.XOR, children=[payload_configure, assembly_setup])

# Define partial order
root = StrictPartialOrder(nodes=[design_consult, component_sourcing, sensor_calibrate, firmware_integrate, payload_xor, flight_loop, wiring_connect, chassis_build, software_load, packaging_prep, logistics_plan, client_review])

# Define dependencies
root.order.add_edge(design_consult, component_sourcing)
root.order.add_edge(component_sourcing, sensor_calibrate)
root.order.add_edge(sensor_calibrate, firmware_integrate)
root.order.add_edge(firmware_integrate, payload_xor)
root.order.add_edge(payload_xor, flight_loop)
root.order.add_edge(flight_loop, wiring_connect)
root.order.add_edge(wiring_connect, chassis_build)
root.order.add_edge(chassis_build, software_load)
root.order.add_edge(software_load, packaging_prep)
root.order.add_edge(packaging_prep, logistics_plan)
root.order.add_edge(logistics_plan, client_review)

print(root)