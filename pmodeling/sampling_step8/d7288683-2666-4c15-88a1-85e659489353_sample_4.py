import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
sourcing = Transition(label='Component Sourcing')
assembly = Transition(label='Frame Assembly')
motor_install = Transition(label='Motor Installation')
sensor_mount = Transition(label='Sensor Mounting')
wiring_setup = Transition(label='Wiring Setup')
firmware_upload = Transition(label='Firmware Upload')
ai_module = Transition(label='AI Module')
calibration = Transition(label='Calibration Phase')
stress_testing = Transition(label='Stress Testing')
flight_simulation = Transition(label='Flight Simulation')
pattern_adjustment = Transition(label='Pattern Adjustment')
quality_inspect = Transition(label='Quality Inspect')
compliance_check = Transition(label='Compliance Check')
packaging_final = Transition(label='Packaging Final')
delivery_setup = Transition(label='Delivery Setup')

# Define the loop for calibration and stress testing
calibration_loop = OperatorPOWL(operator=Operator.LOOP, children=[calibration, stress_testing])

# Define the XOR for flight simulation and pattern adjustment
flight_simulation_xor = OperatorPOWL(operator=Operator.XOR, children=[flight_simulation, pattern_adjustment])

# Define the main workflow
root = StrictPartialOrder(nodes=[sourcing, assembly, motor_install, sensor_mount, wiring_setup, firmware_upload, ai_module, calibration_loop, flight_simulation_xor, quality_inspect, compliance_check, packaging_final, delivery_setup])
root.order.add_edge(sourcing, assembly)
root.order.add_edge(assembly, motor_install)
root.order.add_edge(motor_install, sensor_mount)
root.order.add_edge(sensor_mount, wiring_setup)
root.order.add_edge(wiring_setup, firmware_upload)
root.order.add_edge(firmware_upload, ai_module)
root.order.add_edge(ai_module, calibration_loop)
root.order.add_edge(calibration_loop, flight_simulation_xor)
root.order.add_edge(flight_simulation_xor, quality_inspect)
root.order.add_edge(quality_inspect, compliance_check)
root.order.add_edge(compliance_check, packaging_final)
root.order.add_edge(packaging_final, delivery_setup)