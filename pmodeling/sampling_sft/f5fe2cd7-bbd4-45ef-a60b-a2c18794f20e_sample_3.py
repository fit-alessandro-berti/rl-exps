import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
rc = Transition(label='Radiocarbon Test')
sr = Transition(label='Stylistic Review')
ec = Transition(label='Expert Consult')
da = Transition(label='Document Audit')
lv = Transition(label='Legal Verify')
cr = Transition(label='Condition Report')
df = Transition(label='Discrepancy Flag')
re = Transition(label='Re-examination')
asrc = Transition(label='Alternative Source')
av = Transition(label='Acquisition Vote')
ce = Transition(label='Catalog Entry')
ep = Transition(label='Exhibit Plan')
fa = Transition(label='Final Approval')

# Build the loop body for discrepancy handling: Re-examination -> Alternative Source
loop_body = StrictPartialOrder(nodes=[re, asrc])
loop_body.order.add_edge(re, asrc)

# Define the loop: Discrepancy Flag -> loop_body, then exit or repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[df, loop_body])

# Build the final approval path: Acquisition Vote -> Catalog Entry -> Exhibit Plan -> Final Approval
final_path = StrictPartialOrder(nodes=[av, ce, ep, fa])
final_path.order.add_edge(av, ce)
final_path.order.add_edge(ce, ep)
final_path.order.add_edge(ep, fa)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    pc, ms, rc, sr, ec, da, lv, cr, loop, final_path
])

# Add the control-flow edges
root.order.add_edge(pc, ms)
root.order.add_edge(pc, rc)
root.order.add_edge(ms, sr)
root.order.add_edge(rc, sr)
root.order.add_edge(sr, ec)
root.order.add_edge(ec, da)
root.order.add_edge(da, lv)
root.order.add_edge(lv, cr)
root.order.add_edge(cr, loop)
root.order.add_edge(loop, final_path)

# Final edges for the discrepancy handling loop
root.order.add_edge(df, loop)

# Final edge for the final approval path
root.order.add_edge(loop, final_path)