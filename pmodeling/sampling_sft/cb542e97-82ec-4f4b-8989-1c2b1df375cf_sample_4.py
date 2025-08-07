import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ai = Transition(label='Artifact Intake')
cc = Transition(label='Condition Check')
mt = Transition(label='Material Test')
asrch = Transition(label='Archival Search')
scmp = Transition(label='Style Compare')
er = Transition(label='Expert Review')
rc = Transition(label='Restoration Check')
pt = Transition(label='Provenance Trace')
lv = Transition(label='Legal Verify')
va = Transition(label='Value Appraise')
ce = Transition(label='Catalog Entry')
mp = Transition(label='Marketing Plan')
asup = Transition(label='Auction Setup')
cf = Transition(label='Certify Final')
sr = Transition(label='Sales Report')

# Build the partial order
root = StrictPartialOrder(nodes=[
    ai, cc, mt, asrch, scmp, er, rc, pt, lv, va, ce, mp, asup, cf, sr
])

# Intake -> Condition Check -> Material Test
root.order.add_edge(ai, cc)
root.order.add_edge(cc, mt)

# Material Test branches into archival search and style compare
root.order.add_edge(mt, asrch)
root.order.add_edge(mt, scmp)

# Both archival search and style compare feed into expert review
root.order.add_edge(asrch, er)
root.order.add_edge(scmp, er)

# Expert review feeds into restoration check
root.order.add_edge(er, rc)

# Restoration check feeds into provenance trace
root.order.add_edge(rc, pt)

# Provenance trace feeds into legal verify
root.order.add_edge(pt, lv)

# Legal verify feeds into value appraisal
root.order.add_edge(lv, va)

# Value appraisal feeds into catalog entry
root.order.add_edge(va, ce)

# Catalog entry feeds into marketing plan
root.order.add_edge(ce, mp)

# Marketing plan feeds into auction setup
root.order.add_edge(mp, asup)

# Auction setup feeds into certification and sales report
root.order.add_edge(asup, cf)
root.order.add_edge(asup, sr)

# Finally, certification and sales report are concurrent
# (no additional edges needed as they are already at the end)