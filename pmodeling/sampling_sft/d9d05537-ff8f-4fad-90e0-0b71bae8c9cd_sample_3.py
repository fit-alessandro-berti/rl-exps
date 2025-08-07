import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
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

# Define the iterative recovery loop: collect data, mitigate risks, then optionally consult and update status
recovery_body = StrictPartialOrder(nodes=[data_collect, risk_mitigate, external_consult, status_update])
recovery_body.order.add_edge(data_collect, risk_mitigate)
recovery_body.order.add_edge(risk_mitigate, external_consult)
recovery_body.order.add_edge(external_consult, status_update)

loop_recovery = OperatorPOWL(operator=Operator.LOOP, children=[recovery_body, recovery_plan])

# Assemble the overall partial order
root = StrictPartialOrder(nodes=[
    alert_verify,
    impact_assess,
    team_assemble,
    resource_alloc,
    stakeholder_not,
    legal_review,
    media_brief,
    response_deploy,
    situation_mon,
    loop_recovery
])

# Define the control-flow edges
root.order.add_edge(alert_verify, impact_assess)
root.order.add_edge(impact_assess, team_assemble)
root.order.add_edge(team_assemble, resource_alloc)
root.order.add_edge(resource_alloc, stakeholder_not)
root.order.add_edge(stakeholder_not, legal_review)
root.order.add_edge(legal_review, media_brief)
root.order.add_edge(media_brief, response_deploy)
root.order.add_edge(response_deploy, situation_mon)
root.order.add_edge(situation_mon, loop_recovery)