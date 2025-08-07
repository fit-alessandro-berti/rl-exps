import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
t_intake      = Transition(label='Artifact Intake')
t_vscan       = Transition(label='Visual Scan')
t_mtest       = Transition(label='Material Test')
t_rccheck     = Transition(label='Radiocarbon Check')
t_prosearch   = Transition(label='Provenance Search')
t_archive     = Transition(label='Archive Review')
t_expconsult  = Transition(label='Expert Consult')
t_mexam       = Transition(label='Microscope Exam')
t_irscan      = Transition(label='Infrared Scan')
t_legal       = Transition(label='Legal Verify')
t_condition   = Transition(label='Condition Report')
t_dcatalog    = Transition(label='Digital Catalog')
t_ownership   = Transition(label='Ownership Audit')
t_restplan    = Transition(label='Restoration Plan')
t_final       = Transition(label='Final Approval')
t_authcert    = Transition(label='Authentication Cert')

# Loop for expert consultations: do Expert Consult, then optionally do Expert Consult again
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[t_expconsult, t_expconsult])

# Build the partial order
root = StrictPartialOrder(nodes=[
    t_intake,
    t_vscan,
    t_mtest,
    t_rccheck,
    t_prosearch,
    t_archive,
    expert_loop,
    t_mexam,
    t_irscan,
    t_legal,
    t_condition,
    t_dcatalog,
    t_ownership,
    t_restplan,
    t_final,
    t_authcert
])

# Define the control-flow dependencies
root.order.add_edge(t_intake, t_vscan)
root.order.add_edge(t_intake, t_mtest)
root.order.add_edge(t_intake, t_rccheck)
root.order.add_edge(t_intake, t_prosearch)

root.order.add_edge(t_vscan, expert_loop)
root.order.add_edge(t_mtest, expert_loop)
root.order.add_edge(t_rccheck, expert_loop)
root.order.add_edge(t_prosearch, expert_loop)

root.order.add_edge(expert_loop, t_mexam)
root.order.add_edge(expert_loop, t_irscan)

root.order.add_edge(t_mexam, t_legal)
root.order.add_edge(t_irscan, t_legal)

root.order.add_edge(t_legal, t_condition)
root.order.add_edge(t_condition, t_dcatalog)
root.order.add_edge(t_dcatalog, t_ownership)
root.order.add_edge(t_ownership, t_restplan)
root.order.add_edge(t_restplan, t_final)
root.order.add_edge(t_final, t_authcert)

print(root)