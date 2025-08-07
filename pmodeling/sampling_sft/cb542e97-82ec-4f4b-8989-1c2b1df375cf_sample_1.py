import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ai = Transition(label='Artifact Intake')
cc = Transition(label='Condition Check')
mt = Transition(label='Material Test')
asrch = Transition(label='Archival Search')
scomp = Transition(label='Style Compare')
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

# Loop for continuous expert review and archival search
expert_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[er, asrch]
)

# Loop for continuous style comparison and material testing
style_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[scomp, mt]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    ai, cc, style_loop,
    mt, asrch,
    expert_loop, er,
    rc,
    pt, lv, va, ce, mp, asup,
    cf, sr
])

# Define the control-flow dependencies
root.order.add_edge(ai, cc)
root.order.add_edge(cc, style_loop)

root.order.add_edge(style_loop, rc)

root.order.add_edge(rc, mt)
root.order.add_edge(mt, asrch)

root.order.add_edge(asrch, expert_loop)
root.order.add_edge(expert_loop, er)

root.order.add_edge(er, pt)
root.order.add_edge(er, lv)
root.order.add_edge(er, va)
root.order.add_edge(er, ce)
root.order.add_edge(er, mp)
root.order.add_edge(er, asup)

root.order.add_edge(pt, lv)
root.order.add_edge(lv, va)
root.order.add_edge(va, ce)
root.order.add_edge(ce, mp)
root.order.add_edge(mp, asup)

root.order.add_edge(asup, cf)
root.order.add_edge(cf, sr)