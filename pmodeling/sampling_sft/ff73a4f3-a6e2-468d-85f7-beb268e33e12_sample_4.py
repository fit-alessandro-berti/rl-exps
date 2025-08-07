import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the loop body: Update Systems -> Train Users -> Document Findings
body = StrictPartialOrder(nodes=[update, train, document])
body.order.add_edge(update, train)
body.order.add_edge(train, document)

# Define the loop: Review Lessons -> Close Process
loop = OperatorPOWL(operator=Operator.LOOP, children=[review, close])

# Assemble the top-level partial order
root = StrictPartialOrder(nodes=[
    audit, interview, assess, plan,
    legal, security,
    recover, validate, restore,
    body,
    loop
])

# Control-flow edges
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
root.order.add_edge(recover, validate)
root.order.add_edge(validate, restore)
root.order.add_edge(validate, body)
root.order.add_edge(body, loop)