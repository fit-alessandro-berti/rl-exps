import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
pc = Transition(label='Provenance Check')
sc = Transition(label='Sample Collection')
sp = Transition(label='Spectroscopy Test')
cd = Transition(label='Carbon Dating')
er = Transition(label='Expert Review')
lc = Transition(label='Legal Clearance')
ca = Transition(label='Cultural Assessment')
ds = Transition(label='Digital Scan')
rd = Transition(label='Report Draft')
sm = Transition(label='Stakeholder Meet')
av = Transition(label='Acquisition Vote')
rp = Transition(label='Restoration Plan')
cr = Transition(label='Condition Report')
ae = Transition(label='Archival Entry')
fa = Transition(label='Final Approval')

# Loop for continuous scientific analysis: Spectroscopy Test then optionally Carbon Dating
analysis_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sp, cd]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, sc, analysis_loop, er, lc, ca, ca,
    ds, rd, sm, av, rp, cr, ae, fa
])

# Sequence of provenance check -> sample collection -> analysis loop
root.order.add_edge(pc, sc)
root.order.add_edge(sc, analysis_loop)

# After analysis loop, expert review and cultural assessment in parallel
root.order.add_edge(analysis_loop, er)
root.order.add_edge(analysis_loop, ca)

# Both expert review and cultural assessment then legal clearance
root.order.add_edge(er, lc)
root.order.add_edge(ca, lc)

# Legal clearance and digital scan in parallel
root.order.add_edge(lc, ds)

# Digital scan then report drafting
root.order.add_edge(ds, rd)

# Stakeholder meeting and acquisition vote in parallel
root.order.add_edge(rd, sm)
root.order.add_edge(rd, av)

# After meeting and vote, restoration plan and condition report
root.order.add_edge(sm, rp)
root.order.add_edge(av, cr)

# Both restoration and condition reports then archival entry
root.order.add_edge(rp, ae)
root.order.add_edge(cr, ae)

# Finally, archival entry and final approval
root.order.add_edge(ae, fa)