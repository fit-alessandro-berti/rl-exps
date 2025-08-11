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

# Define loop and choice nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_calibrate, firmware_integrate, payload_configure])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[assembly_setup, wiring_connect, chassis_build, software_load])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[flight_testing, data_analyze, regulation_check])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, packaging_prep, logistics_plan, client_review])
choice1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])

# Define root
root = StrictPartialOrder(nodes=[choice1, choice2, choice3, choice4])
root.order.add_edge(choice1, loop1)
root.order.add_edge(choice2, loop2)
root.order.add_edge(choice3, loop3)
root.order.add_edge(choice4, loop4)