import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ai = Transition(label='Artifact Intake')
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Sampling')
st = Transition(label='Scientific Test')
er = Transition(label='Expert Review')
asrch = Transition(label='Archive Search')
lv = Transition(label='Legal Verify')
oc = Transition(label='Ownership Confirm')
ca = Transition(label='Compliance Audit')
dd = Transition(label='Data Documentation')
ir = Transition(label='Interim Report')
dr = Transition(label='Department Review')
cm = Transition(label='Consensus Meeting')
fa = Transition(label='Final Approval')
ar = Transition(label='Artifact Release')

# Build the loop body: archive search, legal verify, ownership confirm, compliance audit
body = StrictPartialOrder(nodes=[asrch, lv, oc, ca])
body.order.add_edge(asrch, lv)
body.order.add_edge(lv, oc)
body.order.add_edge(oc, ca)

# Loop: do Data Documentation, then optionally do the body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[dd, body])

# Build the main partial order
root = StrictPartialOrder(nodes=[ai, pc, ms, st, er, loop, ir, dr, cm, fa, ar])

# Sequential dependencies
root.order.add_edge(ai, pc)
root.order.add_edge(pc, ms)
root.order.add_edge(ms, st)
root.order.add_edge(st, er)
root.order.add_edge(er, loop)
root.order.add_edge(loop, ir)
root.order.add_edge(ir, dr)
root.order.add_edge(dr, cm)
root.order.add_edge(cm, fa)
root.order.add_edge(fa, ar)

# Print the root to verify
print(root)