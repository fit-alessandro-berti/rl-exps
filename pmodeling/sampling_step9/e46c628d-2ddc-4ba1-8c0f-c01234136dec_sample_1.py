import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loop and choice nodes
loop_resource_check = OperatorPOWL(operator=Operator.LOOP, children=[resource_check, skip])
choice_alert_dispatch = OperatorPOWL(operator=Operator.XOR, children=[alert_dispatch, skip])
choice_team_mobilize = OperatorPOWL(operator=Operator.XOR, children=[team_mobilize, skip])
choice_command_setup = OperatorPOWL(operator=Operator.XOR, children=[command_setup, skip])
choice_intel_gather = OperatorPOWL(operator=Operator.XOR, children=[intel_gather, skip])
choice_priority_set = OperatorPOWL(operator=Operator.XOR, children=[priority_set, skip])
choice_field_deploy = OperatorPOWL(operator=Operator.XOR, children=[field_deploy, skip])
choice_comm_sync = OperatorPOWL(operator=Operator.XOR, children=[comm_sync, skip])
choice_public_update = OperatorPOWL(operator=Operator.XOR, children=[public_update, skip])
choice_supply_manage = OperatorPOWL(operator=Operator.XOR, children=[supply_manage, skip])
choice_safety_monitor = OperatorPOWL(operator=Operator.XOR, children=[safety_monitor, skip])
choice_incident_log = OperatorPOWL(operator=Operator.XOR, children=[incident_log, skip])
choice_recovery_plan = OperatorPOWL(operator=Operator.XOR, children=[recovery_plan, skip])
choice_debrief_team = OperatorPOWL(operator=Operator.XOR, children=[debrief_team, skip])
choice_data_archive = OperatorPOWL(operator=Operator.XOR, children=[data_archive, skip])

# Define root node
root = StrictPartialOrder(nodes=[loop_resource_check, choice_alert_dispatch, choice_team_mobilize, choice_command_setup, choice_intel_gather, choice_priority_set, choice_field_deploy, choice_comm_sync, choice_public_update, choice_supply_manage, choice_safety_monitor, choice_incident_log, choice_recovery_plan, choice_debrief_team, choice_data_archive])

# Define dependencies
root.order.add_edge(loop_resource_check, choice_alert_dispatch)
root.order.add_edge(choice_alert_dispatch, choice_team_mobilize)
root.order.add_edge(choice_team_mobilize, choice_command_setup)
root.order.add_edge(choice_command_setup, choice_intel_gather)
root.order.add_edge(choice_intel_gather, choice_priority_set)
root.order.add_edge(choice_priority_set, choice_field_deploy)
root.order.add_edge(choice_field_deploy, choice_comm_sync)
root.order.add_edge(choice_comm_sync, choice_public_update)
root.order.add_edge(choice_public_update, choice_supply_manage)
root.order.add_edge(choice_supply_manage, choice_safety_monitor)
root.order.add_edge(choice_safety_monitor, choice_incident_log)
root.order.add_edge(choice_incident_log, choice_recovery_plan)
root.order.add_edge(choice_recovery_plan, choice_debrief_team)
root.order.add_edge(choice_debrief_team, choice_data_archive)

# Print the POWL model
print(root)