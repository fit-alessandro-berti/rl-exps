import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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
packaging_final = Transition(label='Packaging Final')
delivery_setup = Transition(label='Delivery Setup')

# Define the dependencies and loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[calibration, stress_testing, flight_simulation])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[pattern_adjustment, quality_inspect, compliance_check])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_final, delivery_setup])
xor = OperatorPOWL(operator=Operator.XOR, children=[motor_installation, sensor_mounting, wiring_setup])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[firmware_upload, ai_module])
root = StrictPartialOrder(nodes=[sourcing, assembly, xor, xor2, loop1, loop2, loop3])

# Connect the nodes
root.order.add_edge(sourcing, assembly)
root.order.add_edge(assembly, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, packaging_final)
root.order.add_edge(packaging_final, delivery_setup)

print(root)