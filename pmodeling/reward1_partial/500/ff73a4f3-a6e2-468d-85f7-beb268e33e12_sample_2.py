import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
audit = Transition(label='Audit Artifacts')
interview = Transition(label='Interview Staff')
assess = Transition(label='Assess Risks')
plan = Transition(label='Plan Retrieval')
legal = Transition(label='Legal Review')
security = Transition(label='Security Check')
execute = Transition(label='Execute Recovery')
validate = Transition(label='Validate Items')
restore = Transition(label='Restore Function')
update = Transition(label='Update Systems')
train = Transition(label='Train Users')
document = Transition(label='Document Findings')
archive = Transition(label='Archive Records')
review = Transition(label='Review Lessons')
close = Transition(label='Close Process')

# Define the silent transitions for concurrent activities
skip_audit = SilentTransition()
skip_interview = SilentTransition()
skip_assess = SilentTransition()
skip_plan = SilentTransition()
skip_legal = SilentTransition()
skip_security = SilentTransition()
skip_execute = SilentTransition()
skip_validate = SilentTransition()
skip_restore = SilentTransition()
skip_update = SilentTransition()
skip_train = SilentTransition()
skip_document = SilentTransition()
skip_archive = SilentTransition()
skip_review = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(
    nodes=[audit, interview, assess, plan, legal, security, execute, validate, restore, update, train, document, archive, review, close],
    order={
        audit: [interview, assess, plan, legal, security, execute, validate, restore, update, train, document, archive, review, close],
        interview: [assess, plan, legal, security, execute, validate, restore, update, train, document, archive, review, close],
        assess: [plan, legal, security, execute, validate, restore, update, train, document, archive, review, close],
        plan: [legal, security, execute, validate, restore, update, train, document, archive, review, close],
        legal: [security, execute, validate, restore, update, train, document, archive, review, close],
        security: [execute, validate, restore, update, train, document, archive, review, close],
        execute: [validate, restore, update, train, document, archive, review, close],
        validate: [restore, update, train, document, archive, review, close],
        restore: [update, train, document, archive, review, close],
        update: [train, document, archive, review, close],
        train: [document, archive, review, close],
        document: [archive, review, close],
        archive: [review, close],
        review: [close]
    }
)

# Add dependencies between activities
root.order.add_edge(audit, interview)
root.order.add_edge(audit, assess)
root.order.add_edge(audit, plan)
root.order.add_edge(audit, legal)
root.order.add_edge(audit, security)
root.order.add_edge(audit, execute)
root.order.add_edge(audit, validate)
root.order.add_edge(audit, restore)
root.order.add_edge(audit, update)
root.order.add_edge(audit, train)
root.order.add_edge(audit, document)
root.order.add_edge(audit, archive)
root.order.add_edge(audit, review)
root.order.add_edge(audit, close)

root.order.add_edge(interview, assess)
root.order.add_edge(interview, plan)
root.order.add_edge(interview, legal)
root.order.add_edge(interview, security)
root.order.add_edge(interview, execute)
root.order.add_edge(interview, validate)
root.order.add_edge(interview, restore)
root.order.add_edge(interview, update)
root.order.add_edge(interview, train)
root.order.add_edge(interview, document)
root.order.add_edge(interview, archive)
root.order.add_edge(interview, review)
root.order.add_edge(interview, close)

root.order.add_edge(assess, plan)
root.order.add_edge(assess, legal)
root.order.add_edge(assess, security)
root.order.add_edge(assess, execute)
root.order.add_edge(assess, validate)
root.order.add_edge(assess, restore)
root.order.add_edge(assess, update)
root.order.add_edge(assess, train)
root.order.add_edge(assess, document)
root.order.add_edge(assess, archive)
root.order.add_edge(assess, review)
root.order.add_edge(assess, close)

root.order.add_edge(plan, legal)
root.order.add_edge(plan, security)
root.order.add_edge(plan, execute)
root.order.add_edge(plan, validate)
root.order.add_edge(plan, restore)
root.order.add_edge(plan, update)
root.order.add_edge(plan, train)
root.order.add_edge(plan, document)
root.order.add_edge(plan, archive)
root.order.add_edge(plan, review)
root.order.add_edge(plan, close)

root.order.add_edge(legal, security)
root.order.add_edge(legal, execute)
root.order.add_edge(legal, validate)
root.order.add_edge(legal, restore)
root.order.add_edge(legal, update)
root.order.add_edge(legal, train)
root.order.add_edge(legal, document)
root.order.add_edge(legal, archive)
root.order.add_edge(legal, review)
root.order.add_edge(legal, close)

root.order.add_edge(security, execute)
root.order.add_edge(security, validate)
root.order.add_edge(security, restore)
root.order.add_edge(security, update)
root.order.add_edge(security, train)
root.order.add_edge(security, document)
root.order.add_edge(security, archive)
root.order.add_edge(security, review)
root.order.add_edge(security, close)

root.order.add_edge(execute, validate)
root.order.add_edge(execute, restore)
root.order.add_edge(execute, update)
root.order.add_edge(execute, train)
root.order.add_edge(execute, document)
root.order.add_edge(execute, archive)
root.order.add_edge(execute, review)
root.order.add_edge(execute, close)

root.order.add_edge(validate, restore)
root.order.add_edge(validate, update)
root.order.add_edge(validate, train)
root.order.add_edge(validate, document)
root.order.add_edge(validate, archive)
root.order.add_edge(validate, review)
root.order.add_edge(validate, close)

root.order.add_edge(restore, update)
root.order.add_edge(restore, train)
root.order.add_edge(restore, document)
root.order.add_edge(restore, archive)
root.order.add_edge(restore, review)
root.order.add_edge(restore, close)

root.order.add_edge(update, train)
root.order.add_edge(update, document)
root.order.add_edge(update, archive)
root.order.add_edge(update, review)
root.order.add_edge(update, close)

root.order.add_edge(train, document)
root.order.add_edge(train, archive)
root.order.add_edge(train, review)
root.order.add_edge(train, close)

root.order.add_edge(document, archive)
root.order.add_edge(document, review)
root.order.add_edge(document, close)

root.order.add_edge(archive, review)
root.order.add_edge(archive, close)

root.order.add_edge(review, close)

# Print the POWL model
print(root)