from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loops and XORs
# The alert trigger leads to initial assessment and stakeholder notification
# Initial assessment leads to resource check, risk analysis, command setup, deploy teams, data collection, situation update, priority adjustment, external liaison, supply dispatch, media brief, impact review, recovery plan, and process audit
# These steps are repeated until the process is complete
root = StrictPartialOrder(nodes=[alert_trigger, initial_assess, stakeholder_notify, resource_check, risk_analyze, command_setup, deploy_teams, data_collect, situation_update, priority_adjust, external_liaison, supply_dispatch, media_brief, impact_review, recovery_plan, process_audit])
root.order.add_edge(alert_trigger, initial_assess)
root.order.add_edge(initial_assess, stakeholder_notify)
root.order.add_edge(stakeholder_notify, resource_check)
root.order.add_edge(resource_check, risk_analyze)
root.order.add_edge(risk_analyze, command_setup)
root.order.add_edge(command_setup, deploy_teams)
root.order.add_edge(deploy_teams, data_collect)
root.order.add_edge(data_collect, situation_update)
root.order.add_edge(situation_update, priority_adjust)
root.order.add_edge(priority_adjust, external_liaison)
root.order.add_edge(external_liaison, supply_dispatch)
root.order.add_edge(supply_dispatch, media_brief)
root.order.add_edge(media_brief, impact_review)
root.order.add_edge(impact_review, recovery_plan)
root.order.add_edge(recovery_plan, process_audit)