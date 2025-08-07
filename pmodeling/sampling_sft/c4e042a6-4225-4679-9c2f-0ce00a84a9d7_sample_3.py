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
se = Transition(label='Sustainability')
ce = Transition(label='Customer Engage')

# Build the production & fulfillment partial order
prod_po = StrictPartialOrder(nodes=[
    dc, pb, qr, aa, bs, ca, ia, ps, sp, cc, fl
])
prod_po.order.add_edge(dc, pb)
prod_po.order.add_edge(pb, qr)
prod_po.order.add_edge(qr, aa)
prod_po.order.add_edge(aa, ca)
prod_po.order.add_edge(ca, bs)
prod_po.order.add_edge(bs, ia)
prod_po.order.add_edge(ia, ps)
prod_po.order.add_edge(ps, sp)
prod_po.order.add_edge(sp, cc)
prod_po.order.add_edge(cc, fl)

# Build the marketing & customer engagement partial order
marketing_po = StrictPartialOrder(nodes=[mt, of, se])
marketing_po.order.add_edge(mt, of)
marketing_po.order.add_edge(of, se)

# Build the main process as a choice between production & marketing
main_choice = OperatorPOWL(operator=Operator.XOR, children=[prod_po, marketing_po])

# Assemble the overall root process
root = StrictPartialOrder(nodes=[
    ms, sa, cv, main_choice, ce
])
root.order.add_edge(ms, sa)
root.order.add_edge(sa, cv)
root.order.add_edge(cv, main_choice)
root.order.add_edge(main_choice, ce)