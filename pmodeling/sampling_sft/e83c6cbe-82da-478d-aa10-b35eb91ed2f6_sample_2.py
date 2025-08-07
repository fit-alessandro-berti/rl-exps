import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
pc = Transition(label='Provenance Check')
mt = Transition(label='Material Testing')
sr = Transition(label='Stylistic Review')
ep = Transition(label='Expert Panel')
lc = Transition(label='Legal Clearance')
ea = Transition(label='Ethics Audit')
iq = Transition(label='Insurance Quote')
ra = Transition(label='Risk Assess')
da = Transition(label='Digital Archive')
rb = Transition(label='Replica Build')
tp = Transition(label='Transport Prep')
fr = Transition(label='Final Review')
ce = Transition(label='Catalog Entry')
pn = Transition(label='Public Notice')
cr = Transition(label='Condition Report')

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, mt, sr, ep,
    lc, ea,
    iq, ra,
    da, rb, tp,
    fr, ce, pn, cr
])

# Initial provenance research and material testing are concurrent
root.order.add_edge(pc, mt)
root.order.add_edge(pc, sr)

# After provenance and material, proceed to expert panel
root.order.add_edge(mt, ep)
root.order.add_edge(sr, ep)

# Expert panel outputs feed into all other branches
for child in [lc, ea, iq, ra, da, rb, tp, fr, ce, pn, cr]:
    root.order.add_edge(ep, child)

# Legal clearance and ethics audit can proceed in parallel after expert panel
for child in [lc, ea]:
    root.order.add_edge(ep, child)

# Insurance quote and risk assessment can proceed in parallel after expert panel
for child in [iq, ra]:
    root.order.add_edge(ep, child)

# Digital archive, replica build, and transport prep can proceed in parallel after expert panel
for child in [da, rb, tp]:
    root.order.add_edge(ep, child)

# Final review feeds into catalog entry, public notice, and condition report
for child in [ce, pn, cr]:
    root.order.add_edge(fr, child)