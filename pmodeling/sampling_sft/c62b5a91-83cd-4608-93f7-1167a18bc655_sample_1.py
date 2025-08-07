import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ai = Transition(label='Artifact Intake')
cc = Transition(label='Condition Check')
pr = Transition(label='Provenance Research')
st = Transition(label='Scientific Testing')
rd = Transition(label='Radiocarbon Dating')
sc = Transition(label='Spectroscopy Scan')
lc = Transition(label='Legal Clearance')
hc = Transition(label='Heritage Compliance')
da = Transition(label='Digital Archiving')
er = Transition(label='Expert Review')
cv = Transition(label='Committee Vote')
aa = Transition(label='Acquisition Approval')
cp = Transition(label='Conservation Plan')
ss = Transition(label='Storage Setup')
su = Transition(label='Stakeholder Update')

# Build the partial‐order sub‐workflow for testing and validation
testing_po = StrictPartialOrder(nodes=[st, rd, sc])
testing_po.order.add_edge(st, rd)
testing_po.order.add_edge(st, sc)

# Build the loop for continuous scientific testing
loop_testing = OperatorPOWL(operator=Operator.LOOP, children=[testing_po, testing_po])

# Build the loop for continuous expert review
loop_review = OperatorPOWL(operator=Operator.LOOP, children=[er, er])

# Assemble the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    ai, cc, pr, loop_testing, lc, hc, da, loop_review,
    cv, aa, cp, ss, su
])

# Define the control‐flow dependencies
root.order.add_edge(ai, cc)
root.order.add_edge(cc, pr)
root.order.add_edge(pr, loop_testing)
root.order.add_edge(loop_testing, lc)
root.order.add_edge(lc, hc)
root.order.add_edge(hc, da)
root.order.add_edge(da, loop_review)
root.order.add_edge(loop_review, cv)
root.order.add_edge(cv, aa)
root.order.add_edge(aa, cp)
root.order.add_edge(cp, ss)
root.order.add_edge(ss, su)