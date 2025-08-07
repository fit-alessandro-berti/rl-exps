import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
alert_verify    = Transition(label='Alert Verify')
impact_assess   = Transition(label='Impact Assess')
team_assemble   = Transition(label='Team Assemble')
resource_alloc  = Transition(label='Resource Allocate')
stakeholder_not = Transition(label='Stakeholder Notify')
legal_review    = Transition(label='Legal Review')
media_brief     = Transition(label='Media Brief')
response_deploy = Transition(label='Response Deploy')
situation_mon   = Transition(label='Situation Monitor')
data_collect    = Transition(label='Data Collect')
risk_mitigate   = Transition(label='Risk Mitigate')
recovery_plan   = Transition(label='Recovery Plan')
external_consult= Transition(label='External Consult')
status_update   = Transition(label='Status Update')
post_review     = Transition(label='Post Review')

# Define the monitoring loop: repeat Situation Monitor -> Data Collect -> Risk Mitigate
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[situation_mon, data_collect, risk_mitigate])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    alert_verify, impact_assess, team_assemble, resource_alloc,
    stakeholder_not, legal_review, media_brief, response_deploy,
    monitor_loop, recovery_plan, external_consult, status_update,
    post_review
])

# Add control-flow edges
root.order.add_edge(alert_verify, impact_assess)
root.order.add_edge(impact_assess, team_assemble)
root.order.add_edge(team_assemble, resource_alloc)
root.order.add_edge(resource_alloc, stakeholder_not)
root.order.add_edge(stakeholder_not, legal_review)
root.order.add_edge(legal_review, media_brief)
root.order.add_edge(media_brief, response_deploy)
root.order.add_edge(response_deploy, monitor_loop)
root.order.add_edge(monitor_loop, recovery_plan)
root.order.add_edge(recovery_plan, external_consult)
root.order.add_edge(external_consult, status_update)
root.order.add_edge(status_update, post_review)