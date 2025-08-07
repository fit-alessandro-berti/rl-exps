import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
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
review = Transition(label='Review Lessons')
close = Transition(label='Close Process')

# Define the loop for reintegration: Train Users then either exit or Archive Records and Review Lessons and Train Users again
reintegration_loop = OperatorPOWL(operator=Operator.LOOP, children=[train, archive])

# Build the partial order
root = StrictPartialOrder(nodes=[
    audit, interview, assess, plan, legal, security, recover,
    validate, restore, update, reintegration_loop, document, review, close
])

# Define the control-flow dependencies
root.order.add_edge(audit, assess)
root.order.add_edge(interview, assess)
root.order.add_edge(assess, plan)
root.order.add_edge(plan, legal)
root.order.add_edge(plan, security)
root.order.add_edge(legal, recover)
root.order.add_edge(security, recover)
root.order.add_edge(recover, validate)
root.order.add_edge(validate, restore)
root.order.add_edge(restore, update)
root.order.add_edge(update, reintegration_loop)
root.order.add_edge(reintegration_loop, document)
root.order.add_edge(document, review)
root.order.add_edge(review, close)