import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Material Sourcing')
cv = Transition(label='Cultural Verify')
et = Transition(label='Eco Transport')
bs = Transition(label='Batch Storytelling')
ca = Transition(label='Craftsman Assignment')
pc = Transition(label='Product Creation')
pcatalog = Transition(label='Provenance Catalog')
cm = Transition(label='Community Marketing')
ct = Transition(label='Collector Targeting')
pa = Transition(label='Package Assembly')
lc = Transition(label='Local Cooperatives')
ea = Transition(label='Environmental Audit')
el = Transition(label='Ethical Logistics')
gs = Transition(label='Global Shipping')
fc = Transition(label='Feedback Collection')

# Loop for continuous feedback collection
loop = OperatorPOWL(operator=Operator.LOOP, children=[fc, fc])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, cv, et, bs, ca, pc, pcatalog,
    cm, ct, pa, lc, ea, el, gs, loop
])

# Material sourcing, verify, transport, storytelling, assignment
root.order.add_edge(ms, cv)
root.order.add_edge(cv, et)

# After transport, do storytelling and assignment in parallel
root.order.add_edge(et, bs)
root.order.add_edge(et, ca)

# After storytelling and assignment, proceed to product creation
root.order.add_edge(bs, pc)
root.order.add_edge(ca, pc)

# Catalog provenance after product creation
root.order.add_edge(pc, pcatalog)

# Marketing and targeting after cataloging
root.order.add_edge(pcatalog, cm)
root.order.add_edge(pcatalog, ct)

# Assembly, local cooperatives, audits, logistics, shipping in parallel
root.order.add_edge(cm, pa)
root.order.add_edge(ct, pa)
root.order.add_edge(pa, lc)
root.order.add_edge(pa, ea)
root.order.add_edge(pa, el)

# Loop for continuous feedback collection
root.order.add_edge(lc, loop)
root.order.add_edge(ea, loop)
root.order.add_edge(el, loop)

# Finally, global shipping after feedback loop
root.order.add_edge(loop, gs)