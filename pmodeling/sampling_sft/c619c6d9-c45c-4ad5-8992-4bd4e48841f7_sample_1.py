import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
design_consult      = Transition(label='Design Consult')
component_sourcing  = Transition(label='Component Sourcing')
sensor_calibrate    = Transition(label='Sensor Calibrate')
firmware_integrate  = Transition(label='Firmware Integrate')
payload_configure   = Transition(label='Payload Configure')
assembly_setup      = Transition(label='Assembly Setup')
wiring_connect      = Transition(label='Wiring Connect')
chassis_build       = Transition(label='Chassis Build')
software_load       = Transition(label='Software Load')
flight_testing      = Transition(label='Flight Testing')
data_analyze        = Transition(label='Data Analyze')
regulation_check    = Transition(label='Regulation Check')
quality_inspect     = Transition(label='Quality Inspect')
packaging_prep      = Transition(label='Packaging Prep')
logistics_plan      = Transition(label='Logistics Plan')
client_review       = Transition(label='Client Review')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for iterative flight testing and data analysis
flight_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[flight_testing, data_analyze]
)

# Build the overall partial order
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
    flight_loop,
    regulation_check,
    quality_inspect,
    packaging_prep,
    logistics_plan,
    client_review
])

# Define the control-flow edges
root.order.add_edge(design_consult, component_sourcing)
root.order.add_edge(component_sourcing, sensor_calibrate)
root.order.add_edge(component_sourcing, firmware_integrate)
root.order.add_edge(sensor_calibrate, payload_configure)
root.order.add_edge(firmware_integrate, payload_configure)
root.order.add_edge(payload_configure, assembly_setup)
root.order.add_edge(assembly_setup, wiring_connect)
root.order.add_edge(assembly_setup, chassis_build)
root.order.add_edge(wiring_connect, software_load)
root.order.add_edge(chassis_build, software_load)
root.order.add_edge(software_load, flight_loop)
root.order.add_edge(flight_loop, regulation_check)
root.order.add_edge(regulation_check, quality_inspect)
root.order.add_edge(quality_inspect, packaging_prep)
root.order.add_edge(packaging_prep, logistics_plan)
root.order.add_edge(logistics_plan, client_review)

# Final exit edge from client_review to silent skip
root.order.add_edge(client_review, skip)