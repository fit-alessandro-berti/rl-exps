import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
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

# Define the process
xor1 = OperatorPOWL(operator=Operator.XOR, children=[impact_assess, team_assemble])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[resource_allocate, stakeholder_notify])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, media_brief])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[response_deploy, situation_monitor])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[data_collect, risk_mitigate])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[recovery_plan, external_consult])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[status_update, post_review])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])

# Define the root
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)
root.order.add_edge(loop, xor7)

print(root)