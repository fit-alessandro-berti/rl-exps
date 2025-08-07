import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Build the partial order
root = StrictPartialOrder(nodes=[
    alert_verify,
    impact_assess,
    team_assemble,
    resource_allocate,
    stakeholder_notify,
    legal_review,
    media_brief,
    response_deploy,
    situation_monitor,
    data_collect,
    risk_mitigate,
    recovery_plan,
    external_consult,
    status_update,
    post_review
])

# Alert Verify -> Impact Assess
root.order.add_edge(alert_verify, impact_assess)

# Impact Assess -> Team Assemble
root.order.add_edge(impact_assess, team_assemble)

# Team Assemble -> Resource Allocate
root.order.add_edge(team_assemble, resource_allocate)

# Resource Allocate -> Stakeholder Notify
root.order.add_edge(resource_allocate, stakeholder_notify)

# Stakeholder Notify -> Legal Review
root.order.add_edge(stakeholder_notify, legal_review)

# Legal Review -> Media Brief
root.order.add_edge(legal_review, media_brief)

# Media Brief -> Response Deploy
root.order.add_edge(media_brief, response_deploy)

# Response Deploy -> Situation Monitor
root.order.add_edge(response_deploy, situation_monitor)

# Situation Monitor -> Data Collect
root.order.add_edge(situation_monitor, data_collect)

# Data Collect -> Risk Mitigate
root.order.add_edge(data_collect, risk_mitigate)

# Risk Mitigate -> Recovery Plan
root.order.add_edge(risk_mitigate, recovery_plan)

# Recovery Plan -> External Consult
root.order.add_edge(recovery_plan, external_consult)

# External Consult -> Status Update
root.order.add_edge(external_consult, status_update)

# Status Update -> Post Review
root.order.add_edge(status_update, post_review)

# Post Review -> Impact Assess (loop)
loop = OperatorPOWL(operator=Operator.LOOP, children=[impact_assess, post_review])
root.order.add_edge(post_review, loop)