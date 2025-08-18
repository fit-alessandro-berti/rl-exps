import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loop and choice nodes
calibration_loop = OperatorPOWL(operator=Operator.LOOP, children=[calibration_phase, stress_testing])
flight_simulation_choice = OperatorPOWL(operator=Operator.XOR, children=[flight_simulation, pattern_adjustment])
quality_inspect_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, compliance_check])
final_packaging = OperatorPOWL(operator=Operator.LOOP, children=[packaging_final, delivery_setup])

# Create the root node with the defined activities
root = StrictPartialOrder(nodes=[
    component_sourcing, frame_assembly, motor_installation, sensor_mounting, wiring_setup,
    firmware_upload, ai_module, calibration_loop, flight_simulation_choice,
    quality_inspect_loop, final_packaging
])

# Add edges to define the partial order
root.order.add_edge(component_sourcing, frame_assembly)
root.order.add_edge(frame_assembly, motor_installation)
root.order.add_edge(motor_installation, sensor_mounting)
root.order.add_edge(sensor_mounting, wiring_setup)
root.order.add_edge(wiring_setup, firmware_upload)
root.order.add_edge(firmware_upload, ai_module)
root.order.add_edge(ai_module, calibration_loop)
root.order.add_edge(calibration_loop, flight_simulation_choice)
root.order.add_edge(flight_simulation_choice, quality_inspect_loop)
root.order.add_edge(quality_inspect_loop, final_packaging)
root.order.add_edge(final_packaging, delivery_setup)

print(root)