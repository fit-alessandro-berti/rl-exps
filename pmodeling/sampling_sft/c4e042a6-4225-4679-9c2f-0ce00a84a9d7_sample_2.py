import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
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
se = Transition(label='Sustainability')
ce = Transition(label='Customer Engage')

# Define the production loop: do Prototype Build then Quality Review, repeat until exit
production_loop = OperatorPOWL(operator=Operator.LOOP, children=[pb, qr])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    ms, sa, cv, dc, production_loop, ca, bs, ia, cc,
    sp, fl, mt, of, se, ce
])

# Define the control‐flow dependencies
root.order.add_edge(ms, sa)
root.order.add_edge(sa, cv)
root.order.add_edge(cv, dc)
root.order.add_edge(dc, production_loop)
root.order.add_edge(production_loop, ca)
root.order.add_edge(ca, bs)
root.order.add_edge(bs, ia)
root.order.add_edge(ia, cc)
root.order.add_edge(cc, sp)
root.order.add_edge(sp, fl)
root.order.add_edge(fl, mt)
root.order.add_edge(mt, of)
root.order.add_edge(of, se)
root.order.add_edge(se, ce)