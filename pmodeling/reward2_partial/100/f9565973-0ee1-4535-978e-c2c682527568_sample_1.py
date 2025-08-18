from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
intake = Transition(label='Artifact Intake')
survey = Transition(label='Initial Survey')
test = Transition(label='Material Test')
registry = Transition(label='Registry Search')
owner_interview = Transition(label='Owner Interview')
condition = Transition(label='Condition Report')
forgery = Transition(label='Forgery Scan')
tagging = Transition(label='Digital Tagging')
ledger = Transition(label='Ledger Entry')
expert = Transition(label='Expert Review')
legal = Transition(label='Legal Verify')
draft = Transition(label='Provenance Draft')
approval = Transition(label='Client Approval')
certificate = Transition(label='Final Certificate')
storage = Transition(label='Archive Storage')

# Define the partial order
root = StrictPartialOrder(nodes=[intake, survey, test, registry, owner_interview, condition, forgery, tagging, ledger, expert, legal, draft, approval, certificate, storage])

# Define the order dependencies
root.order.add_edge(intake, survey)
root.order.add_edge(survey, test)
root.order.add_edge(test, registry)
root.order.add_edge(registry, owner_interview)
root.order.add_edge(owner_interview, condition)
root.order.add_edge(condition, forgery)
root.order.add_edge(forgery, tagging)
root.order.add_edge(tagging, ledger)
root.order.add_edge(ledger, expert)
root.order.add_edge(expert, legal)
root.order.add_edge(legal, draft)
root.order.add_edge(draft, approval)
root.order.add_edge(approval, certificate)
root.order.add_edge(certificate, storage)

print(root)