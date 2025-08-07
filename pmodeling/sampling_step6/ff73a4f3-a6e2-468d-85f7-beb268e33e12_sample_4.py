import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
audit_artifacts = Transition(label='Audit Artifacts')
interview_staff = Transition(label='Interview Staff')
assess_risks = Transition(label='Assess Risks')
plan_retrieval = Transition(label='Plan Retrieval')
legal_review = Transition(label='Legal Review')
security_check = Transition(label='Security Check')
execute_recovery = Transition(label='Execute Recovery')
validate_items = Transition(label='Validate Items')
restore_function = Transition(label='Restore Function')
update_systems = Transition(label='Update Systems')
train_users = Transition(label='Train Users')
document_findings = Transition(label='Document Findings')
archive_records = Transition(label='Archive Records')
review_lessons = Transition(label='Review Lessons')
close_process = Transition(label='Close Process')

# Define the partial order
root = StrictPartialOrder(nodes=[
    audit_artifacts,
    interview_staff,
    assess_risks,
    plan_retrieval,
    legal_review,
    security_check,
    execute_recovery,
    validate_items,
    restore_function,
    update_systems,
    train_users,
    document_findings,
    archive_records,
    review_lessons,
    close_process
])

# Add dependencies if any (e.g., audit artifacts must be completed before interviewing staff)
# In this simple example, no dependencies are explicitly defined.

print(root)