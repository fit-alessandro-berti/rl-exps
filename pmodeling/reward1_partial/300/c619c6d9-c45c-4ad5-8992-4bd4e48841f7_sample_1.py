from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define the workflow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[firmware_integrate, data_analyze])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[regulation_check, quality_inspect])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, logistics_plan])
xor = OperatorPOWL(operator=Operator.XOR, children=[client_review, SilentTransition()])
root = StrictPartialOrder(nodes=[design_consult, component_sourcing, sensor_calibrate, firmware_integrate, payload_configure, assembly_setup, wiring_connect, chassis_build, software_load, flight_testing, loop1, loop2, loop3, xor])
root.order.add_edge(design_consult, component_sourcing)
root.order.add_edge(component_sourcing, sensor_calibrate)
root.order.add_edge(sensor_calibrate, firmware_integrate)
root.order.add_edge(firmware_integrate, data_analyze)
root.order.add_edge(data_analyze, regulation_check)
root.order.add_edge(regulation_check, quality_inspect)
root.order.add_edge(quality_inspect, packaging_prep)
root.order.add_edge(packaging_prep, logistics_plan)
root.order.add_edge(logistics_plan, client_review)
root.order.add_edge(client_review, xor)
root.order.add_edge(flight_testing, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, xor)

# Return the root of the POWL model
return root