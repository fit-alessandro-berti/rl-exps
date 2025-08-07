import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
intake = Transition(label='Artifact Intake')
vi = Transition(label='Visual Inspection')
mt = Transition(label='Material Testing')
rd = Transition(label='Radiocarbon Dating')
pc = Transition(label='Provenance Check')
ar = Transition(label='Archive Research')
ec = Transition(label='Expert Review')
sa = Transition(label='Style Analysis')
ca = Transition(label='Craftsmanship Eval')
cc = Transition(label='Condition Check')
rp = Transition(label='Restoration Plan')
fr = Transition(label='Forgery Risk')
lr = Transition(label='Legal Review')
rdraft = Transition(label='Report Drafting')
ce = Transition(label='Catalog Entry')

# Build the loop body: Style Analysis -> Craftsmanship Eval -> Condition Check -> Restoration Plan
body = StrictPartialOrder(nodes=[sa, ca, cc, rp])
body.order.add_edge(sa, ca)
body.order.add_edge(ca, cc)
body.order.add_edge(cc, rp)

# LOOP: Provenance Check, Archive Research, Expert Review, then body
loop = OperatorPOWL(operator=Operator.LOOP, children=[pc, ar, ec, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    intake, vi, mt, rd, loop, fr, lr, rdraft, ce
])
root.order.add_edge(intake, vi)
root.order.add_edge(vi, mt)
root.order.add_edge(mt, rd)
root.order.add_edge(rd, loop)
root.order.add_edge(loop, fr)
root.order.add_edge(fr, lr)
root.order.add_edge(lr, rdraft)
root.order.add_edge(rdraft, ce)