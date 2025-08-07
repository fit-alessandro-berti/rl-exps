import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    threat_assess,
    alert_dispatch,
    resource_check,
    team_mobilize,
    command_setup,
    intel_gather,
    risk_evaluate,
    priority_set,
    field_deploy,
    comm_sync,
    public_update,
    supply_manage,
    safety_monitor,
    incident_log,
    recovery_plan,
    debrief_team,
    data_archive
])

# Add dependencies if any (not specified in the problem statement, so we leave it empty)
# root.order.add_edge(...)  # Uncomment and add edges as needed

# Now 'root' contains the POWL model for the process
print(root)