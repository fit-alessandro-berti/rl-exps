import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activity_names = ['Component Sourcing', 'Frame Assembly', 'Motor Installation', 'Sensor Mounting', 'Wiring Setup', 'Firmware Upload', 'AI Module', 'Calibration Phase', 'Stress Testing', 'Flight Simulation', 'Pattern Adjustment', 'Quality Inspect', 'Compliance Check', 'Packaging Final', 'Delivery Setup']
activities = [Transition(label=name) for name in activity_names]

# Define the loop for iterative flight pattern optimization
loop = OperatorPOWL(operator=Operator.LOOP, children=activities[:6])

# Define the exclusive choice for AI module installation and calibration
xor = OperatorPOWL(operator=Operator.XOR, children=activities[6:9])

# Define the partial order
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Return the root of the POWL model
root