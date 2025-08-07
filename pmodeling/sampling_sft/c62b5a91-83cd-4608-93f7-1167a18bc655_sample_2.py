import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ai = Transition(label='Artifact Intake')
cc = Transition(label='Condition Check')
pr = Transition(label='Provenance Research')
st = Transition(label='Scientific Testing')
rd = Transition(label='Radiocarbon Dating')
sp = Transition(label='Spectroscopy Scan')
lc = Transition(label='Legal Clearance')
hc = Transition(label='Heritage Compliance')
da = Transition(label='Digital Archiving')
er = Transition(label='Expert Review')
cv = Transition(label='Committee Vote')
aa = Transition(label='Acquisition Approval')
cp = Transition(label='Conservation Plan')
ss = Transition(label='Storage Setup')
su = Transition(label='Stakeholder Update')

# Define the expert review loop: repeat Expert Review -> Committee Vote until consensus
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[er, cv]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    ai, cc, pr, st, rd, sp, lc, hc, da, loop, aa, cp, ss, su
])

# Add ordering constraints
root.order.add_edge(ai, cc)
root.order.add_edge(cc, pr)
root.order.add_edge(pr, st)
root.order.add_edge(st, rd)
root.order.add_edge(st, sp)
root.order.add_edge(rd, lc)
root.order.add_edge(sp, lc)
root.order.add_edge(lc, hc)
root.order.add_edge(hc, da)
root.order.add_edge(da, loop)
root.order.add_edge(loop, aa)
root.order.add_edge(aa, cp)
root.order.add_edge(cp, ss)
root.order.add_edge(ss, su)