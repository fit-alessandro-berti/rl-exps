import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
# Start with the initial design consultation
root = StrictPartialOrder(nodes=['Design Consult'])

# Add nodes for component sourcing
component_sourcing = Transition(label='Component Sourcing')
root.add_node(component_sourcing)
root.add_edge(root, component_sourcing)

# Add nodes for sensor calibration
sensor_calibrate = Transition(label='Sensor Calibrate')
root.add_node(sensor_calibrate)
root.add_edge(component_sourcing, sensor_calibrate)

# Add nodes for firmware integration
firmware_integrate = Transition(label='Firmware Integrate')
root.add_node(firmware_integrate)
root.add_edge(sensor_calibrate, firmware_integrate)

# Add nodes for payload configuration
payload_configure = Transition(label='Payload Configure')
root.add_node(payload_configure)
root.add_edge(firmware_integrate, payload_configure)

# Add nodes for assembly setup
assembly_setup = Transition(label='Assembly Setup')
root.add_node(assembly_setup)
root.add_edge(payload_configure, assembly_setup)

# Add nodes for wiring connection
wiring_connect = Transition(label='Wiring Connect')
root.add_node(wiring_connect)
root.add_edge(assembly_setup, wiring_connect)

# Add nodes for chassis building
chassis_build = Transition(label='Chassis Build')
root.add_node(chassis_build)
root.add_edge(wiring_connect, chassis_build)

# Add nodes for software loading
software_load = Transition(label='Software Load')
root.add_node(software_load)
root.add_edge(chassis_build, software_load)

# Add nodes for flight testing
flight_testing = Transition(label='Flight Testing')
root.add_node(flight_testing)
root.add_edge(software_load, flight_testing)

# Add nodes for data analysis
data_analyze = Transition(label='Data Analyze')
root.add_node(data_analyze)
root.add_edge(flight_testing, data_analyze)

# Add nodes for regulation check
regulation_check = Transition(label='Regulation Check')
root.add_node(regulation_check)
root.add_edge(data_analyze, regulation_check)

# Add nodes for quality inspection
quality_inspect = Transition(label='Quality Inspect')
root.add_node(quality_inspect)
root.add_edge(regulation_check, quality_inspect)

# Add nodes for packaging preparation
packaging_prep = Transition(label='Packaging Prep')
root.add_node(packaging_prep)
root.add_edge(quality_inspect, packaging_prep)

# Add nodes for logistics planning
logistics_plan = Transition(label='Logistics Plan')
root.add_node(logistics_plan)
root.add_edge(packaging_prep, logistics_plan)

# Add nodes for client review
client_review = Transition(label='Client Review')
root.add_node(client_review)
root.add_edge(logistics_plan, client_review)

# Define the loop for the process
loop = OperatorPOWL(operator=Operator.LOOP, children=['Flight Testing', 'Data Analyze', 'Regulation Check', 'Quality Inspect', 'Packaging Prep', 'Logistics Plan', 'Client Review'])
root.add_node(loop)
root.add_edge(root, loop)

# Define the XOR for the process
xor = OperatorPOWL(operator=Operator.XOR, children=['Assembly Setup', 'Software Load', 'Sensor Calibrate', 'Firmware Integrate', 'Payload Configure', 'Chassis Build'])
root.add_node(xor)
root.add_edge(root, xor)

# Add the loop and XOR to the root node
root.add_edge(root, loop)
root.add_edge(root, xor)

# Print the final POWL model
print(root)