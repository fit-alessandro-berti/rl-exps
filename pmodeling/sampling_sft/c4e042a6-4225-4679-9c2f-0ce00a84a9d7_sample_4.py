import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ms = Transition(label='Material Sourcing')
sa = Transition(label='Supplier Audit')
cv = Transition(label='Credential Verify')
dc = Transition(label='Design Concept')
pb = Transition(label='Prototype Build')
qr = Transition(label='Quality Review')
aa = Transition(label='Artisan Assign')
bs = Transition(label='Batch Scheduling')
ca = Transition(label='Custom Approvals')
ia = Transition(label='Inventory Adjust')
ps = Transition(label='Production Sync')
sp = Transition(label='Shipping Plan')
cc = Transition(label='Compliance Check')
fl = Transition(label='Feedback Loop')
mt = Transition(label='Market Target')
of = Transition(label='Order Fulfill')
ce = Transition(label='Customer Engage')
s = Transition(label='Sustainability')

# Define the production branch: Design -> Prototype -> Quality Review -> Artisan Assign -> Batch Scheduling
production_branch = StrictPartialOrder(nodes=[dc, pb, qr, aa, bs])
production_branch.order.add_edge(dc, pb)
production_branch.order.add_edge(pb, qr)
production_branch.order.add_edge(qr, aa)
production_branch.order.add_edge(aa, bs)

# Define the feedback loop: repeat Feedback Loop -> Customer Engage -> Sustainability
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[fl, ce, s])

# Assemble the overall process
root = StrictPartialOrder(nodes=[
    ms, sa, cv, production_branch, ca, ia, ps, sp, cc, feedback_loop, mt, of
])

# Sequential flow: Material Sourcing -> Supplier Audit -> Credential Verify -> Production Branch -> Custom Approvals -> Inventory Adjust
root.order.add_edge(ms, sa)
root.order.add_edge(sa, cv)
root.order.add_edge(cv, production_branch)
root.order.add_edge(production_branch, ca)
root.order.add_edge(ca, ia)
root.order.add_edge(ia, ps)
root.order.add_edge(ps, sp)
root.order.add_edge(sp, cc)

# Parallel feedback: after Production Sync, enter the feedback loop
root.order.add_edge(ps, feedback_loop)

# After the loop, Market Target -> Order Fulfill
root.order.add_edge(feedback_loop, mt)
root.order.add_edge(mt, of)