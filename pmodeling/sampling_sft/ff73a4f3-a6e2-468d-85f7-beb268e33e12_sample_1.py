import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
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
archive = Transition(label='Archive Records')
document = Transition(label='Document Findings')
lessons = Transition(label='Review Lessons')
close = Transition(label='Close Process')

# Define the loop body: validate -> restore -> update -> train -> archive -> document -> lessons
body = StrictPartialOrder(nodes=[validate, restore, update, train, archive, document, lessons])
body.order.add_edge(validate, restore)
body.order.add_edge(restore, update)
body.order.add_edge(update, train)
body.order.add_edge(train, archive)
body.order.add_edge(archive, document)
body.order.add_edge(document, lessons)

# LOOP: execute the body, then optionally repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[execute, body])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[audit, interview, assess, plan, legal, security, loop, close])
root.order.add_edge(audit, assess)
root.order.add_edge(interview, assess)
root.order.add_edge(assess, plan)
root.order.add_edge(plan, legal)
root.order.add_edge(legal, security)
root.order.add_edge(security, loop)
root.order.add_edge(loop, close)