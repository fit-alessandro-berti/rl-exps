import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    component_sourcing,
    frame_assembly,
    motor_installation,
    sensor_mounting,
    wiring_setup,
    firmware_upload,
    ai_module,
    calibration_phase,
    stress_testing,
    flight_simulation,
    pattern_adjustment,
    quality_inspect,
    compliance_check,
    packaging_final,
    delivery_setup
])

# Add dependencies if necessary (based on the specific process flow)
# For example, if 'Calibration Phase' depends on 'Component Sourcing':
# root.order.add_edge(component_sourcing, calibration_phase)

# Similarly, you can add more dependencies as needed for the specific process flow.