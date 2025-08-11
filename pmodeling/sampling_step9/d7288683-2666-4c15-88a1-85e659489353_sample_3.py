import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
component_sourcing = Transition(label='Component Sourcing')
frame_assembly = Transition(label='Frame Assembly')
motor_installation = Transition(label='Motor Installation')
sensor_mounting = Transition(label='Sensor Mounting')
wiring_setup = Transition(label='Wiring Setup')
firmware_upload = Transition(label='Firmware Upload')
ai_module = Transition(label='AI Module')
calibration_phase = Transition(label='Calibration Phase')
stress_testing = Transition(label='Stress Testing')
flight_simulation = Transition(label='Flight Simulation')
pattern_adjustment = Transition(label='Pattern Adjustment')
quality_inspect = Transition(label='Quality Inspect')
compliance_check = Transition(label='Compliance Check')
packaging_final = Transition(label='Packaging Final')
delivery_setup = Transition(label='Delivery Setup')

# Define silent transitions (for empty labels)
skip = SilentTransition()

# Define the workflow
loop_calibration = OperatorPOWL(operator=Operator.LOOP, children=[calibration_phase, skip])
loop_testing = OperatorPOWL(operator=Operator.LOOP, children=[stress_testing, skip])
loop_simulation = OperatorPOWL(operator=Operator.LOOP, children=[flight_simulation, skip])
loop_adjustment = OperatorPOWL(operator=Operator.LOOP, children=[pattern_adjustment, skip])
loop_inspect = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, skip])
loop_compliance = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, skip])
loop_delivery = OperatorPOWL(operator=Operator.LOOP, children=[delivery_setup, skip])

xor_components = OperatorPOWL(operator=Operator.XOR, children=[component_sourcing, frame_assembly, motor_installation, sensor_mounting, wiring_setup, firmware_upload, ai_module])

xor_calibration = OperatorPOWL(operator=Operator.XOR, children=[loop_calibration, xor_components])

xor_testing = OperatorPOWL(operator=Operator.XOR, children=[loop_testing, xor_calibration])

xor_simulation = OperatorPOWL(operator=Operator.XOR, children=[loop_simulation, xor_testing])

xor_adjustment = OperatorPOWL(operator=Operator.XOR, children=[loop_adjustment, xor_simulation])

xor_inspect = OperatorPOWL(operator=Operator.XOR, children=[loop_inspect, xor_adjustment])

xor_compliance = OperatorPOWL(operator=Operator.XOR, children=[loop_compliance, xor_inspect])

xor_delivery = OperatorPOWL(operator=Operator.XOR, children=[loop_delivery, xor_compliance])

root = StrictPartialOrder(nodes=[xor_delivery])
root.order.add_edge(xor_delivery, xor_compliance)
root.order.add_edge(xor_compliance, xor_inspect)
root.order.add_edge(xor_inspect, xor_adjustment)
root.order.add_edge(xor_adjustment, xor_simulation)
root.order.add_edge(xor_simulation, xor_testing)
root.order.add_edge(xor_testing, xor_calibration)
root.order.add_edge(xor_calibration, xor_components)
root.order.add_edge(xor_components, xor_delivery)

# The final POWL model is in the variable 'root'