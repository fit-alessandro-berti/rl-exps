import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

audit = Transition(label='Audit Artifacts')
interview = Transition(label='Interview Staff')
assess = Transition(label='Assess Risks')
plan = Transition(label='Plan Retrieval')
legal = Transition(label='Legal Review')
security = Transition(label='Security Check')
recover = Transition(label='Execute Recovery')
validate = Transition(label='Validate Items')
restore = Transition(label='Restore Function')
update = Transition(label='Update Systems')
train = Transition(label='Train Users')
document = Transition(label='Document Findings')
archive = Transition(label='Archive Records')
lessons = Transition(label='Review Lessons')
close = Transition(label='Close Process')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    audit,
    interview,
    assess,
    plan,
    legal,
    security,
    recover,
    validate,
    restore,
    update,
    train,
    document,
    archive,
    lessons,
    close
])

# Define the dependencies
root.order.add_edge(audit, assess)
root.order.add_edge(interview, assess)
root.order.add_edge(assess, plan)
root.order.add_edge(plan, legal)
root.order.add_edge(plan, security)
root.order.add_edge(legal, recover)
root.order.add_edge(legal, validate)
root.order.add_edge(security, recover)
root.order.add_edge(security, validate)
root.order.add_edge(recover, restore)
root.order.add_edge(recover, update)
root.order.add_edge(recover, train)
root.order.add_edge(restore, validate)
root.order.add_edge(restore, update)
root.order.add_edge(restore, train)
root.order.add_edge(validate, update)
root.order.add_edge(validate, train)
root.order.add_edge(update, document)
root.order.add_edge(update, archive)
root.order.add_edge(train, document)
root.order.add_edge(train, archive)
root.order.add_edge(document, lessons)
root.order.add_edge(archive, lessons)
root.order.add_edge(lessons, close)

print(root)