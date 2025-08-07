import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
cs = Transition(label='Component Sourcing')
fb = Transition(label='Client Feedback')
sensor = Transition(label='Sensor Calibrate')
motor = Transition(label='Motor Assembly')
frame = Transition(label='Frame Build')
sw = Transition(label='Software Install')
algo = Transition(label='Algorithm Tune')
battery = Transition(label='Battery Integrate')
signal = Transition(label='Signal Test')
durability = Transition(label='Durability Check')
flight = Transition(label='Flight Simulate')
quality = Transition(label='Quality Inspect')
compliance = Transition(label='Compliance Review')
pack = Transition(label='Packaging Prep')
logistics = Transition(label='Logistics Plan')

# Build the core assembly & testing partial order
core = StrictPartialOrder(nodes=[
    sensor, motor, frame, sw, algo,
    battery, signal, durability, flight, quality
])
core.order.add_edge(sensor, battery)
core.order.add_edge(motor, battery)
core.order.add_edge(frame, battery)
core.order.add_edge(sw, battery)
core.order.add_edge(algo, battery)
core.order.add_edge(battery, signal)
core.order.add_edge(signal, durability)
core.order.add_edge(durability, flight)
core.order.add_edge(flight, quality)

# Loop for iterative flight & quality checks
loop = OperatorPOWL(operator=Operator.LOOP, children=[flight, quality])

# Assemble the full process partial order
root = StrictPartialOrder(nodes=[
    cs, fb, core, loop, compliance, pack, logistics
])
root.order.add_edge(cs, core)
root.order.add_edge(fb, compliance)
root.order.add_edge(core, compliance)
root.order.add_edge(compliance, pack)
root.order.add_edge(pack, logistics)

# Final loop for client feedback integration
skip = SilentTransition()
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, fb])
root.order.add_edge(loop, xor)