import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
rc = Transition(label='Radiocarbon Test')
dc = Transition(label='Database Query')
sc = Transition(label='Style Compare')
bp = Transition(label='Blockchain Prep')
lr = Transition(label='Legal Review')
oa = Transition(label='Ownership Audit')
cp = Transition(label='Conservation Plan')
ep = Transition(label='Expert Panel')
rd = Transition(label='Report Draft')
cr = Transition(label='Client Review')
asub = Transition(label='Authority Submit')
es = Transition(label='Exhibit Setup')
fa = Transition(label='Final Approval')

# Loop for concurrent analysis: Material Scan & Radiocarbon Test
loop_analysis = OperatorPOWL(operator=Operator.LOOP, children=[ms, rc])

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, loop_analysis, dc, sc,
    bp, lr, oa, cp,
    ep, rd, cr, asub, es, fa
])

# Add ordering constraints
root.order.add_edge(pc, loop_analysis)
root.order.add_edge(loop_analysis, dc)
root.order.add_edge(loop_analysis, sc)

# Parallel preparation before Expert Panel
root.order.add_edge(dc, bp)
root.order.add_edge(sc, bp)
root.order.add_edge(bp, lr)
root.order.add_edge(bp, oa)
root.order.add_edge(bp, cp)

# Sequence after Expert Panel
root.order.add_edge(ep, rd)
root.order.add_edge(rd, cr)
root.order.add_edge(cr, asub)
root.order.add_edge(asub, es)
root.order.add_edge(es, fa)