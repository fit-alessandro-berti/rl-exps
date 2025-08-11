import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

audit = Transition(label='Audit Artifacts')
interview = Transition(label='Interview Staff')
assess = Transition(label='Assess Risks')
retrieval = Transition(label='Plan Retrieval')
legal = Transition(label='Legal Review')
security = Transition(label='Security Check')
execute = Transition(label='Execute Recovery')
validate = Transition(label='Validate Items')
restore = Transition(label='Restore Function')
update = Transition(label='Update Systems')
train = Transition(label='Train Users')
document = Transition(label='Document Findings')
archive = Transition(label='Archive Records')
lessons = Transition(label='Review Lessons')
close = Transition(label='Close Process')

# Silent transitions
skip_audit = SilentTransition()
skip_interview = SilentTransition()
skip_assess = SilentTransition()
skip_retrieval = SilentTransition()
skip_legal = SilentTransition()
skip_security = SilentTransition()
skip_execute = SilentTransition()
skip_validate = SilentTransition()
skip_restore = SilentTransition()
skip_update = SilentTransition()
skip_train = SilentTransition()
skip_document = SilentTransition()
skip_archive = SilentTransition()
skip_lessons = SilentTransition()

# Workflow model
audit_workflow = OperatorPOWL(operator=Operator.XOR, children=[audit, skip_audit])
interview_workflow = OperatorPOWL(operator=Operator.XOR, children=[interview, skip_interview])
assess_workflow = OperatorPOWL(operator=Operator.XOR, children=[assess, skip_assess])
retrieval_workflow = OperatorPOWL(operator=Operator.XOR, children=[retrieval, skip_retrieval])
legal_workflow = OperatorPOWL(operator=Operator.XOR, children=[legal, skip_legal])
security_workflow = OperatorPOWL(operator=Operator.XOR, children=[security, skip_security])
execute_workflow = OperatorPOWL(operator=Operator.XOR, children=[execute, skip_execute])
validate_workflow = OperatorPOWL(operator=Operator.XOR, children=[validate, skip_validate])
restore_workflow = OperatorPOWL(operator=Operator.XOR, children=[restore, skip_restore])
update_workflow = OperatorPOWL(operator=Operator.XOR, children=[update, skip_update])
train_workflow = OperatorPOWL(operator=Operator.XOR, children=[train, skip_train])
document_workflow = OperatorPOWL(operator=Operator.XOR, children=[document, skip_document])
archive_workflow = OperatorPOWL(operator=Operator.XOR, children=[archive, skip_archive])
lessons_workflow = OperatorPOWL(operator=Operator.XOR, children=[lessons, skip_lessons])

root = StrictPartialOrder(nodes=[
    audit_workflow, interview_workflow, assess_workflow, retrieval_workflow, legal_workflow, security_workflow,
    execute_workflow, validate_workflow, restore_workflow, update_workflow, train_workflow, document_workflow,
    archive_workflow, lessons_workflow, close
])

root.order.add_edge(audit_workflow, interview_workflow)
root.order.add_edge(interview_workflow, assess_workflow)
root.order.add_edge(assess_workflow, retrieval_workflow)
root.order.add_edge(retrieval_workflow, legal_workflow)
root.order.add_edge(legal_workflow, security_workflow)
root.order.add_edge(security_workflow, execute_workflow)
root.order.add_edge(execute_workflow, validate_workflow)
root.order.add_edge(validate_workflow, restore_workflow)
root.order.add_edge(restore_workflow, update_workflow)
root.order.add_edge(update_workflow, train_workflow)
root.order.add_edge(train_workflow, document_workflow)
root.order.add_edge(document_workflow, archive_workflow)
root.order.add_edge(archive_workflow, lessons_workflow)
root.order.add_edge(lessons_workflow, close)

print(root)