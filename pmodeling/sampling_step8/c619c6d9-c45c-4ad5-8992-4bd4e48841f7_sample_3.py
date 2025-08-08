import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_calibrate, firmware_integrate, payload_configure, assembly_setup, wiring_connect, chassis_build, software_load, flight_testing, data_analyze, regulation_check, quality_inspect])
xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, logistics_plan, client_review])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)