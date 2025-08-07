import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
pc = Transition(label='Provenance Check')
ms = Transition(label='Material Scan')
er = Transition(label='Expert Review')
la = Transition(label='Legal Audit')
cr = Transition(label='Condition Report')
cd = Transition(label='Carbon Dating')
ov = Transition(label='Ownership Verify')
hm = Transition(label='Historical Match')
cc = Transition(label='Customs Clearance')
ra = Transition(label='Risk Assessment')
ea = Transition(label='Ethics Approval')
rp = Transition(label='Restoration Plan')
fa = Transition(label='Final Approval')
ce = Transition(label='Catalog Entry')
ep = Transition(label='Exhibit Prep')

# Silent transition for optional restoration
skip = SilentTransition()

# Optional restoration branch: Restoration Plan -> Exhibit Prep
rest_branch = StrictPartialOrder(nodes=[rp, ep])
rest_branch.order.add_edge(rp, ep)

# Loop for optional restoration: repeat Restoration Plan -> Exhibit Prep until exit
loop_rest = OperatorPOWL(operator=Operator.LOOP, children=[rp, skip])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    pc, ms, er, la, cr, cd, ov, hm, cc, ra, ea, loop_rest, fa, ce
])

# Main sequence
root.order.add_edge(pc, ms)
root.order.add_edge(ms, er)
root.order.add_edge(er, la)
root.order.add_edge(la, cr)
root.order.add_edge(cr, cd)
root.order.add_edge(cd, ov)
root.order.add_edge(ov, hm)
root.order.add_edge(hm, cc)
root.order.add_edge(cc, ra)
root.order.add_edge(ra, ea)
root.order.add_edge(ea, loop_rest)

# Optional restoration after all other activities
root.order.add_edge(loop_rest, fa)

# Final catalog entry after approval
root.order.add_edge(fa, ce)