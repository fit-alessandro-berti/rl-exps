from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition with its label
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

# Define the partial order edges
root.order.add_edge(component_sourcing, frame_assembly)
root.order.add_edge(frame_assembly, motor_installation)
root.order.add_edge(motor_installation, sensor_mounting)
root.order.add_edge(sensor_mounting, wiring_setup)
root.order.add_edge(wiring_setup, firmware_upload)
root.order.add_edge(firmware_upload, ai_module)
root.order.add_edge(ai_module, calibration_phase)
root.order.add_edge(calibration_phase, stress_testing)
root.order.add_edge(stress_testing, flight_simulation)
root.order.add_edge(flight_simulation, pattern_adjustment)
root.order.add_edge(pattern_adjustment, quality_inspect)
root.order.add_edge(quality_inspect, compliance_check)
root.order.add_edge(compliance_check, packaging_final)
root.order.add_edge(packaging_final, delivery_setup)

# Print the root POWL model
print(root)