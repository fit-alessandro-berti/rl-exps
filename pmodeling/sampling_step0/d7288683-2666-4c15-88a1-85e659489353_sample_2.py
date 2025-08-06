import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
source_sourcing = Transition(label='Component Sourcing')
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

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice for AI module installation
xor_ai_module = OperatorPOWL(operator=Operator.XOR, children=[ai_module, skip])

# Define the loop for flight pattern optimization
loop_pattern_adjustment = OperatorPOWL(operator=Operator.LOOP, children=[flight_simulation, pattern_adjustment])

# Define the exclusive choice for flight simulation
xor_flight_simulation = OperatorPOWL(operator=Operator.XOR, children=[flight_simulation, skip])

# Define the exclusive choice for calibration phase
xor_calibration_phase = OperatorPOWL(operator=Operator.XOR, children=[calibration_phase, skip])

# Define the exclusive choice for firmware upload
xor_firmware_upload = OperatorPOWL(operator=Operator.XOR, children=[firmware_upload, skip])

# Define the exclusive choice for motor installation
xor_motor_installation = OperatorPOWL(operator=Operator.XOR, children=[motor_installation, skip])

# Define the exclusive choice for sensor mounting
xor_sensor_mounting = OperatorPOWL(operator=Operator.XOR, children=[sensor_mounting, skip])

# Define the exclusive choice for wiring setup
xor_wiring_setup = OperatorPOWL(operator=Operator.XOR, children=[wiring_setup, skip])

# Define the exclusive choice for stress testing
xor_stress_testing = OperatorPOWL(operator=Operator.XOR, children=[stress_testing, skip])

# Define the exclusive choice for quality inspect
xor_quality_inspect = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, skip])

# Define the exclusive choice for compliance check
xor_compliance_check = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])

# Define the exclusive choice for packaging final
xor_packaging_final = OperatorPOWL(operator=Operator.XOR, children=[packaging_final, skip])

# Define the exclusive choice for delivery setup
xor_delivery_setup = OperatorPOWL(operator=Operator.XOR, children=[delivery_setup, skip])

# Define the exclusive choice for frame assembly
xor_frame_assembly = OperatorPOWL(operator=Operator.XOR, children=[frame_assembly, xor_ai_module, xor_firmware_upload, xor_motor_installation, xor_sensor_mounting, xor_wiring_setup, xor_stress_testing, xor_quality_inspect, xor_compliance_check, xor_packaging_final, xor_delivery_setup])

# Define the root POWL model
root = StrictPartialOrder(nodes=[source_sourcing, xor_frame_assembly, loop_pattern_adjustment, xor_flight_simulation, xor_calibration_phase, xor_firmware_upload, xor_motor_installation, xor_sensor_mounting, xor_wiring_setup, xor_stress_testing, xor_quality_inspect, xor_compliance_check, xor_packaging_final, xor_delivery_setup])

# Add the dependencies between the nodes
root.order.add_edge(source_sourcing, xor_frame_assembly)
root.order.add_edge(xor_frame_assembly, loop_pattern_adjustment)
root.order.add_edge(loop_pattern_adjustment, xor_flight_simulation)
root.order.add_edge(xor_flight_simulation, xor_calibration_phase)
root.order.add_edge(xor_calibration_phase, xor_firmware_upload)
root.order.add_edge(xor_firmware_upload, xor_motor_installation)
root.order.add_edge(xor_motor_installation, xor_sensor_mounting)
root.order.add_edge(xor_sensor_mounting, xor_wiring_setup)
root.order.add_edge(xor_wiring_setup, xor_stress_testing)
root.order.add_edge(xor_stress_testing, xor_quality_inspect)
root.order.add_edge(xor_quality_inspect, xor_compliance_check)
root.order.add_edge(xor_compliance_check, xor_packaging_final)
root.order.add_edge(xor_packaging_final, xor_delivery_setup)

# Return the root POWL model
return root