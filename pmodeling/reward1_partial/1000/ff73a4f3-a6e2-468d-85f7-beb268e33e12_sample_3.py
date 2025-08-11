import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define activities
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

# Define control flow
audit_artifacts.next = interview_staff
interview_staff.next = assess_risks
assess_risks.next = plan_retrieval
plan_retrieval.next = legal_review
legal_review.next = security_check
security_check.next = execute_recovery
execute_recovery.next = validate_items
validate_items.next = restore_function
restore_function.next = update_systems
update_systems.next = train_users
train_users.next = document_findings
document_findings.next = archive_records
archive_records.next = review_lessons
review_lessons.next = close_process

root = StrictPartialOrder(nodes=[audit_artifacts, interview_staff, assess_risks, plan_retrieval, legal_review, security_check, execute_recovery, validate_items, restore_function, update_systems, train_users, document_findings, archive_records, review_lessons, close_process])