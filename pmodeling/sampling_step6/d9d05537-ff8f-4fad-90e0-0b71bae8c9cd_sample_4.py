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

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    alert_verify, impact_assess, team_assemble, resource_allocate,
    stakeholder_notify, legal_review, media_brief, response_deploy,
    situation_monitor, data_collect, risk_mitigate, recovery_plan,
    external_consult, status_update, post_review
])

# Define dependencies between activities (if any, as per the process description)
# For simplicity, let's assume no dependencies are defined in the given process description
# If dependencies were specified, they would be added here

print(root)