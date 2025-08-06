import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[
    OperatorPOWL(operator=Operator.LOOP, children=[firmware_upload, ai_module]),
    OperatorPOWL(operator=Operator.LOOP, children=[calibration_phase, stress_testing])
])
loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_simulation, pattern_adjustment])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[
    OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, compliance_check]),
    OperatorPOWL(operator=Operator.LOOP, children=[packaging_final, delivery_setup])
])

# Create the Partial Order (PO)
root = StrictPartialOrder(nodes=[xor, loop, xor2])
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor2)