import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
alert_trigger = Transition(label='Alert Trigger')
initial_assess = Transition(label='Initial Assess')
stakeholder_notify = Transition(label='Stakeholder Notify')
resource_check = Transition(label='Resource Check')
risk_analyze = Transition(label='Risk Analyze')
command_setup = Transition(label='Command Setup')
deploy_teams = Transition(label='Deploy Teams')
data_collect = Transition(label='Data Collect')
situation_update = Transition(label='Situation Update')
priority_adjust = Transition(label='Priority Adjust')
external_liaison = Transition(label='External Liaison')
supply_dispatch = Transition(label='Supply Dispatch')
media_brief = Transition(label='Media Brief')
impact_review = Transition(label='Impact Review')
recovery_plan = Transition(label='Recovery Plan')
process_audit = Transition(label='Process Audit')

skip = SilentTransition()

# Define the loop for resource mobilization and risk mitigation
loop_resource_mobilization = OperatorPOWL(operator=Operator.LOOP, children=[resource_check, risk_analyze])

# Define the exclusive choice for initial assessment and stakeholder notification
exclusive_choice_initial_assess_stakeholder_notify = OperatorPOWL(operator=Operator.XOR, children=[initial_assess, stakeholder_notify])

# Define the exclusive choice for command setup and deployment of teams
exclusive_choice_command_setup_deploy_teams = OperatorPOWL(operator=Operator.XOR, children=[command_setup, deploy_teams])

# Define the exclusive choice for data collection and situation update
exclusive_choice_data_collect_situation_update = OperatorPOWL(operator=Operator.XOR, children=[data_collect, situation_update])

# Define the exclusive choice for priority adjustment and external liaison
exclusive_choice_priority_adjust_external_liaison = OperatorPOWL(operator=Operator.XOR, children=[priority_adjust, external_liaison])

# Define the exclusive choice for supply dispatch and media brief
exclusive_choice_supply_dispatch_media_brief = OperatorPOWL(operator=Operator.XOR, children=[supply_dispatch, media_brief])

# Define the exclusive choice for impact review and recovery plan
exclusive_choice_impact_review_recovery_plan = OperatorPOWL(operator=Operator.XOR, children=[impact_review, recovery_plan])

# Define the exclusive choice for process audit and end
exclusive_choice_process_audit_end = OperatorPOWL(operator=Operator.XOR, children=[process_audit, skip])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[alert_trigger, exclusive_choice_initial_assess_stakeholder_notify, exclusive_choice_command_setup_deploy_teams, exclusive_choice_data_collect_situation_update, exclusive_choice_priority_adjust_external_liaison, exclusive_choice_supply_dispatch_media_brief, exclusive_choice_impact_review_recovery_plan, exclusive_choice_process_audit_end])
root.order.add_edge(alert_trigger, exclusive_choice_initial_assess_stakeholder_notify)
root.order.add_edge(exclusive_choice_initial_assess_stakeholder_notify, exclusive_choice_command_setup_deploy_teams)
root.order.add_edge(exclusive_choice_command_setup_deploy_teams, exclusive_choice_data_collect_situation_update)
root.order.add_edge(exclusive_choice_data_collect_situation_update, exclusive_choice_priority_adjust_external_liaison)
root.order.add_edge(exclusive_choice_priority_adjust_external_liaison, exclusive_choice_supply_dispatch_media_brief)
root.order.add_edge(exclusive_choice_supply_dispatch_media_brief, exclusive_choice_impact_review_recovery_plan)
root.order.add_edge(exclusive_choice_impact_review_recovery_plan, exclusive_choice_process_audit_end)

print(root)