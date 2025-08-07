import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
intake       = Transition(label='Intake Review')
condition    = Transition(label='Condition Scan')
material     = Transition(label='Material Test')
style        = Transition(label='Style Match')
provenance   = Transition(label='Provenance Log')
forgery      = Transition(label='Forgery Risk')
legal        = Transition(label='Legal Audit')
expert       = Transition(label='Expert Panel')
crosscheck   = Transition(label='Data Crosscheck')
report       = Transition(label='Report Draft')
blockchain   = Transition(label='Blockchain Tag')
certification= Transition(label='Certification')
feedback     = Transition(label='Client Feedback')
final        = Transition(label='Final Approval')
release      = Transition(label='Release Prep')

# Build the iterative feedback loop for expert panel and data crosscheck
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[expert, crosscheck]
)

# Build the main partial order
root = StrictPartialOrder(nodes=[
    intake, condition, material, style, provenance,
    forgery, legal, feedback_loop, report, blockchain,
    certification, final, release
])

# Add sequential dependencies
root.order.add_edge(intake, condition)
root.order.add_edge(condition, material)
root.order.add_edge(material, style)
root.order.add_edge(style, provenance)
root.order.add_edge(provenance, forgery)
root.order.add_edge(forgery, legal)
root.order.add_edge(legal, feedback_loop)
root.order.add_edge(feedback_loop, report)
root.order.add_edge(report, blockchain)
root.order.add_edge(blockchain, certification)
root.order.add_edge(certification, final)
root.order.add_edge(final, release)