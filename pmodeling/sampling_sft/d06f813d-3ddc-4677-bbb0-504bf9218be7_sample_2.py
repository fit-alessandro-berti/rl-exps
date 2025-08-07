import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Loop for multi-disciplinary testing: Sampling -> (Spectroscopy + Radiocarbon) -> Material Analysis
testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[ss, StrictPartialOrder(nodes=[st, rd, ma])])

# Parallelize expert consultation with forensic review
expert_choice = OperatorPOWL(operator=Operator.XOR, children=[ec, fr])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    pc, testing_loop, expert_choice, lv, oa, ra, iq, cr, doc, crv, fa
])

# Define control-flow dependencies
root.order.add_edge(pc, testing_loop)
root.order.add_edge(testing_loop, expert_choice)
root.order.add_edge(expert_choice, lv)
root.order.add_edge(lv, oa)
root.order.add_edge(oa, ra)
root.order.add_edge(ra, iq)
root.order.add_edge(iq, cr)
root.order.add_edge(cr, doc)
root.order.add_edge(doc, crv)
root.order.add_edge(crv, fa)