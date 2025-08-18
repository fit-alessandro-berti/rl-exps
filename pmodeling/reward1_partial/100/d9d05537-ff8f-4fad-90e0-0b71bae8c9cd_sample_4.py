from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, media_brief])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[response_deploy, situation_monitor])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[data_collect, risk_mitigate])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[recovery_plan, external_consult])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[status_update, post_review])

# Create root node
root = StrictPartialOrder(nodes=[alert_verify, impact_assess, team_assemble, resource_allocate, stakeholder_notify, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(alert_verify, impact_assess)
root.order.add_edge(impact_assess, team_assemble)
root.order.add_edge(team_assemble, resource_allocate)
root.order.add_edge(resource_allocate, stakeholder_notify)
root.order.add_edge(stakeholder_notify, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, post_review)