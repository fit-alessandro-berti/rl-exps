import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ai = Transition(label='Artifact Intake')
cc = Transition(label='Condition Check')
pr = Transition(label='Provenance Research')
st = Transition(label='Scientific Testing')
rd = Transition(label='Radiocarbon Dating')
ss = Transition(label='Spectroscopy Scan')
lc = Transition(label='Legal Clearance')
hc = Transition(label='Heritage Compliance')
da = Transition(label='Digital Archiving')
er = Transition(label='Expert Review')
cv = Transition(label='Committee Vote')
aa = Transition(label='Acquisition Approval')
cp = Transition(label='Conservation Plan')
ssu = Transition(label='Storage Setup')
su = Transition(label='Stakeholder Update')

# Build the loop for the expert review cycle: do Expert Review, then either exit or do Committee Vote and repeat
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[er, cv])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    ai, cc, pr, st, rd, ss, lc, hc, da, expert_loop, aa, cp, ssu, su
])

# Initial sequence
root.order.add_edge(ai, cc)
root.order.add_edge(cc, pr)

# Provenance research feeds testing
root.order.add_edge(pr, st)

# Testing branches into radiocarbon and spectroscopy
root.order.add_edge(st, rd)
root.order.add_edge(st, ss)

# All testing results branch to legal and heritage compliance
root.order.add_edge(rd, lc)
root.order.add_edge(ss, lc)
root.order.add_edge(lc, hc)

# Compliance branch to digital archiving
root.order.add_edge(hc, da)

# Digital archiving then expert review cycle
root.order.add_edge(da, expert_loop)

# Expert review cycle leads to acquisition approval
root.order.add_edge(expert_loop, aa)

# Acquisition approval triggers conservation plan and storage setup
root.order.add_edge(aa, cp)
root.order.add_edge(aa, ssu)

# Finally, stakeholder update completes the process
root.order.add_edge(cp, su)
root.order.add_edge(ssu, su)