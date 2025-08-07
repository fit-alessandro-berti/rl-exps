import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
lc = Transition(label='Local Cooperatives')
ea = Transition(label='Environmental Audit')
el = Transition(label='Ethical Logistics')
gs = Transition(label='Global Shipping')
fc = Transition(label='Feedback Collection')

# Define the feedback collection loop: do Feedback Collection, then either exit or do all the previous steps and repeat
loop_body = StrictPartialOrder(nodes=[ea, el, gs, fc])
loop_body.order.add_edge(ea, el)
loop_body.order.add_edge(el, gs)
loop_body.order.add_edge(gs, fc)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[fc, loop_body])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ms, cv, et, bst, ca, pc, pcat, cm, ct, pa, lc, feedback_loop
])

# Define the control-flow dependencies
root.order.add_edge(ms, cv)
root.order.add_edge(cv, et)
root.order.add_edge(et, bst)
root.order.add_edge(bst, ca)
root.order.add_edge(ca, pc)
root.order.add_edge(pc, pcat)
root.order.add_edge(pcat, cm)
root.order.add_edge(cm, ct)
root.order.add_edge(ct, pa)
root.order.add_edge(pa, lc)
root.order.add_edge(lc, feedback_loop)