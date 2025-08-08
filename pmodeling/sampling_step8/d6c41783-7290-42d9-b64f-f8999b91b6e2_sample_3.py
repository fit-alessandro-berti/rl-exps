from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
qm = Transition(label='Quantum Modeling')
de = Transition(label='Data Encoding')
rs = Transition(label='Route Simulation')
df = Transition(label='Demand Forecast')
ss = Transition(label='Supplier Sync')
en = Transition(label='Entangle Nodes')
ra = Transition(label='Risk Analysis')
isv = Transition(label='Inventory Scan')
lc = Transition(label='Latency Check')
tp = Transition(label='Transport Plan')
qc = Transition(label='Quantum Compute')
sc = Transition(label='Scenario Test')
ra2 = Transition(label='Resource Align')
pu = Transition(label='Protocol Update')
fl = Transition(label='Feedback Loop')
co = Transition(label='Cost Optimize')
ir = Transition(label='Impact Review')

# Define control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[qm, de])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[rs, df])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[ss, en])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ra, isv])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[lc, tp])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[qc, sc])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[ra2, pu])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[fl, co])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[ir, co])

# Define partial order
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)

print(root)