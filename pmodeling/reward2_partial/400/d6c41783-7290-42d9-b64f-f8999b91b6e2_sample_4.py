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
st = Transition(label='Scenario Test')
raa = Transition(label='Resource Align')
pu = Transition(label='Protocol Update')
fl = Transition(label='Feedback Loop')
co = Transition(label='Cost Optimize')
ir = Transition(label='Impact Review')

# Define partial order
root = StrictPartialOrder(nodes=[qm, de, rs, df, ss, en, ra, isv, lc, tp, qc, st, raa, pu, fl, co, ir])

# Define dependencies
root.order.add_edge(qm, de)
root.order.add_edge(de, rs)
root.order.add_edge(rs, df)
root.order.add_edge(df, ss)
root.order.add_edge(ss, en)
root.order.add_edge(en, ra)
root.order.add_edge(ra, isv)
root.order.add_edge(isv, lc)
root.order.add_edge(lc, tp)
root.order.add_edge(tp, qc)
root.order.add_edge(qc, st)
root.order.add_edge(st, raa)
root.order.add_edge(raa, pu)
root.order.add_edge(pu, fl)
root.order.add_edge(fl, co)
root.order.add_edge(co, ir)

# Save the result in the variable 'root'