import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
rt = Transition(label='Radiocarbon Test')
dc = Transition(label='Database Query')
sp = Transition(label='Style Compare')
bp = Transition(label='Blockchain Prep')
lr = Transition(label='Legal Review')
oa = Transition(label='Ownership Audit')
cp = Transition(label='Conservation Plan')
ep = Transition(label='Expert Panel')
rd = Transition(label='Report Draft')
cr = Transition(label='Client Review')
asub = Transition(label='Authority Submit')
eset = Transition(label='Exhibit Setup')
fa = Transition(label='Final Approval')

# Build the partial‐order sub‐model for the expert panel and validation
panel_po = StrictPartialOrder(nodes=[ep, rd, cr, asub, eset, fa])
panel_po.order.add_edge(ep, rd)
panel_po.order.add_edge(rd, cr)
panel_po.order.add_edge(cr, asub)
panel_po.order.add_edge(asub, eset)
panel_po.order.add_edge(eset, fa)

# Main workflow: concurrent material analysis, followed by expert validation
main_po = StrictPartialOrder(nodes=[pc, ms, rt, dc, sp, bp, lr, oa, cp])
main_po.order.add_edge(pc, ms)
main_po.order.add_edge(pc, rt)
main_po.order.add_edge(ms, dc)
main_po.order.add_edge(rt, dc)
main_po.order.add_edge(dc, sp)
main_po.order.add_edge(sp, bp)
main_po.order.add_edge(bp, lr)
main_po.order.add_edge(lr, oa)
main_po.order.add_edge(oa, cp)

# Final choice: either Exhibit Setup or Final Approval (no choice)
final_choice = OperatorPOWL(operator=Operator.XOR, children=[eset, fa])

# Assemble the overall process as a partial order
root = StrictPartialOrder(nodes=[main_po, panel_po, final_choice])
root.order.add_edge(main_po, panel_po)
root.order.add_edge(panel_po, final_choice)