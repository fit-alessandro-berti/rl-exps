import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
sourcing = Transition(label='Component Sourcing')
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

# Define the root process
root = StrictPartialOrder(nodes=[
    sourcing,
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

# The order of activities is not explicitly defined in the POWL model for this process, as it's typically determined by the sequence of tasks and dependencies between them.
# If there are specific dependencies between activities, they would be defined in the 'order' attribute of the StrictPartialOrder object.
# For example, if 'frame_assembly' must be completed before 'motor_installation', you would add an edge in the 'order' attribute as follows:
# root.order.add_edge(sourcing, frame_assembly)
# root.order.add_edge(frame_assembly, motor_installation)

# Print the root process to verify
print(root)