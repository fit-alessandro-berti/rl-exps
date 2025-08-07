import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
intake       = Transition(label='Artifact Intake')
provenance   = Transition(label='Provenance Check')
sampling     = Transition(label='Material Sampling')
test         = Transition(label='Scientific Test')
expert       = Transition(label='Expert Review')
archive      = Transition(label='Archive Search')
verify       = Transition(label='Legal Verify')
ownership    = Transition(label='Ownership Confirm')
audit        = Transition(label='Compliance Audit')
doc          = Transition(label='Data Documentation')
interim      = Transition(label='Interim Report')
dept_review  = Transition(label='Department Review')
consensus    = Transition(label='Consensus Meeting')
approval     = Transition(label='Final Approval')
release      = Transition(label='Artifact Release')

# Loop for iterative review and consensus
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[interim, dept_review]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake,
    provenance,
    sampling,
    test,
    expert,
    archive,
    verify,
    ownership,
    audit,
    doc,
    loop,
    consensus,
    approval,
    release
])

# Initial dependencies
root.order.add_edge(intake, provenance)
root.order.add_edge(provenance, sampling)
root.order.add_edge(sampling, test)
root.order.add_edge(test, expert)
root.order.add_edge(expert, archive)
root.order.add_edge(archive, verify)
root.order.add_edge(verify, ownership)
root.order.add_edge(ownership, audit)
root.order.add_edge(audit, doc)

# After each test, proceed to the loop
root.order.add_edge(sampling, loop)
root.order.add_edge(test, loop)
root.order.add_edge(expert, loop)
root.order.add_edge(archive, loop)
root.order.add_edge(verify, loop)
root.order.add_edge(ownership, loop)
root.order.add_edge(audit, loop)
root.order.add_edge(doc, loop)

# Loop then either exit or go back to the test sequence
root.order.add_edge(loop, loop)
root.order.add_edge(loop, consensus)

# After consensus, either approve or reject
root.order.add_edge(consensus, approval)
root.order.add_edge(consensus, release)

# Finally, approval or release leads to artifact release
root.order.add_edge(approval, release)
root.order.add_edge(release, release)