import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
ai = Transition(label='Artifact Intake')
cc = Transition(label='Condition Check')
mt = Transition(label='Material Test')
asrch = Transition(label='Archival Search')
scompare = Transition(label='Style Compare')
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

# Loop for repeated style comparison and expert review
po_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[scompare, er]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ai, cc, mt, asrch, po_loop, rc, pt, lv, va, ce, mp, asup, cf, sr
])

# Define the control-flow edges
root.order.add_edge(ai, cc)
root.order.add_edge(cc, mt)
root.order.add_edge(cc, asrch)
root.order.add_edge(mt, po_loop)
root.order.add_edge(asrch, po_loop)
root.order.add_edge(po_loop, rc)
root.order.add_edge(rc, pt)
root.order.add_edge(pt, lv)
root.order.add_edge(lv, va)
root.order.add_edge(va, ce)
root.order.add_edge(ce, mp)
root.order.add_edge(mp, asup)
root.order.add_edge(asup, cf)
root.order.add_edge(cf, sr)