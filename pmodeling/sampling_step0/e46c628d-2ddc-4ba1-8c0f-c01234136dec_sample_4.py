from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model
loop_threat_assess = OperatorPOWL(operator=Operator.LOOP, children=[threat_assess])
xor_resource_check = OperatorPOWL(operator=Operator.XOR, children=[resource_check, skip])
xor_alert_dispatch = OperatorPOWL(operator=Operator.XOR, children=[alert_dispatch, skip])
xor_command_setup = OperatorPOWL(operator=Operator.XOR, children=[command_setup, skip])
xor_intel_gather = OperatorPOWL(operator=Operator.XOR, children=[intel_gather, skip])
xor_risk_evaluate = OperatorPOWL(operator=Operator.XOR, children=[risk_evaluate, skip])
xor_priority_set = OperatorPOWL(operator=Operator.XOR, children=[priority_set, skip])
xor_field_deploy = OperatorPOWL(operator=Operator.XOR, children=[field_deploy, skip])
xor_comm_sync = OperatorPOWL(operator=Operator.XOR, children=[comm_sync, skip])
xor_public_update = OperatorPOWL(operator=Operator.XOR, children=[public_update, skip])
xor_supply_manage = OperatorPOWL(operator=Operator.XOR, children=[supply_manage, skip])
xor_safety_monitor = OperatorPOWL(operator=Operator.XOR, children=[safety_monitor, skip])
xor_incident_log = OperatorPOWL(operator=Operator.XOR, children=[incident_log, skip])
xor_recovery_plan = OperatorPOWL(operator=Operator.XOR, children=[recovery_plan, skip])
xor_debrief_team = OperatorPOWL(operator=Operator.XOR, children=[debrief_team, skip])
xor_data_archive = OperatorPOWL(operator=Operator.XOR, children=[data_archive, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    loop_threat_assess,
    xor_resource_check,
    xor_alert_dispatch,
    xor_command_setup,
    xor_intel_gather,
    xor_risk_evaluate,
    xor_priority_set,
    xor_field_deploy,
    xor_comm_sync,
    xor_public_update,
    xor_supply_manage,
    xor_safety_monitor,
    xor_incident_log,
    xor_recovery_plan,
    xor_debrief_team,
    xor_data_archive
])

# Define the edges
root.order.add_edge(loop_threat_assess, xor_resource_check)
root.order.add_edge(loop_threat_assess, xor_alert_dispatch)
root.order.add_edge(loop_threat_assess, xor_command_setup)
root.order.add_edge(loop_threat_assess, xor_intel_gather)
root.order.add_edge(loop_threat_assess, xor_risk_evaluate)
root.order.add_edge(loop_threat_assess, xor_priority_set)
root.order.add_edge(loop_threat_assess, xor_field_deploy)
root.order.add_edge(loop_threat_assess, xor_comm_sync)
root.order.add_edge(loop_threat_assess, xor_public_update)
root.order.add_edge(loop_threat_assess, xor_supply_manage)
root.order.add_edge(loop_threat_assess, xor_safety_monitor)
root.order.add_edge(loop_threat_assess, xor_incident_log)
root.order.add_edge(loop_threat_assess, xor_recovery_plan)
root.order.add_edge(loop_threat_assess, xor_debrief_team)
root.order.add_edge(loop_threat_assess, xor_data_archive)

print(root)