import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with their labels
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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        alert_trigger,
        initial_assess,
        stakeholder_notify,
        resource_check,
        risk_analyze,
        command_setup,
        deploy_teams,
        data_collect,
        situation_update,
        priority_adjust,
        external_liaison,
        supply_dispatch,
        media_brief,
        impact_review,
        recovery_plan,
        process_audit
    ],
    order={
        (alert_trigger, initial_assess): True,
        (initial_assess, stakeholder_notify): True,
        (stakeholder_notify, resource_check): True,
        (resource_check, risk_analyze): True,
        (risk_analyze, command_setup): True,
        (command_setup, deploy_teams): True,
        (deploy_teams, data_collect): True,
        (data_collect, situation_update): True,
        (situation_update, priority_adjust): True,
        (priority_adjust, external_liaison): True,
        (external_liaison, supply_dispatch): True,
        (supply_dispatch, media_brief): True,
        (media_brief, impact_review): True,
        (impact_review, recovery_plan): True,
        (recovery_plan, process_audit): True
    }
)

# Print the root node
print(root)