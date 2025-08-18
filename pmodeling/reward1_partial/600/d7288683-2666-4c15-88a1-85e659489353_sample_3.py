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
xor = OperatorPOWL(operator=Operator.XOR, children=[calibration_phase, stress_testing])
loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_simulation, pattern_adjustment])
partial_order = StrictPartialOrder(nodes=[
    component_sourcing,
    frame_assembly,
    motor_installation,
    sensor_mounting,
    wiring_setup,
    firmware_upload,
    ai_module,
    xor,
    quality_inspect,
    compliance_check,
    packaging_final,
    delivery_setup
])
partial_order.order.add_edge(component_sourcing, frame_assembly)
partial_order.order.add_edge(frame_assembly, motor_installation)
partial_order.order.add_edge(motor_installation, sensor_mounting)
partial_order.order.add_edge(sensor_mounting, wiring_setup)
partial_order.order.add_edge(wiring_setup, firmware_upload)
partial_order.order.add_edge(firmware_upload, ai_module)
partial_order.order.add_edge(ai_module, xor)
partial_order.order.add_edge(xor, quality_inspect)
partial_order.order.add_edge(quality_inspect, compliance_check)
partial_order.order.add_edge(compliance_check, packaging_final)
partial_order.order.add_edge(packaging_final, delivery_setup)

root = partial_order