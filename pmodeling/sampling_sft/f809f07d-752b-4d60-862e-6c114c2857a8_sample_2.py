import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
pc = Transition(label='Provenance Check')
mt = Transition(label='Material Test')
asrch = Transition(label='Archive Search')
er = Transition(label='Expert Review')
ds = Transition(label='3D Scanning')
wa = Transition(label='Wear Analysis')
dc = Transition(label='Database Cross')
lc = Transition(label='Law Consult')
fd = Transition(label='Forgery Detect')
cert = Transition(label='Certification')
dp = Transition(label='Document Prep')
cs = Transition(label='Client Brief')
ss = Transition(label='Secure Storage')
ra = Transition(label='Risk Assessment')
fa = Transition(label='Final Approval')

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, mt, asrch, er,
    ds, wa, dc, lc, fd,
    cert, dp, cs, ss,
    ra, fa
])

# Provenance check precedes material test
root.order.add_edge(pc, mt)

# Material test can be done concurrently with archive search and expert review
root.order.add_edge(mt, asrch)
root.order.add_edge(mt, er)

# All three archival activities can proceed in parallel
root.order.add_edge(asrch, ds)
root.order.add_edge(er, ds)

# 3D scanning and wear analysis happen after 3D scanning
root.order.add_edge(ds, wa)

# Database cross and law consult happen in parallel
root.order.add_edge(ds, dc)
root.order.add_edge(ds, lc)

# Forgery detection happens after both database cross and law consult
root.order.add_edge(dc, fd)
root.order.add_edge(lc, fd)

# All detection results precede certification
root.order.add_edge(fd, cert)

# Certification precedes document preparation
root.order.add_edge(cert, dp)

# Document preparation precedes client briefing
root.order.add_edge(dp, cs)

# Client briefing precedes secure storage
root.order.add_edge(cs, ss)

# Risk assessment happens concurrently before final approval
root.order.add_edge(ra, fa)

# All steps precede final approval
for node in [ds, wa, fd, cert, dp, cs, ss, ra]:
    root.order.add_edge(node, fa)