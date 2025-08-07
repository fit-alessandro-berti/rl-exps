import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
ms = Transition(label='Material Sourcing')
cv = Transition(label='Cultural Verify')
et = Transition(label='Eco Transport')
bst = Transition(label='Batch Storytelling')
ca = Transition(label='Craftsman Assignment')
pc = Transition(label='Product Creation')
pcat = Transition(label='Provenance Catalog')
cm = Transition(label='Community Marketing')
ct = Transition(label='Collector Targeting')
pa = Transition(label='Package Assembly')
lo = Transition(label='Local Cooperatives')
ea = Transition(label='Environmental Audit')
el = Transition(label='Ethical Logistics')
gs = Transition(label='Global Shipping')
fc = Transition(label='Feedback Collection')

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    ms, cv, et, bst, ca, pc, pcat, cm, ct, pa, lo, ea, el, gs, fc
])

# Define the control‐flow dependencies
root.order.add_edge(ms, cv)
root.order.add_edge(cv, et)
root.order.add_edge(et, bst)
root.order.add_edge(bst, ca)
root.order.add_edge(ca, pc)
root.order.add_edge(pc, pcat)
root.order.add_edge(pcat, cm)
root.order.add_edge(cm, ct)
root.order.add_edge(ct, pa)
root.order.add_edge(pa, lo)
root.order.add_edge(lo, ea)
root.order.add_edge(ea, el)
root.order.add_edge(el, gs)
root.order.add_edge(gs, fc)

# The process ends with feedback collection
# no outgoing edges from fc

print(root)