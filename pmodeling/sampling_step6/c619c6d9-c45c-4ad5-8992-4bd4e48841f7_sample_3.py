import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the process
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

# Define the partial order of the process
root = StrictPartialOrder(nodes=[
    design_consult,
    component_sourcing,
    sensor_calibrate,
    firmware_integrate,
    payload_configure,
    assembly_setup,
    wiring_connect,
    chassis_build,
    software_load,
    flight_testing,
    data_analyze,
    regulation_check,
    quality_inspect,
    packaging_prep,
    logistics_plan,
    client_review
])

# Optionally, define dependencies if any are present in the process
# For example, if there's a dependency between 'Component Sourcing' and 'Sensor Calibrate':
# root.order.add_edge(component_sourcing, sensor_calibrate)

# Now 'root' contains the POWL model for the process.
# You can use this model to simulate the process or further analyze it.