import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
sourcing = Transition(label='Component Sourcing')
assembly = Transition(label='Frame Assembly')
motor_installation = Transition(label='Motor Installation')
sensor_mounting = Transition(label='Sensor Mounting')
wiring_setup = Transition(label='Wiring Setup')
firmware_upload = Transition(label='Firmware Upload')
ai_module = Transition(label='AI Module')
calibration = Transition(label='Calibration Phase')
stress_testing = Transition(label='Stress Testing')
flight_simulation = Transition(label='Flight Simulation')
pattern_adjustment = Transition(label='Pattern Adjustment')
quality_inspect = Transition(label='Quality Inspect')
compliance_check = Transition(label='Compliance Check')
packaging = Transition(label='Packaging Final')
delivery = Transition(label='Delivery Setup')

# Define the loop nodes
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_simulation, pattern_adjustment])
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_simulation, pattern_adjustment])
flight_loop = OperatorPOWL(operator=Operator.LOOP, children=[flight_simulation, pattern_adjustment])

# Define the exclusive choice nodes
calibration_choice = OperatorPOWL(operator=Operator.XOR, children=[calibration, stress_testing])
flight_choice = OperatorPOWL(operator=Operator.XOR, children=[flight_simulation, pattern_adjustment])

# Define the root model
root = StrictPartialOrder(nodes=[sourcing, assembly, motor_installation, sensor_mounting, wiring_setup, firmware_upload, ai_module, calibration_choice, flight_choice, flight_loop, quality_inspect, compliance_check, packaging, delivery])
root.order.add_edge(sourcing, assembly)
root.order.add_edge(assembly, motor_installation)
root.order.add_edge(motor_installation, sensor_mounting)
root.order.add_edge(sensor_mounting, wiring_setup)
root.order.add_edge(wiring_setup, firmware_upload)
root.order.add_edge(firmware_upload, ai_module)
root.order.add_edge(ai_module, calibration_choice)
root.order.add_edge(calibration_choice, flight_choice)
root.order.add_edge(flight_choice, flight_loop)
root.order.add_edge(flight_loop, quality_inspect)
root.order.add_edge(quality_inspect, compliance_check)
root.order.add_edge(compliance_check, packaging)
root.order.add_edge(packaging, delivery)

# Print the root model
print(root)