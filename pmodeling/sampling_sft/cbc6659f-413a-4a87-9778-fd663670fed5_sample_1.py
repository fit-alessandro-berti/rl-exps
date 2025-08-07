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

# Loop for risk assessment and ethics approval (until exit)
loop = OperatorPOWL(operator=Operator.LOOP, children=[ra, ea])

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, ms, er, la, cr, cd, ov, hm, cc, loop, rp, fa, ce, ep
])

# Add control-flow edges
root.order.add_edge(pc, ms)
root.order.add_edge(ms, er)
root.order.add_edge(er, la)
root.order.add_edge(la, cr)
root.order.add_edge(cr, cd)
root.order.add_edge(cd, ov)
root.order.add_edge(ov, hm)
root.order.add_edge(hm, cc)
root.order.add_edge(cc, loop)
root.order.add_edge(loop, rp)
root.order.add_edge(rp, fa)
root.order.add_edge(fa, ce)
root.order.add_edge(ce, ep)