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

# Define silent transition
skip = SilentTransition()

# Define the process tree
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    threat_assess, alert_dispatch, resource_check, team_mobilize, command_setup,
    intel_gather, risk_evaluate, priority_set, field_deploy, comm_sync, public_update,
    supply_manage, safety_monitor, incident_log, recovery_plan, debrief_team, data_archive
])

# Define the partial order
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, threat_assess)
root.order.add_edge(loop, alert_dispatch)
root.order.add_edge(loop, resource_check)
root.order.add_edge(loop, team_mobilize)
root.order.add_edge(loop, command_setup)
root.order.add_edge(loop, intel_gather)
root.order.add_edge(loop, risk_evaluate)
root.order.add_edge(loop, priority_set)
root.order.add_edge(loop, field_deploy)
root.order.add_edge(loop, comm_sync)
root.order.add_edge(loop, public_update)
root.order.add_edge(loop, supply_manage)
root.order.add_edge(loop, safety_monitor)
root.order.add_edge(loop, incident_log)
root.order.add_edge(loop, recovery_plan)
root.order.add_edge(loop, debrief_team)
root.order.add_edge(loop, data_archive)