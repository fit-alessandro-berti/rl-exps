import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake       = Transition(label='Artifact Intake')
cond_check   = Transition(label='Condition Check')
mat_sampling = Transition(label='Material Sampling')
radiocarbon  = Transition(label='Radiocarbon Test')
provenance   = Transition(label='Provenance Review')
imaging      = Transition(label='Imaging Capture')
chemical     = Transition(label='Chemical Analysis')
historical   = Transition(label='Historical Match')
expert       = Transition(label='Expert Consult')
forgery      = Transition(label='Forgery Scan')
market       = Transition(label='Market Survey')
value        = Transition(label='Value Estimate')
certification= Transition(label='Certification')
archive      = Transition(label='Digital Archive')
storage      = Transition(label='Final Storage')

# Define the core verification branch: sampling -> tests -> cross-referencing -> expert
verification_branch = StrictPartialOrder(nodes=[
    mat_sampling, radiocarbon, provenance, historical, expert
])
verification_branch.order.add_edge(mat_sampling, radiocarbon)
verification_branch.order.add_edge(mat_sampling, provenance)
verification_branch.order.add_edge(radiocarbon, historical)
verification_branch.order.add_edge(provenance, historical)
verification_branch.order.add_edge(historical, expert)

# Define the loop for repeated forgery scans
skip = SilentTransition()
forgery_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[forgery, skip]
)

# Define the final value estimation and certification branch
value_branch = StrictPartialOrder(nodes=[
    value, certification
])
value_branch.order.add_edge(value, certification)

# Assemble the overall process as a choice between the verification branch and forgery loop,
# then followed by value estimation and final storage
root = StrictPartialOrder(nodes=[
    intake, cond_check, verification_branch, forgery_loop,
    value_branch, archive, storage
])
root.order.add_edge(intake, cond_check)
root.order.add_edge(cond_check, verification_branch)
root.order.add_edge(cond_check, forgery_loop)
root.order.add_edge(verification_branch, value_branch)
root.order.add_edge(forgery_loop, value_branch)
root.order.add_edge(value_branch, archive)
root.order.add_edge(archive, storage)