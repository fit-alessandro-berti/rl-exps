import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ai = Transition(label='Artifact Intake')
cc = Transition(label='Condition Check')
ms = Transition(label='Multi-spectral Scan')
mt = Transition(label='Material Test')
dm = Transition(label='Database Match')
pc = Transition(label='Provenance Check')
er = Transition(label='Expert Review')
hq = Transition(label='Historical Query')
lc = Transition(label='Lab Collaboration')
ia = Transition(label='Imaging Analysis')
fd = Transition(label='Forgery Detection')
ld = Transition(label='Legal Drafting')
ci = Transition(label='Certification Issue')
cb = Transition(label='Client Briefing')
au = Transition(label='Archival Update')

# Build the loop body: Expert Review -> Historical Query -> Lab Collaboration -> Imaging Analysis -> Forgery Detection
body = StrictPartialOrder(nodes=[er, hq, lc, ia, fd])
body.order.add_edge(er, hq)
body.order.add_edge(hq, lc)
body.order.add_edge(lc, ia)
body.order.add_edge(ia, fd)

# LOOP: do Condition Check, then either exit or do the loop body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[cc, body])

# Build the main partial order
root = StrictPartialOrder(nodes=[
    ai, cc, ms, mt, dm, pc, loop,
    er, hq, lc, ia, fd, ld, ci, cb, au
])

# Sequential edges
root.order.add_edge(ai, cc)
root.order.add_edge(cc, ms)
root.order.add_edge(cc, mt)
root.order.add_edge(ms, dm)
root.order.add_edge(mt, dm)
root.order.add_edge(dm, pc)
root.order.add_edge(pc, er)
root.order.add_edge(er, hq)
root.order.add_edge(hq, lc)
root.order.add_edge(lc, ia)
root.order.add_edge(ia, fd)
root.order.add_edge(fd, ld)
root.order.add_edge(ld, ci)
root.order.add_edge(ci, cb)
root.order.add_edge(cb, au)