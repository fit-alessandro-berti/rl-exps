import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
audit = Transition(label='Audit Artifacts')
interview = Transition(label='Interview Staff')
assess = Transition(label='Assess Risks')
plan = Transition(label='Plan Retrieval')
legal = Transition(label='Legal Review')
security = Transition(label='Security Check')
recovery = Transition(label='Execute Recovery')
validate = Transition(label='Validate Items')
restore = Transition(label='Restore Function')
update = Transition(label='Update Systems')
train = Transition(label='Train Users')
document = Transition(label='Document Findings')
archive = Transition(label='Archive Records')
review = Transition(label='Review Lessons')
close = Transition(label='Close Process')

# Create the POWL model
root = StrictPartialOrder(nodes=[
    audit, interview, assess, plan, legal, security, recovery, validate, restore, update, train, document, archive, review, close
])

# Define the dependencies
root.order.add_edge(audit, interview)
root.order.add_edge(interview, assess)
root.order.add_edge(assess, plan)
root.order.add_edge(plan, legal)
root.order.add_edge(legal, security)
root.order.add_edge(security, recovery)
root.order.add_edge(recovery, validate)
root.order.add_edge(validate, restore)
root.order.add_edge(restore, update)
root.order.add_edge(update, train)
root.order.add_edge(train, document)
root.order.add_edge(document, archive)
root.order.add_edge(archive, review)
root.order.add_edge(review, close)

print(root)