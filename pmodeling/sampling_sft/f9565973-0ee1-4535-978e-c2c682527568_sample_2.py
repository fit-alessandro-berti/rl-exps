import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
intake     = Transition(label='Artifact Intake')
survey     = Transition(label='Initial Survey')
test       = Transition(label='Material Test')
check      = Transition(label='Historical Check')
registry   = Transition(label='Registry Search')
owner      = Transition(label='Owner Interview')
condition  = Transition(label='Condition Report')
forgery    = Transition(label='Forgery Scan')
expert     = Transition(label='Expert Review')
legal      = Transition(label='Legal Verify')
tag        = Transition(label='Digital Tagging')
ledger     = Transition(label='Ledger Entry')
draft      = Transition(label='Provenance Draft')
approval   = Transition(label='Client Approval')
final      = Transition(label='Final Certificate')
archive    = Transition(label='Archive Storage')

# Silent transition for loop exit
skip = SilentTransition()

# Choice: either proceed with forgery scan or skip
xor = OperatorPOWL(operator=Operator.XOR, children=[forgery, skip])

# Loop: after condition report, either exit or do forgery scan then re-do condition report
loop = OperatorPOWL(operator=Operator.LOOP, children=[condition, xor])

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake,
    survey,
    test,
    check,
    registry,
    owner,
    loop,
    condition,
    expert,
    legal,
    tag,
    ledger,
    draft,
    approval,
    final,
    archive
])

# Define the control-flow order
root.order.add_edge(intake, survey)
root.order.add_edge(survey, test)
root.order.add_edge(test, check)
root.order.add_edge(check, registry)
root.order.add_edge(check, owner)
root.order.add_edge(registry, draft)
root.order.add_edge(owner, draft)
root.order.add_edge(draft, expert)
root.order.add_edge(draft, legal)
root.order.add_edge(expert, tag)
root.order.add_edge(legal, tag)
root.order.add_edge(tag, ledger)
root.order.add_edge(ledger, draft)
root.order.add_edge(draft, approval)
root.order.add_edge(approval, final)
root.order.add_edge(final, archive)