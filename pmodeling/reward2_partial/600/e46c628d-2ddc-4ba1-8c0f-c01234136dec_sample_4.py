import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    threat_assess, alert_dispatch, resource_check, team_mobilize, command_setup, 
    intel_gather, risk_evaluate, priority_set, field_deploy, comm_sync, public_update, 
    supply_manage, safety_monitor, incident_log, recovery_plan, debrief_team, data_archive
])

# Define the order of the nodes
root.order.add_edge(threat_assess, alert_dispatch)
root.order.add_edge(alert_dispatch, resource_check)
root.order.add_edge(resource_check, team_mobilize)
root.order.add_edge(team_mobilize, command_setup)
root.order.add_edge(command_setup, intel_gather)
root.order.add_edge(intel_gather, risk_evaluate)
root.order.add_edge(risk_evaluate, priority_set)
root.order.add_edge(priority_set, field_deploy)
root.order.add_edge(field_deploy, comm_sync)
root.order.add_edge(comm_sync, public_update)
root.order.add_edge(public_update, supply_manage)
root.order.add_edge(supply_manage, safety_monitor)
root.order.add_edge(safety_monitor, incident_log)
root.order.add_edge(incident_log, recovery_plan)
root.order.add_edge(recovery_plan, debrief_team)
root.order.add_edge(debrief_team, data_archive)

print(root)