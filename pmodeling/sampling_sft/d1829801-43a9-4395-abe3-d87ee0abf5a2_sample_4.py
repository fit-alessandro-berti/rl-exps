import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
ai = Transition(label='Artifact Intake')
vi = Transition(label='Visual Inspection')
mt = Transition(label='Material Testing')
rd = Transition(label='Radiocarbon Dating')
pc = Transition(label='Provenance Check')
ar = Transition(label='Archive Research')
er = Transition(label='Expert Review')
sa = Transition(label='Style Analysis')
ca = Transition(label='Craftsmanship Eval')
cc = Transition(label='Condition Check')
rp = Transition(label='Restoration Plan')
fr = Transition(label='Forgery Risk')
lr = Transition(label='Legal Review')
rdg = Transition(label='Report Drafting')
ce = Transition(label='Catalog Entry')

# Loop for parallel provenance research and archival record check
provenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pc, ar]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    ai, vi, mt, rd,
    provenance_loop,
    er,
    sa, ca, cc,
    rp, fr, lr,
    rdg, ce
])

# Define the control-flow dependencies
root.order.add_edge(ai, vi)
root.order.add_edge(vi, mt)
root.order.add_edge(vi, rd)
root.order.add_edge(mt, provenance_loop)
root.order.add_edge(rd, provenance_loop)
root.order.add_edge(provenance_loop, er)
root.order.add_edge(er, sa)
root.order.add_edge(er, ca)
root.order.add_edge(er, cc)
root.order.add_edge(sa, rp)
root.order.add_edge(ca, rp)
root.order.add_edge(cc, rp)
root.order.add_edge(rp, fr)
root.order.add_edge(rp, lr)
root.order.add_edge(fr, rdg)
root.order.add_edge(lr, rdg)
root.order.add_edge(rdg, ce)