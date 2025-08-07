import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
intake     = Transition(label='Artifact Intake')
initial    = Transition(label='Initial Survey')
material   = Transition(label='Material Test')
historical = Transition(label='Historical Check')
registry   = Transition(label='Registry Search')
owner      = Transition(label='Owner Interview')
condition  = Transition(label='Condition Report')
forgery    = Transition(label='Forgery Scan')
digital    = Transition(label='Digital Tagging')
ledger     = Transition(label='Ledger Entry')
expert     = Transition(label='Expert Review')
legal      = Transition(label='Legal Verify')
provenance = Transition(label='Provenance Draft')
approval   = Transition(label='Client Approval')
final      = Transition(label='Final Certificate')
archive    = Transition(label='Archive Storage')

# Build the verification loop: do material test, then either exit or do historical check and repeat
verification_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[material, historical]
)

# Build the expert review with optional forgery scan
expert_with_forgery = OperatorPOWL(
    operator=Operator.XOR,
    children=[expert, forgery]
)

# Build the legal compliance branch: do expert review with forgery, then legal verify
legal_branch = StrictPartialOrder(nodes=[expert_with_forgery, legal])
legal_branch.order.add_edge(expert_with_forgery, legal)

# Assemble the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    intake, initial, verification_loop,
    condition, digital, ledger,
    provenance, approval, final, archive,
    legal_branch
])

# Define the control-flow dependencies
root.order.add_edge(intake, initial)
root.order.add_edge(initial, verification_loop)
root.order.add_edge(verification_loop, condition)
root.order.add_edge(condition, digital)
root.order.add_edge(digital, ledger)
root.order.add_edge(ledger, provenance)
root.order.add_edge(provenance, approval)
root.order.add_edge(provenance, final)
root.order.add_edge(approval, archive)
root.order.add_edge(final, archive)
root.order.add_edge(legal_branch, archive)