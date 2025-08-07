import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
init    = Transition(label='Initial Inquiry')
doc     = Transition(label='Document Review')
hist    = Transition(label='Historical Research')
sample  = Transition(label='Material Sampling')
test    = Transition(label='Forensic Testing')
own     = Transition(label='Ownership Audit')
legal   = Transition(label='Legal Verification')
eth     = Transition(label='Ethical Screening')
expert  = Transition(label='Expert Consultation')
cultural= Transition(label='Cultural Assessment')
cond    = Transition(label='Condition Survey')
proven  = Transition(label='Provenance Mapping')
risk    = Transition(label='Risk Analysis')
report  = Transition(label='Report Compilation')
approval= Transition(label='Acquisition Approval')
repatri = Transition(label='Repatriation Review')
archive = Transition(label='Archival Storage')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    init, doc, hist, sample, test, own, legal, eth,
    expert, cultural, cond, proven, risk,
    report, approval, repatri, archive
])

# Define the control‐flow dependencies
root.order.add_edge(init, doc)
root.order.add_edge(doc, hist)
root.order.add_edge(hist, sample)
root.order.add_edge(sample, test)
root.order.add_edge(test, own)
root.order.add_edge(own, legal)
root.order.add_edge(legal, eth)
root.order.add_edge(eth, expert)
root.order.add_edge(expert, cultural)
root.order.add_edge(cultural, cond)
root.order.add_edge(cond, proven)
root.order.add_edge(proven, risk)
root.order.add_edge(risk, report)

# Choice for acquisition or repatriation
choice = OperatorPOWL(operator=Operator.XOR, children=[approval, repatri])
root.order.add_edge(report, choice)

# Final archival storage after either choice
root.order.add_edge(choice, archive)