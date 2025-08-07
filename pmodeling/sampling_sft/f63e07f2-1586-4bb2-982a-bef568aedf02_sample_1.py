import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ai = Transition(label='Artifact Intake')
pc = Transition(label='Provenance Check')
ar = Transition(label='Archive Research')
ei = Transition(label='Expert Interview')
ma = Transition(label='Material Analysis')
st1 = Transition(label='Spectroscopy Test')
cd = Transition(label='Carbon Dating')
di = Transition(label='Digital Imaging')
m3d = Transition(label='3D Modeling')
dr = Transition(label='Data Review')
cm = Transition(label='Consensus Meeting')
cp = Transition(label='Conservation Plan')
ps = Transition(label='Preservation Setup')
doc = Transition(label='Documentation')
ep = Transition(label='Exhibition Prep')

# Build the partial order
root = StrictPartialOrder(nodes=[
    ai, pc, ar, ei,
    ma, st1, cd,
    di, m3d,
    dr, cm,
    cp, ps,
    doc, ep
])

# Order dependencies
root.order.add_edge(ai, pc)
root.order.add_edge(pc, ar)
root.order.add_edge(pc, ei)

root.order.add_edge(ar, ma)
root.order.add_edge(ei, ma)

root.order.add_edge(ma, st1)
root.order.add_edge(ma, cd)

root.order.add_edge(st1, dr)
root.order.add_edge(cd, dr)

root.order.add_edge(dr, cm)

root.order.add_edge(cm, cp)
root.order.add_edge(cm, ps)

root.order.add_edge(cp, doc)
root.order.add_edge(ps, doc)

root.order.add_edge(doc, ep)