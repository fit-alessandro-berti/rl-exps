from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
A = Transition(label='Seed Selection')
B = Transition(label='Nutrient Setup')
C = Transition(label='Growth Monitoring')
D = Transition(label='Climate Adjust')
E = Transition(label='Pest Control')
F = Transition(label='Water Recirculate')
G = Transition(label='Light Calibration')
H = Transition(label='Robotic Harvest')
I = Transition(label='Quality Inspect')
J = Transition(label='Waste Process')
K = Transition(label='Energy Reuse')
L = Transition(label='Inventory Update')
M = Transition(label='Demand Forecast')
N = Transition(label='Order Dispatch')
O = Transition(label='Community Event')
P = Transition(label='Feedback Collect')
Q = Transition(label='Data Analyze')
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[C, D, E, F, G, H, I])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[J, K, L])
xor = OperatorPOWL(operator=Operator.XOR, children=[M, N])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[O, P])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Q, skip])

# Define the root node
root = StrictPartialOrder(nodes=[loop1, loop2, xor, xor2, xor3])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor, xor3)

# Return the root node
return root