import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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
st = Transition(label='Scenario Test')
ru = Transition(label='Resource Align')
pu = Transition(label='Protocol Update')
fl = Transition(label='Feedback Loop')
co = Transition(label='Cost Optimize')
ir = Transition(label='Impact Review')

# Build the loop body: Simulation -> Test -> Resource Align -> Protocol Update
body = StrictPartialOrder(nodes=[qc, st, ru, pu])
body.order.add_edge(qc, st)
body.order.add_edge(st, ru)
body.order.add_edge(ru, pu)

# Loop: do Simulation -> Test, then optionally do Feedback Loop and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, fl])

# Assemble the root partial order
root = StrictPartialOrder(nodes=[
    qm, de, rs, df, ss, en, ra, isv, lc, tp, loop, co, ir
])

# Add the control-flow dependencies
root.order.add_edge(qm, de)
root.order.add_edge(de, rs)
root.order.add_edge(rs, df)
root.order.add_edge(df, ss)
root.order.add_edge(ss, en)
root.order.add_edge(en, ra)
root.order.add_edge(ra, isv)
root.order.add_edge(isv, lc)
root.order.add_edge(lc, tp)
root.order.add_edge(tp, loop)
root.order.add_edge(loop, co)
root.order.add_edge(co, ir)

print(root)