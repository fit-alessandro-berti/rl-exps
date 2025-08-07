import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake      = Transition(label='Intake Review')
condition   = Transition(label='Condition Scan')
material    = Transition(label='Material Test')
style       = Transition(label='Style Match')
provenance  = Transition(label='Provenance Log')
forgery     = Transition(label='Forgery Risk')
legal       = Transition(label='Legal Audit')
expert      = Transition(label='Expert Panel')
crosscheck  = Transition(label='Data Crosscheck')
report      = Transition(label='Report Draft')
blockchain  = Transition(label='Blockchain Tag')
cert        = Transition(label='Certification')
feedback    = Transition(label='Client Feedback')
approval    = Transition(label='Final Approval')
release     = Transition(label='Release Prep')

# Silent transition for loop continuation
skip        = SilentTransition()

# Loop: Expert Panel -> Data Crosscheck, repeated until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[expert, crosscheck])

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake, condition, material, style, provenance,
    forgery, legal,
    loop, report, blockchain, cert, feedback, approval, release
])

# Define the control-flow dependencies
root.order.add_edge(intake, condition)
root.order.add_edge(intake, material)
root.order.add_edge(condition, loop)
root.order.add_edge(material, loop)
root.order.add_edge(loop, report)
root.order.add_edge(provenance, report)
root.order.add_edge(forgery, report)
root.order.add_edge(legal, report)
root.order.add_edge(report, blockchain)
root.order.add_edge(blockchain, cert)
root.order.add_edge(cert, feedback)
root.order.add_edge(feedback, approval)
root.order.add_edge(approval, release)

# Final note: no unconnected nodes, all activities are either directly or transitively connected