import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Define the loop for the response deployment and monitoring
loop_response = OperatorPOWL(operator=Operator.LOOP, children=[response_deploy, situation_monitor])

# Define the XOR for the stakeholder notification and media briefing
xor_stakeholder = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_notify, media_brief])

# Define the XOR for the legal review and external consultation
xor_legal = OperatorPOWL(operator=Operator.XOR, children=[legal_review, external_consult])

# Define the loop for the data collection and risk mitigation
loop_data = OperatorPOWL(operator=Operator.LOOP, children=[data_collect, risk_mitigate])

# Define the loop for the recovery plan and post-review
loop_recovery = OperatorPOWL(operator=Operator.LOOP, children=[recovery_plan, post_review])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[
    alert_verify,
    impact_assess,
    team_assemble,
    resource_allocate,
    loop_response,
    xor_stakeholder,
    xor_legal,
    loop_data,
    loop_recovery
])

# Define the dependencies between the nodes
root.order.add_edge(alert_verify, impact_assess)
root.order.add_edge(impact_assess, team_assemble)
root.order.add_edge(team_assemble, resource_allocate)
root.order.add_edge(resource_allocate, loop_response)
root.order.add_edge(loop_response, xor_stakeholder)
root.order.add_edge(xor_stakeholder, xor_legal)
root.order.add_edge(xor_legal, loop_data)
root.order.add_edge(loop_data, loop_recovery)
root.order.add_edge(loop_recovery, alert_verify)

print(root)