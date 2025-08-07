import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ms = Transition(label='Material Sourcing')
bh = Transition(label='Botanical Harvest')
ep = Transition(label='Extraction Phase')
ab = Transition(label='Accord Blending')
ot = Transition(label='Olfactory Testing')
ap = Transition(label='Aging Process')
sc = Transition(label='Stability Check')
sp = Transition(label='Sensory Panel')
ld = Transition(label='Label Design')
bc = Transition(label='Bottle Crafting')
bm = Transition(label='Batch Mixing')
qr = Transition(label='Quality Review')
pf = Transition(label='Packaging Final')
iu = Transition(label='Inventory Update')
ml = Transition(label='Market Launch')

# Loop for iterative olfactory testing
loop = OperatorPOWL(operator=Operator.LOOP, children=[ot, sp])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, bh, ep, ab, loop, sc, ld, bc, bm, qr, pf, iu, ml
])

# Define the control-flow dependencies
root.order.add_edge(ms, bh)
root.order.add_edge(bh, ep)
root.order.add_edge(ep, ab)
root.order.add_edge(ab, loop)
root.order.add_edge(loop, sc)
root.order.add_edge(sc, ld)
root.order.add_edge(ld, bc)
root.order.add_edge(bc, bm)
root.order.add_edge(bm, qr)
root.order.add_edge(qr, pf)
root.order.add_edge(pf, iu)
root.order.add_edge(iu, ml)