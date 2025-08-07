import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Build the loop for multi-modal analysis: spectroscopy then carbon dating
analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[sp, cd])

# Build the stakeholder review loop: one meeting, then optionally another
stakeholder_loop = OperatorPOWL(operator=Operator.LOOP, children=[sm, av])

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, sc, analysis_loop,
    ca, er,
    lc,
    ds, rd,
    stakeholder_loop,
    rp, cr, ae, fa
])

# Define the control-flow dependencies
root.order.add_edge(pc, sc)
root.order.add_edge(sc, analysis_loop)

# Analysis loop body
root.order.add_edge(analysis_loop, ca)
root.order.add_edge(analysis_loop, er)

# After analysis and expert review, go to legal and cultural assessment
root.order.add_edge(ca, lc)
root.order.add_edge(er, lc)

# Legal and cultural assessment then to digital scan
root.order.add_edge(lc, ds)

# Digital scan then report draft
root.order.add_edge(ds, rd)

# Stakeholder loop body
root.order.add_edge(stakeholder_loop, rp)
root.order.add_edge(stakeholder_loop, cr)
root.order.add_edge(stakeholder_loop, ae)
root.order.add_edge(stakeholder_loop, fa)

# After report draft, do restoration plan
root.order.add_edge(rd, rp)

# After restoration plan, do condition report, archival entry, and final approval
root.order.add_edge(rp, cr)
root.order.add_edge(rp, ae)
root.order.add_edge(cr, fa)