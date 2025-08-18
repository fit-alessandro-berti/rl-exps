import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[team_assemble, impact_assess])
loop = OperatorPOWL(operator=Operator.LOOP, children=[resource_allocate, stakeholder_notify, legal_review, media_brief, response_deploy, situation_monitor, data_collect, risk_mitigate, recovery_plan, external_consult, status_update])
root = StrictPartialOrder(nodes=[alert_verify, xor, loop])
root.order.add_edge(alert_verify, xor)
root.order.add_edge(xor, loop)

# Print the POWL model
print(root)