import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ig = Transition(label='Intel Gathering')
ra = Transition(label='Risk Assess')
bs = Transition(label='Behavior Scan')
nm = Transition(label='Network Monitor')
ac = Transition(label='Audit Conduct')
fs = Transition(label='Flag Suspicion')
lr = Transition(label='Legal Review')
cc = Transition(label='Compliance Check')
et = Transition(label='Employee Train')
ts = Transition(label='Threat Simulate')
ip = Transition(label='Incident Plan')
rd = Transition(label='Response Drill')
de = Transition(label='Data Encrypt')
pl = Transition(label='Partner Liaison')
rg = Transition(label='Report Generate')
fl = Transition(label='Feedback Loop')

# Loop for continuous improvement: simulate threats, then either exit or do feedback
improvement_loop = OperatorPOWL(operator=Operator.LOOP, children=[ts, fl])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ig, ra, bs, nm, ac,
    fs, lr, cc, et,
    improvement_loop,
    ip, rd, de, pl, rg
])

# Define the control-flow dependencies
root.order.add_edge(ig, ra)
root.order.add_edge(ig, bs)
root.order.add_edge(ig, nm)
root.order.add_edge(ig, ac)
root.order.add_edge(ra, fs)
root.order.add_edge(bs, fs)
root.order.add_edge(nm, fs)
root.order.add_edge(ac, fs)
root.order.add_edge(fs, lr)
root.order.add_edge(fs, cc)
root.order.add_edge(fs, et)
root.order.add_edge(lr, improvement_loop)
root.order.add_edge(cc, improvement_loop)
root.order.add_edge(et, improvement_loop)
root.order.add_edge(improvement_loop, ip)
root.order.add_edge(ip, rd)
root.order.add_edge(ip, de)
root.order.add_edge(ip, pl)
root.order.add_edge(rd, rg)
root.order.add_edge(de, rg)
root.order.add_edge(pl, rg)
root.order.add_edge(rg, improvement_loop)