import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
A = Transition(label='Component Sourcing')
B = Transition(label='Frame Assembly')
C = Transition(label='Motor Installation')
D = Transition(label='Sensor Mounting')
E = Transition(label='Wiring Setup')
F = Transition(label='Firmware Upload')
G = Transition(label='AI Module')
H = Transition(label='Calibration Phase')
I = Transition(label='Stress Testing')
J = Transition(label='Flight Simulation')
K = Transition(label='Pattern Adjustment')
L = Transition(label='Quality Inspect')
M = Transition(label='Compliance Check')
N = Transition(label='Packaging Final')
O = Transition(label='Delivery Setup')

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[B, C, D, E, F])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[G, H, I, J])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[K, L, M])
xor = OperatorPOWL(operator=Operator.XOR, children=[N, skip])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, xor])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, xor)