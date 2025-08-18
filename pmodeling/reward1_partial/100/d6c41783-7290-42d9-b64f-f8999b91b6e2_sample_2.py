import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
qm = Transition(label='Quantum Modeling')
de = Transition(label='Data Encoding')
rs = Transition(label='Route Simulation')
df = Transition(label='Demand Forecast')
ss = Transition(label='Supplier Sync')
en = Transition(label='Entangle Nodes')
ra = Transition(label='Risk Analysis')
is_ = Transition(label='Inventory Scan')
lc = Transition(label='Latency Check')
tp = Transition(label='Transport Plan')
qc = Transition(label='Quantum Compute')
st = Transition(label='Scenario Test')
raa = Transition(label='Resource Align')
pu = Transition(label='Protocol Update')
fl = Transition(label='Feedback Loop')
co = Transition(label='Cost Optimize')
ir = Transition(label='Impact Review')

# Define the operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[de, qm])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ra, df])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[ss, en])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[rc, tp])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[qc, st])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[raa, pu])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[fl, co])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[ir, co])

# Define the root node
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor2, xor5)
root.order.add_edge(xor3, xor6)
root.order.add_edge(xor4, xor7)
root.order.add_edge(xor5, xor8)

# Print the root node
print(root)