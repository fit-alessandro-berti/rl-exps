import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process structure
alert_trigger_to_initial_assess = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[alert_trigger, initial_assess])
initial_assess_to_stakeholder_notify = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[initial_assess, stakeholder_notify])
stakeholder_notify_to_resource_check = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[stakeholder_notify, resource_check])
resource_check_to_risk_analyze = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[resource_check, risk_analyze])
risk_analyze_to_command_setup = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[risk_analyze, command_setup])
command_setup_to_deploy_teams = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[command_setup, deploy_teams])
deploy_teams_to_data_collect = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[deploy_teams, data_collect])
data_collect_to_situation_update = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[data_collect, situation_update])
situation_update_to_priority_adjust = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[situation_update, priority_adjust])
priority_adjust_to_external_liaison = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[priority_adjust, external_liaison])
external_liaison_to_supply_dispatch = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[external_liaison, supply_dispatch])
supply_dispatch_to_media_brief = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[supply_dispatch, media_brief])
media_brief_to_impact_review = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[media_brief, impact_review])
impact_review_to_recovery_plan = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[impact_review, recovery_plan])
recovery_plan_to_process_audit = OperatorPOWL(operator=Operator.EXCLUSIVE, children=[recovery_plan, process_audit])

# Define the partial order
root = StrictPartialOrder(nodes=[
    alert_trigger_to_initial_assess,
    initial_assess_to_stakeholder_notify,
    stakeholder_notify_to_resource_check,
    resource_check_to_risk_analyze,
    risk_analyze_to_command_setup,
    command_setup_to_deploy_teams,
    deploy_teams_to_data_collect,
    data_collect_to_situation_update,
    situation_update_to_priority_adjust,
    priority_adjust_to_external_liaison,
    external_liaison_to_supply_dispatch,
    supply_dispatch_to_media_brief,
    media_brief_to_impact_review,
    impact_review_to_recovery_plan,
    recovery_plan_to_process_audit
])

# Add dependencies
root.order.add_edge(alert_trigger_to_initial_assess, initial_assess_to_stakeholder_notify)
root.order.add_edge(initial_assess_to_stakeholder_notify, stakeholder_notify_to_resource_check)
root.order.add_edge(stakeholder_notify_to_resource_check, resource_check_to_risk_analyze)
root.order.add_edge(resource_check_to_risk_analyze, risk_analyze_to_command_setup)
root.order.add_edge(risk_analyze_to_command_setup, command_setup_to_deploy_teams)
root.order.add_edge(command_setup_to_deploy_teams, deploy_teams_to_data_collect)
root.order.add_edge(deploy_teams_to_data_collect, data_collect_to_situation_update)
root.order.add_edge(data_collect_to_situation_update, situation_update_to_priority_adjust)
root.order.add_edge(situation_update_to_priority_adjust, priority_adjust_to_external_liaison)
root.order.add_edge(priority_adjust_to_external_liaison, external_liaison_to_supply_dispatch)
root.order.add_edge(external_liaison_to_supply_dispatch, supply_dispatch_to_media_brief)
root.order.add_edge(supply_dispatch_to_media_brief, media_brief_to_impact_review)
root.order.add_edge(media_brief_to_impact_review, impact_review_to_recovery_plan)
root.order.add_edge(impact_review_to_recovery_plan, recovery_plan_to_process_audit)

print(root)