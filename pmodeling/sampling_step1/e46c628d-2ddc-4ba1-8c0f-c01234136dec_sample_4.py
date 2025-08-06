import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the initial and final transitions
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[team_mobilize, command_setup])
xor = OperatorPOWL(operator=Operator.XOR, children=[field_deploy, comm_sync])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Add the remaining activities to the POWL model
root.nodes.append(alert_dispatch)
root.nodes.append(resource_check)
root.nodes.append(intel_gather)
root.nodes.append(risk_evaluate)
root.nodes.append(priority_set)
root.nodes.append(supply_manage)
root.nodes.append(safety_monitor)
root.nodes.append(incident_log)
root.nodes.append(recovery_plan)
root.nodes.append(debrief_team)
root.nodes.append(data_archive)

# Add the necessary edges to the POWL model
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

# Print the final POWL model
print(root)