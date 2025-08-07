import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
pc = Transition(label='Provenance Check')
mt = Transition(label='Material Testing')
sr = Transition(label='Stylistic Review')
expert = Transition(label='Expert Panel')
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

# Loop for parallel material testing and stylistic review
loop_mt_sr = OperatorPOWL(operator=Operator.LOOP, children=[mt, sr])

# Build the partial order
root = StrictPartialOrder(nodes=[
    loop_mt_sr,
    expert,
    lc,
    ea,
    iq,
    ra,
    da,
    rb,
    tp,
    fr,
    ce,
    pn,
    cr
])

# Sequence of parallel testing and review before expert panel
root.order.add_edge(loop_mt_sr, expert)

# Parallel clearance and archive activities
root.order.add_edge(lc, da)
root.order.add_edge(ea, da)

# Parallel insurance quote and risk assessment
root.order.add_edge(iq, ra)

# After expert panel, parallel transport preparation and final review
root.order.add_edge(expert, tp)
root.order.add_edge(expert, fr)

# Final review then catalog entry
root.order.add_edge(fr, ce)

# Catalog entry then public notice
root.order.add_edge(ce, pn)

# Public notice then condition report
root.order.add_edge(pn, cr)