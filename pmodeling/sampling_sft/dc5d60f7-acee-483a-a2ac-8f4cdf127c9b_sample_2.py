import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
intake     = Transition(label='Intake Review')
condition  = Transition(label='Condition Scan')
material   = Transition(label='Material Test')
style      = Transition(label='Style Match')
provenance = Transition(label='Provenance Log')
forgery    = Transition(label='Forgery Risk')
legal      = Transition(label='Legal Audit')
expert     = Transition(label='Expert Panel')
crosscheck = Transition(label='Data Crosscheck')
report     = Transition(label='Report Draft')
blockchain = Transition(label='Blockchain Tag')
certify    = Transition(label='Certification')
feedback   = Transition(label='Client Feedback')
approval   = Transition(label='Final Approval')
release    = Transition(label='Release Prep')

# Build the loop for iterative feedback and expert panel review
# A = crosscheck -> report -> blockchain -> certify
A = StrictPartialOrder(nodes=[crosscheck, report, blockchain, certify])
A.order.add_edge(crosscheck, report)
A.order.add_edge(report, blockchain)
A.order.add_edge(blockchain, certify)

# B = feedback -> approval
B = StrictPartialOrder(nodes=[feedback, approval])
B.order.add_edge(feedback, approval)

# LOOP(children=[A, B]) means: do A, then either exit or do B then repeat A
loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Assemble the full workflow as a strict partial order
root = StrictPartialOrder(nodes=[
    intake, condition, material, style,
    provenance, forgery, legal,
    expert, loop, release
])

# Define the control-flow edges
root.order.add_edge(intake, condition)
root.order.add_edge(condition, material)
root.order.add_edge(material, style)
root.order.add_edge(style, provenance)
root.order.add_edge(provenance, forgery)
root.order.add_edge(provenance, legal)
root.order.add_edge(forgery, expert)
root.order.add_edge(legal, expert)
root.order.add_edge(expert, loop)
root.order.add_edge(loop, release)