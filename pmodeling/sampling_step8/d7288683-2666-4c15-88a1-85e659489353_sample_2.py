import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
source = Transition(label='Source')
sourcing = Transition(label='Component Sourcing')
frame = Transition(label='Frame Assembly')
motor = Transition(label='Motor Installation')
sensor = Transition(label='Sensor Mounting')
wiring = Transition(label='Wiring Setup')
firmware = Transition(label='Firmware Upload')
ai_module = Transition(label='AI Module')
calibration = Transition(label='Calibration Phase')
stress = Transition(label='Stress Testing')
flight = Transition(label='Flight Simulation')
adjustment = Transition(label='Pattern Adjustment')
quality = Transition(label='Quality Inspect')
compliance = Transition(label='Compliance Check')
packaging = Transition(label='Packaging Final')
delivery = Transition(label='Delivery Setup')

# Define the partial order
root = StrictPartialOrder(nodes=[source, sourcing, frame, motor, sensor, wiring, firmware, ai_module, calibration, stress, flight, adjustment, quality, compliance, packaging, delivery])
root.order.add_edge(source, sourcing)
root.order.add_edge(sourcing, frame)
root.order.add_edge(frame, motor)
root.order.add_edge(motor, sensor)
root.order.add_edge(sensor, wiring)
root.order.add_edge(wiring, firmware)
root.order.add_edge(firmware, ai_module)
root.order.add_edge(ai_module, calibration)
root.order.add_edge(calibration, stress)
root.order.add_edge(stress, flight)
root.order.add_edge(flight, adjustment)
root.order.add_edge(adjustment, quality)
root.order.add_edge(quality, compliance)
root.order.add_edge(compliance, packaging)
root.order.add_edge(packaging, delivery)