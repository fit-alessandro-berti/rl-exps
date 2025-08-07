import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
pc = Transition(label='Provenance Check')
rt = Transition(label='Radiocarbon Test')
ma = Transition(label='Material Analysis')
ms = Transition(label='Microscopic Scan')
er = Transition(label='Expert Review')
cv = Transition(label='Context Validation')
la = Transition(label='Legal Audit')
ev = Transition(label='Export Verify')
di = Transition(label='Digital Imaging')
md = Transition(label='3D Modeling')
cm = Transition(label='Consensus Meeting')
fa = Transition(label='Final Approval')
ce = Transition(label='Catalog Entry')
vs = Transition(label='Virtual Setup')
ab = Transition(label='Archival Backup')

# Build the scientific analysis partial order
analysis_po = StrictPartialOrder(nodes=[rt, ma, ms])
analysis_po.order.add_edge(rt, ma)
analysis_po.order.add_edge(rt, ms)

# Build the expert consultation partial order
expert_po = StrictPartialOrder(nodes=[er, cv])
expert_po.order.add_edge(er, cv)

# Build the legal audit partial order
legal_po = StrictPartialOrder(nodes=[la, ev])
legal_po.order.add_edge(la, ev)

# Build the virtual setup partial order
virtual_po = StrictPartialOrder(nodes=[di, md, vs])
virtual_po.order.add_edge(di, md)
virtual_po.order.add_edge(di, vs)

# Build the archival backup partial order
archival_po = StrictPartialOrder(nodes=[ab])
# No edges => silent

# Build the consensus meeting partial order
consensus_po = StrictPartialOrder(nodes=[cm])
# No edges => silent

# Build the final approval partial order
final_po = StrictPartialOrder(nodes=[fa, ce])
final_po.order.add_edge(fa, ce)

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    pc,
    analysis_po,
    expert_po,
    legal_po,
    virtual_po,
    archival_po,
    consensus_po,
    final_po
])

# Define the control-flow dependencies
root.order.add_edge(pc, analysis_po)
root.order.add_edge(pc, expert_po)
root.order.add_edge(pc, legal_po)
root.order.add_edge(pc, virtual_po)
root.order.add_edge(pc, archival_po)

# Loop for consensus meeting
root.order.add_edge(analysis_po, consensus_po)
root.order.add_edge(expert_po, consensus_po)
root.order.add_edge(legal_po, consensus_po)
root.order.add_edge(virtual_po, consensus_po)
root.order.add_edge(archival_po, consensus_po)

# Final approval after consensus
root.order.add_edge(consensus_po, final_po)

# Catalog entry after final approval
root.order.add_edge(final_po, ce)