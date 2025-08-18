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

# Define the loop for data collection and risk mitigation
loop_data_risk = OperatorPOWL(operator=Operator.LOOP, children=[data_collect, risk_mitigate])

# Define the choice between response deploy and situation monitor
choice_response_deploy_situation_monitor = OperatorPOWL(operator=Operator.XOR, children=[response_deploy, situation_monitor])

# Define the partial order with all activities and dependencies
root = StrictPartialOrder(nodes=[
    alert_verify, impact_assess, team_assemble, resource_allocate, stakeholder_notify, legal_review, media_brief,
    choice_response_deploy_situation_monitor, loop_data_risk, external_consult, status_update, post_review
])

# Define the dependencies
root.order.add_edge(alert_verify, impact_assess)
root.order.add_edge(impact_assess, team_assemble)
root.order.add_edge(team_assemble, resource_allocate)
root.order.add_edge(resource_allocate, stakeholder_notify)
root.order.add_edge(stakeholder_notify, legal_review)
root.order.add_edge(legal_review, media_brief)
root.order.add_edge(media_brief, choice_response_deploy_situation_monitor)
root.order.add_edge(choice_response_deploy_situation_monitor, loop_data_risk)
root.order.add_edge(loop_data_risk, external_consult)
root.order.add_edge(external_consult, status_update)
root.order.add_edge(status_update, post_review)

print(root)