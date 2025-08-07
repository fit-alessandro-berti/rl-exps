import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ai = Transition(label='Artifact Intake')
ce = Transition(label='Catalog Entry')
vi = Transition(label='Visual Inspect')
mt = Transition(label='Material Test')
sp = Transition(label='Spectroscopy')
hc = Transition(label='Historical Check')
pr = Transition(label='Provenance Trace')
sc = Transition(label='Style Compare')
ts = Transition(label='3D Scanning')
ca = Transition(label='Condition Assess')
pp = Transition(label='Preservation Plan')
lr = Transition(label='Legal Review')
rd = Transition(label='Report Draft')
rf = Transition(label='Report Finalize')
ar = Transition(label='Archive Data')
sp2 = Transition(label='Sale Prep')

# Loop for repeated style compare
loop_compare = OperatorPOWL(operator=Operator.LOOP, children=[sc, pr])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ai, ce, vi, mt, sp, hc, loop_compare, ca, pp, lr, rd, rf, ar, sp2
])

# Sequence edges
root.order.add_edge(ai, ce)
root.order.add_edge(ce, vi)
root.order.add_edge(ce, mt)
root.order.add_edge(vi, sp)
root.order.add_edge(mt, sp)
root.order.add_edge(sp, hc)
root.order.add_edge(hc, loop_compare)
root.order.add_edge(loop_compare, ca)
root.order.add_edge(ca, pp)
root.order.add_edge(pp, lr)
root.order.add_edge(lr, rd)
root.order.add_edge(rd, rf)
root.order.add_edge(rf, ar)
root.order.add_edge(ar, sp2)