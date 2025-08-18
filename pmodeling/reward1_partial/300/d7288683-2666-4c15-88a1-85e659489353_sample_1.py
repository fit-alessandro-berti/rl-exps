from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions
sourcing = Transition(label='Component Sourcing')
assembly = Transition(label='Frame Assembly')
motor = Transition(label='Motor Installation')
sensor = Transition(label='Sensor Mounting')
wiring = Transition(label='Wiring Setup')
firmware = Transition(label='Firmware Upload')
ai_module = Transition(label='AI Module')
calibration = Transition(label='Calibration Phase')
stress = Transition(label='Stress Testing')
simulation = Transition(label='Flight Simulation')
adjustment = Transition(label='Pattern Adjustment')
quality = Transition(label='Quality Inspect')
compliance = Transition(label='Compliance Check')
packaging = Transition(label='Packaging Final')
delivery = Transition(label='Delivery Setup')

# Define loop and choice
loop_calibration = OperatorPOWL(operator=Operator.LOOP, children=[calibration, stress, simulation, adjustment])
choice_quality = OperatorPOWL(operator=Operator.XOR, children=[quality, compliance, packaging])
choice_delivery = OperatorPOWL(operator=Operator.XOR, children=[delivery, packaging])

# Create root
root = StrictPartialOrder(nodes=[sourcing, assembly, motor, sensor, wiring, firmware, ai_module, loop_calibration, choice_quality, choice_delivery])

# Add edges to the partial order
root.order.add_edge(sourcing, assembly)
root.order.add_edge(assembly, motor)
root.order.add_edge(motor, sensor)
root.order.add_edge(sensor, wiring)
root.order.add_edge(wiring, firmware)
root.order.add_edge(firmware, ai_module)
root.order.add_edge(ai_module, loop_calibration)
root.order.add_edge(loop_calibration, choice_quality)
root.order.add_edge(choice_quality, choice_delivery)
root.order.add_edge(choice_delivery, packaging)
root.order.add_edge(packaging, delivery)

# Print the root
print(root)