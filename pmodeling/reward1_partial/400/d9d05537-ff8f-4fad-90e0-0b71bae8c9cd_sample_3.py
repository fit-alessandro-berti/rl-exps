import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for alert verification
alert_loop = OperatorPOWL(operator=Operator.LOOP, children=[alert_verify])

# Define the choices for impact assessment
impact_choice = OperatorPOWL(operator=Operator.XOR, children=[impact_assess, resource_allocate])

# Define the loop for team assembling
team_loop = OperatorPOWL(operator=Operator.LOOP, children=[team_assemble])

# Define the loop for stakeholder notification
stakeholder_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_notify])

# Define the loop for legal review
legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_review])

# Define the loop for media brief
media_loop = OperatorPOWL(operator=Operator.LOOP, children=[media_brief])

# Define the loop for response deployment
response_loop = OperatorPOWL(operator=Operator.LOOP, children=[response_deploy])

# Define the loop for situation monitoring
situation_loop = OperatorPOWL(operator=Operator.LOOP, children=[situation_monitor])

# Define the loop for data collection
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_collect])

# Define the loop for risk mitigation
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_mitigate])

# Define the loop for recovery plan
recovery_loop = OperatorPOWL(operator=Operator.LOOP, children=[recovery_plan])

# Define the loop for external consultation
external_loop = OperatorPOWL(operator=Operator.LOOP, children=[external_consult])

# Define the loop for status update
status_loop = OperatorPOWL(operator=Operator.LOOP, children=[status_update])

# Define the loop for post review
post_loop = OperatorPOWL(operator=Operator.LOOP, children=[post_review])

# Define the root partial order
root = StrictPartialOrder(nodes=[
    alert_loop, impact_choice, team_loop, stakeholder_loop, legal_loop,
    media_loop, response_loop, situation_loop, data_loop, risk_loop,
    recovery_loop, external_loop, status_loop, post_loop
])

# Add dependencies between the loops
root.order.add_edge(alert_loop, impact_choice)
root.order.add_edge(impact_choice, team_loop)
root.order.add_edge(team_loop, stakeholder_loop)
root.order.add_edge(stakeholder_loop, legal_loop)
root.order.add_edge(legal_loop, media_loop)
root.order.add_edge(media_loop, response_loop)
root.order.add_edge(response_loop, situation_loop)
root.order.add_edge(situation_loop, data_loop)
root.order.add_edge(data_loop, risk_loop)
root.order.add_edge(risk_loop, recovery_loop)
root.order.add_edge(recovery_loop, external_loop)
root.order.add_edge(external_loop, status_loop)
root.order.add_edge(status_loop, post_loop)

print(root)