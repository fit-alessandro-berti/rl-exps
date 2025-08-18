import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define each activity as a transition
threat_assess = Transition(label='Threat Assess')
alert_dispatch = Transition(label='Alert Dispatch')
resource_check = Transition(label='Resource Check')
team_mobilize = Transition(label='Team Mobilize')
command_setup = Transition(label='Command Setup')
intel_gather = Transition(label='Intel Gather')
risk_evaluate = Transition(label='Risk Evaluate')
priority_set = Transition(label='Priority Set')
field_deploy = Transition(label='Field Deploy')
comm_sync = Transition(label='Comm Sync')
public_update = Transition(label='Public Update')
supply_manage = Transition(label='Supply Manage')
safety_monitor = Transition(label='Safety Monitor')
incident_log = Transition(label='Incident Log')
recovery_plan = Transition(label='Recovery Plan')
debrief_team = Transition(label='Debrief Team')
data_archive = Transition(label='Data Archive')

# Define the process flow using the defined activities
threat_assess_child = OperatorPOWL(operator=Operator.XOR, children=[resource_check, alert_dispatch])
command_setup_child = OperatorPOWL(operator=Operator.XOR, children=[intel_gather, risk_evaluate])
priority_set_child = OperatorPOWL(operator=Operator.XOR, children=[command_setup, team_mobilize])
field_deploy_child = OperatorPOWL(operator=Operator.XOR, children=[comm_sync, public_update])
supply_manage_child = OperatorPOWL(operator=Operator.XOR, children=[safety_monitor, incident_log])
recovery_plan_child = OperatorPOWL(operator=Operator.XOR, children=[debrief_team, data_archive])

root = StrictPartialOrder(
    nodes=[threat_assess, alert_dispatch, resource_check, team_mobilize, command_setup, intel_gather, risk_evaluate,
           priority_set, field_deploy, comm_sync, public_update, supply_manage, safety_monitor, incident_log,
           recovery_plan, debrief_team, data_archive],
    order={
        (threat_assess, command_setup_child): True,
        (command_setup_child, field_deploy_child): True,
        (field_deploy_child, supply_manage_child): True,
        (supply_manage_child, recovery_plan_child): True,
        (command_setup_child, priority_set_child): True,
        (priority_set_child, field_deploy_child): True,
        (field_deploy_child, supply_manage_child): True,
        (supply_manage_child, recovery_plan_child): True,
        (command_setup_child, debrief_team): True,
        (debrief_team, data_archive): True
    }
)

print(root)