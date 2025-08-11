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

# Define the silent transitions (empty labels)
skip = SilentTransition()

# Define the loops and choices for the process
# Loop for the recovery plan
loop_recovery_plan = OperatorPOWL(operator=Operator.LOOP, children=[recovery_plan])

# Choice for the initial steps
choice_initial_steps = OperatorPOWL(operator=Operator.XOR, children=[impact_assess, team_assemble])

# Choice for the resource allocation
choice_resource_allocation = OperatorPOWL(operator=Operator.XOR, children=[resource_allocate, skip])

# Choice for the stakeholder notification
choice_stakeholder_notification = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_notify, skip])

# Choice for the legal review
choice_legal_review = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])

# Choice for the media brief
choice_media_brief = OperatorPOWL(operator=Operator.XOR, children=[media_brief, skip])

# Choice for the response deployment
choice_response_deployment = OperatorPOWL(operator=Operator.XOR, children=[response_deploy, skip])

# Choice for the situation monitoring
choice_situation_monitoring = OperatorPOWL(operator=Operator.XOR, children=[situation_monitor, skip])

# Choice for the data collection
choice_data_collection = OperatorPOWL(operator=Operator.XOR, children=[data_collect, skip])

# Choice for the risk mitigation
choice_risk_mitigation = OperatorPOWL(operator=Operator.XOR, children=[risk_mitigate, skip])

# Choice for the external consultation
choice_external_consultation = OperatorPOWL(operator=Operator.XOR, children=[external_consult, skip])

# Choice for the status update
choice_status_update = OperatorPOWL(operator=Operator.XOR, children=[status_update, skip])

# Choice for the post-review
choice_post_review = OperatorPOWL(operator=Operator.XOR, children=[post_review, skip])

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    loop_recovery_plan,
    choice_initial_steps,
    choice_resource_allocation,
    choice_stakeholder_notification,
    choice_legal_review,
    choice_media_brief,
    choice_response_deployment,
    choice_situation_monitoring,
    choice_data_collection,
    choice_risk_mitigation,
    choice_external_consultation,
    choice_status_update,
    choice_post_review
])

# Define the dependencies
root.order.add_edge(loop_recovery_plan, choice_initial_steps)
root.order.add_edge(choice_initial_steps, choice_resource_allocation)
root.order.add_edge(choice_resource_allocation, choice_stakeholder_notification)
root.order.add_edge(choice_stakeholder_notification, choice_legal_review)
root.order.add_edge(choice_legal_review, choice_media_brief)
root.order.add_edge(choice_media_brief, choice_response_deployment)
root.order.add_edge(choice_response_deployment, choice_situation_monitoring)
root.order.add_edge(choice_situation_monitoring, choice_data_collection)
root.order.add_edge(choice_data_collection, choice_risk_mitigation)
root.order.add_edge(choice_risk_mitigation, choice_external_consultation)
root.order.add_edge(choice_external_consultation, choice_status_update)
root.order.add_edge(choice_status_update, choice_post_review)