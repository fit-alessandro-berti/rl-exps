import pm4py
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

# Define silent transitions
skip = SilentTransition()

# Define choice of activities
impact_assess_xor = OperatorPOWL(operator=Operator.XOR, children=[impact_assess, skip])
team_assemble_xor = OperatorPOWL(operator=Operator.XOR, children=[team_assemble, skip])
resource_allocate_xor = OperatorPOWL(operator=Operator.XOR, children=[resource_allocate, skip])
stakeholder_notify_xor = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_notify, skip])
legal_review_xor = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
media_brief_xor = OperatorPOWL(operator=Operator.XOR, children=[media_brief, skip])
response_deploy_xor = OperatorPOWL(operator=Operator.XOR, children=[response_deploy, skip])
situation_monitor_xor = OperatorPOWL(operator=Operator.XOR, children=[situation_monitor, skip])
data_collect_xor = OperatorPOWL(operator=Operator.XOR, children=[data_collect, skip])
risk_mitigate_xor = OperatorPOWL(operator=Operator.XOR, children=[risk_mitigate, skip])
recovery_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[recovery_plan, skip])
external_consult_xor = OperatorPOWL(operator=Operator.XOR, children=[external_consult, skip])
status_update_xor = OperatorPOWL(operator=Operator.XOR, children=[status_update, skip])
post_review_xor = OperatorPOWL(operator=Operator.XOR, children=[post_review, skip])

# Define loop activities
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[impact_assess_xor, team_assemble_xor])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[resource_allocate_xor, stakeholder_notify_xor])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[legal_review_xor, media_brief_xor])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[response_deploy_xor, situation_monitor_xor])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[data_collect_xor, risk_mitigate_xor])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[recovery_plan_xor, external_consult_xor])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[status_update_xor, post_review_xor])

# Define root of the POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7])
root.order.add_edge(loop1, impact_assess_xor)
root.order.add_edge(loop1, team_assemble_xor)
root.order.add_edge(loop2, resource_allocate_xor)
root.order.add_edge(loop2, stakeholder_notify_xor)
root.order.add_edge(loop3, legal_review_xor)
root.order.add_edge(loop3, media_brief_xor)
root.order.add_edge(loop4, response_deploy_xor)
root.order.add_edge(loop4, situation_monitor_xor)
root.order.add_edge(loop5, data_collect_xor)
root.order.add_edge(loop5, risk_mitigate_xor)
root.order.add_edge(loop6, recovery_plan_xor)
root.order.add_edge(loop6, external_consult_xor)
root.order.add_edge(loop7, status_update_xor)
root.order.add_edge(loop7, post_review_xor)