import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
ir = Transition(label='Intake Review')
vi = Transition(label='Visual Inspect')
mt = Transition(label='Material Test')
pc = Transition(label='Provenance Check')
asrch = Transition(label='Archival Search')
ec = Transition(label='Expert Consult')
ds = Transition(label='Digital Scan')
cr = Transition(label='Condition Report')
fa = Transition(label='Forgery Assess')
lr = Transition(label='Legal Review')
ra = Transition(label='Risk Analysis')
av = Transition(label='Acquisition Vote')
ce = Transition(label='Catalog Entry')
sp = Transition(label='Storage Prep')
fa2 = Transition(label='Final Approval')

# Define the expert consultation and forgery assessment as a choice
expert_xor = OperatorPOWL(operator=Operator.XOR, children=[ec, fa])

# Build the partial order
root = StrictPartialOrder(nodes=[
    ir, vi, mt, pc, asrch, expert_xor, ds, cr, lr, ra, av, ce, sp, fa2
])

# Initial intake and inspection
root.order.add_edge(ir, vi)
root.order.add_edge(ir, mt)

# After inspection, run provenance check and archival search in parallel
root.order.add_edge(vi, pc)
root.order.add_edge(vi, asrch)

# Both provenance and archival search results feed into the expert choice
root.order.add_edge(pc, expert_xor)
root.order.add_edge(asrch, expert_xor)

# Expert consultation or forgery assessment follows the choice
root.order.add_edge(expert_xor, ds)

# Condition report and risk analysis proceed from the digital scan
root.order.add_edge(ds, cr)
root.order.add_edge(ds, ra)

# Acquisition vote depends on both condition and risk analysis
root.order.add_edge(cr, av)
root.order.add_edge(ra, av)

# After vote, catalog entry and storage prep proceed
root.order.add_edge(av, ce)
root.order.add_edge(av, sp)

# Final approval follows both catalog entry and storage prep
root.order.add_edge(ce, fa2)
root.order.add_edge(sp, fa2)