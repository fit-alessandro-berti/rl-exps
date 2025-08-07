import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
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

# Build the loop body: Quality Review -> Compliance Check -> Inventory Adjust -> Production Sync -> Shipping Plan
loop_body = StrictPartialOrder(nodes=[qr, cc, ia, ps, sp])
loop_body.order.add_edge(qr, cc)
loop_body.order.add_edge(cc, ia)
loop_body.order.add_edge(ia, ps)
loop_body.order.add_edge(ps, sp)

# Define the adaptive inventory adjustment loop: Artisan Assign -> Batch Scheduling -> Custom Approvals -> loop_body
loop_adaptive = OperatorPOWL(operator=Operator.LOOP, children=[aa, bs, ca, loop_body])

# Assemble the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    ms, sa, cv, dc, pb, loop_adaptive,
    fl, mt, of, se, ce
])

# Define the control-flow dependencies
root.order.add_edge(ms, sa)
root.order.add_edge(sa, cv)
root.order.add_edge(cv, dc)
root.order.add_edge(dc, pb)

root.order.add_edge(pb, loop_adaptive)

# Feedback loop branches after the adaptive inventory adjustment
root.order.add_edge(loop_adaptive, fl)

# Target marketing and order fulfillment after feedback
root.order.add_edge(fl, mt)
root.order.add_edge(mt, of)

# Sustainability and customer engagement at the end
root.order.add_edge(of, se)
root.order.add_edge(se, ce)