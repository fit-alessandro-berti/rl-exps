import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
root = StrictPartialOrder(nodes=[audit_artifacts, interview_staff, assess_risks, plan_retrieval, legal_review, security_check, execute_recovery, validate_items, restore_function, update_systems, train_users, document_findings, archive_records, review_lessons, close_process])

# Define the order of execution
root.order.add_edge(audit_artifacts, interview_staff)
root.order.add_edge(interview_staff, assess_risks)
root.order.add_edge(assess_risks, plan_retrieval)
root.order.add_edge(plan_retrieval, legal_review)
root.order.add_edge(legal_review, security_check)
root.order.add_edge(security_check, execute_recovery)
root.order.add_edge(execute_recovery, validate_items)
root.order.add_edge(validate_items, restore_function)
root.order.add_edge(restore_function, update_systems)
root.order.add_edge(update_systems, train_users)
root.order.add_edge(train_users, document_findings)
root.order.add_edge(document_findings, archive_records)
root.order.add_edge(archive_records, review_lessons)
root.order.add_edge(review_lessons, close_process)

# Print the result
print(root)