import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
alert_verify = Transition(label='Alert Verify')
impact_assess = Transition(label='Impact Assess')
team_assemble = Transition(label='Team Assemble')
resource_allocate = Transition(label='Resource Allocate')
stakeholder_notify = Transition(label='Stakeholder Notify')
legal_review = Transition(label='Legal Review')
media_brief = Transition(label='Media Brief')
response_deploy = Transition(label='Response Deploy')
situation_monitor = Transition(label='Situation Monitor')
data_collect = Transition(label='Data Collect')
risk_mitigate = Transition(label='Risk Mitigate')
recovery_plan = Transition(label='Recovery Plan')
external_consult = Transition(label='External Consult')
status_update = Transition(label='Status Update')
post_review = Transition(label='Post Review')

# Define silent transitions
skip = SilentTransition()

# Define loop for the initial steps
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[alert_verify, impact_assess, team_assemble])

# Define exclusive choice for resource allocation
xor_resource = OperatorPOWL(operator=Operator.XOR, children=[resource_allocate, skip])

# Define loop for the response steps
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[response_deploy, media_brief, data_collect, risk_mitigate])

# Define exclusive choice for external consultation
xor_external = OperatorPOWL(operator=Operator.XOR, children=[external_consult, skip])

# Define loop for the monitoring steps
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[situation_monitor, status_update, post_review])

# Define exclusive choice for legal review
xor_legal = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])

# Define exclusive choice for stakeholder notification
xor_stakeholder = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_notify, skip])

# Define exclusive choice for recovery plan
xor_recovery = OperatorPOWL(operator=Operator.XOR, children=[recovery_plan, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, xor_resource, loop2, xor_external, loop3, xor_legal, xor_stakeholder, xor_recovery])

# Define the partial order edges
root.order.add_edge(loop1, xor_resource)
root.order.add_edge(xor_resource, loop2)
root.order.add_edge(loop2, xor_external)
root.order.add_edge(xor_external, loop3)
root.order.add_edge(loop3, xor_legal)
root.order.add_edge(xor_legal, xor_stakeholder)
root.order.add_edge(xor_stakeholder, xor_recovery)
root.order.add_edge(xor_recovery, loop1)

# Print the root POWL model
print(root)