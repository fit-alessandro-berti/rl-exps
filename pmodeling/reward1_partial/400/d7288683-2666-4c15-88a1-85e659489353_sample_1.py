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
stressing = Transition(label='Stress Testing')
simulation = Transition(label='Flight Simulation')
adjustment = Transition(label='Pattern Adjustment')
quality_inspect = Transition(label='Quality Inspect')
compliance_check = Transition(label='Compliance Check')
packaging = Transition(label='Packaging Final')
delivery = Transition(label='Delivery Setup')

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[stressing, quality_inspect])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, packaging])
loop = OperatorPOWL(operator=Operator.LOOP, children=[simulation, adjustment])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[delivery, xor2])

# Define the POWL model
root = StrictPartialOrder(nodes=[sourcing, assembly, motor_installation, sensor_mounting, wiring_setup, firmware_upload, ai_module, calibration, xor, loop, xor3])
root.order.add_edge(sourcing, assembly)
root.order.add_edge(assembly, motor_installation)
root.order.add_edge(motor_installation, sensor_mounting)
root.order.add_edge(sensor_mounting, wiring_setup)
root.order.add_edge(wiring_setup, firmware_upload)
root.order.add_edge(firmware_upload, ai_module)
root.order.add_edge(ai_module, calibration)
root.order.add_edge(calibration, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, simulation)
root.order.add_edge(simulation, adjustment)
root.order.add_edge(adjustment, xor3)
root.order.add_edge(xor3, delivery)
root.order.add_edge(xor3, xor2)

# Print the POWL model
print(root)