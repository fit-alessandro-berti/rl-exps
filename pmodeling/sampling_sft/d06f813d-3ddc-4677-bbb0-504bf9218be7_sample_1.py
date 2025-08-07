import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
pc   = Transition(label='Provenance Check')
ss   = Transition(label='Specimen Sampling')
st   = Transition(label='Spectroscopy Test')
rd   = Transition(label='Radiocarbon Date')
ma   = Transition(label='Material Analysis')
fr   = Transition(label='Forensic Review')
ec   = Transition(label='Expert Consult')
lv   = Transition(label='Legal Verify')
oa   = Transition(label='Ownership Audit')
ra   = Transition(label='Risk Assess')
iq   = Transition(label='Insurance Quote')
cr   = Transition(label='Condition Report')
doc  = Transition(label='Documentation')
crv  = Transition(label='Committee Review')
fa   = Transition(label='Final Approval')

# Define the loop for expert review and forensic analysis
expert_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[ec, fr]
)

# Define the loop for legal verification and ownership audit
legal_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[lv, oa]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    pc, ss, st, rd, ma, expert_loop,
    legal_loop, ra, iq, cr, doc,
    crv, fa
])

# Add the control-flow dependencies
root.order.add_edge(pc, ss)
root.order.add_edge(ss, st)
root.order.add_edge(ss, rd)
root.order.add_edge(st, expert_loop)
root.order.add_edge(rd, expert_loop)
root.order.add_edge(expert_loop, legal_loop)
root.order.add_edge(legal_loop, ra)
root.order.add_edge(ra, iq)
root.order.add_edge(iq, cr)
root.order.add_edge(cr, doc)
root.order.add_edge(doc, crv)
root.order.add_edge(crv, fa)