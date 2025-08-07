import pm4py
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

# Define the root of the process
root = StrictPartialOrder(nodes=[alert_trigger, initial_assess, stakeholder_notify, resource_check, risk_analyze, command_setup, deploy_teams, data_collect, situation_update, priority_adjust, external_liaison, supply_dispatch, media_brief, impact_review, recovery_plan, process_audit])

# Optionally, you can define dependencies if there are any between activities
# For example, if 'Alert Trigger' must occur before 'Initial Assess':
# root.order.add_edge(alert_trigger, initial_assess)

# If you want to save the final result in a variable, you can do so:
# root = root