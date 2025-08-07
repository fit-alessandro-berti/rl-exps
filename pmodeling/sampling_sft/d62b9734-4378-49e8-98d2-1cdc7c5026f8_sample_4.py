import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
pc = Transition(label='Provenance Check')
ic = Transition(label='Image Capture')
ms = Transition(label='Material Scan')
ec = Transition(label='Expert Review')
hc = Transition(label='Historical Cross')
lv = Transition(label='Legal Verify')
rs = Transition(label='Registry Search')
cc = Transition(label='Customs Clear')
ca = Transition(label='Condition Assess')
dl = Transition(label='Data Log')
cc2 = Transition(label='Chain Custody')
rd = Transition(label='Report Draft')
cert = Transition(label='Certification')
sa = Transition(label='Secure Archive')
ap = Transition(label='Auction Prep')

# Build the partial order
root = StrictPartialOrder(nodes=[pc, ic, ms, ec, hc, lv, rs, cc, ca, dl, cc2, rd, cert, sa, ap])

# Initial provenance research
root.order.add_edge(pc, ic)
root.order.add_edge(pc, ms)
root.order.add_edge(pc, ec)
root.order.add_edge(pc, hc)
root.order.add_edge(pc, lv)

# Multi-spectral imaging and material scan
root.order.add_edge(ic, ca)
root.order.add_edge(ms, ca)

# Expert review and historical cross-referencing
root.order.add_edge(ec, ca)
root.order.add_edge(hc, ca)

# Legal verification
root.order.add_edge(lv, ca)

# Parallel registry search and customs clearance
root.order.add_edge(rs, cc)
root.order.add_edge(cc, cc2)

# Concurrency after condition assessment
root.order.add_edge(ca, dl)
root.order.add_edge(ca, cc2)

# Final report drafting and certification
root.order.add_edge(dl, rd)
root.order.add_edge(cc2, rd)
root.order.add_edge(rd, cert)

# Secure archival and auction preparation
root.order.add_edge(cert, sa)
root.order.add_edge(sa, ap)