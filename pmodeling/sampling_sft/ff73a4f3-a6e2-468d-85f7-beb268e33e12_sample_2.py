import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
audit = Transition(label='Audit Artifacts')
interview = Transition(label='Interview Staff')
risk = Transition(label='Assess Risks')
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

# Define the loop body: Validate -> Restore -> Update -> Train -> Document
loop_body = StrictPartialOrder(nodes=[validate, restore, update, train, document])
loop_body.order.add_edge(validate, restore)
loop_body.order.add_edge(restore, update)
loop_body.order.add_edge(update, train)
loop_body.order.add_edge(train, document)

# Loop: do Plan Retrieval, then either exit or execute the loop_body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[plan, loop_body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    audit, interview, risk,
    loop,
    legal, security,
    recovery,
    archive, review, close
])

# Add control-flow edges
root.order.add_edge(audit, risk)
root.order.add_edge(interview, risk)
root.order.add_edge(risk, loop)
root.order.add_edge(loop, legal)
root.order.add_edge(loop, security)
root.order.add_edge(legal, recovery)
root.order.add_edge(security, recovery)
root.order.add_edge(recovery, archive)
root.order.add_edge(archive, review)
root.order.add_edge(review, close)