import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
pc = Transition(label='Provenance Check')
ss = Transition(label='Specimen Sampling')
st = Transition(label='Spectroscopy Test')
rd = Transition(label='Radiocarbon Date')
ma = Transition(label='Material Analysis')
fr = Transition(label='Forensic Review')
ec = Transition(label='Expert Consult')
lv = Transition(label='Legal Verify')
oa = Transition(label='Ownership Audit')
ra = Transition(label='Risk Assess')
iq = Transition(label='Insurance Quote')
cr = Transition(label='Condition Report')
doc = Transition(label='Documentation')
crv = Transition(label='Committee Review')
fa = Transition(label='Final Approval')

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, ss, st, rd, ma, fr,
    ec, lv, oa, ra, iq,
    cr, doc, crv, fa
])

# Define the control-flow dependencies
# Initial research and sampling
root.order.add_edge(pc, ss)
root.order.add_edge(ss, st)
root.order.add_edge(ss, rd)
root.order.add_edge(ss, ma)

# Follow-up analyses
root.order.add_edge(st, fr)
root.order.add_edge(rd, fr)
root.order.add_edge(ma, fr)

# Expert consultation and legal verify in parallel
root.order.add_edge(fr, ec)
root.order.add_edge(fr, lv)

# Audit and risk assessment in parallel
root.order.add_edge(ec, oa)
root.order.add_edge(lv, oa)
root.order.add_edge(oa, ra)

# Insurance and condition report in parallel
root.order.add_edge(oa, iq)
root.order.add_edge(oa, cr)

# Final documentation and committee review
root.order.add_edge(iq, cr)
root.order.add_edge(cr, doc)
root.order.add_edge(doc, crv)

# Final approval
root.order.add_edge(crv, fa)