from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
source = Transition(label='Source')
sourcing = Transition(label='Component Sourcing')
calibrate = Transition(label='Sensor Calibrate')
motor = Transition(label='Motor Assembly')
frame = Transition(label='Frame Build')
install = Transition(label='Software Install')
tune = Transition(label='Algorithm Tune')
integrate = Transition(label='Battery Integrate')
test = Transition(label='Signal Test')
check = Transition(label='Durability Check')
simulate = Transition(label='Flight Simulate')
inspect = Transition(label='Quality Inspect')
review = Transition(label='Compliance Review')
prep = Transition(label='Packaging Prep')
logistics = Transition(label='Logistics Plan')
client = Transition(label='Client Feedback')

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[client, skip])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[simulate, inspect, review])

# Define the partial order
root = StrictPartialOrder(nodes=[source, sourcing, calibrate, motor, frame, install, tune, integrate, test, check, loop, xor])
root.order.add_edge(source, sourcing)
root.order.add_edge(sourcing, calibrate)
root.order.add_edge(calibrate, motor)
root.order.add_edge(motor, frame)
root.order.add_edge(frame, install)
root.order.add_edge(install, tune)
root.order.add_edge(tune, integrate)
root.order.add_edge(integrate, test)
root.order.add_edge(test, check)
root.order.add_edge(check, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, client)
root.order.add_edge(xor, skip)