import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Threat_Assess = Transition(label='Threat Assess')
Alert_Dispatch = Transition(label='Alert Dispatch')
Resource_Check = Transition(label='Resource Check')
Team_Mobilize = Transition(label='Team Mobilize')
Command_Setup = Transition(label='Command Setup')
Intel_Gather = Transition(label='Intel Gather')
Risk_Evaluate = Transition(label='Risk Evaluate')
Priority_Set = Transition(label='Priority Set')
Field_Deploy = Transition(label='Field Deploy')
Comm_Sync = Transition(label='Comm Sync')
Public_Update = Transition(label='Public Update')
Supply_Manage = Transition(label='Supply Manage')
Safety_Monitor = Transition(label='Safety Monitor')
Incident_Log = Transition(label='Incident Log')
Recovery_Plan = Transition(label='Recovery Plan')
Debrief_Team = Transition(label='Debrief Team')
Data_Archive = Transition(label='Data Archive')

skip = SilentTransition()

# Define the POWL model
threat_assess = OperatorPOWL(operator=Operator.AND, children=[Threat_Assess, Alert_Dispatch])
resource_check = OperatorPOWL(operator=Operator.AND, children=[Resource_Check, Team_Mobilize])
command_setup = OperatorPOWL(operator=Operator.AND, children=[Command_Setup, Intel_Gather])
risk_evaluate = OperatorPOWL(operator=Operator.AND, children=[Risk_Evaluate, Priority_Set])
field_deploy = OperatorPOWL(operator=Operator.AND, children=[Field_Deploy, Comm_Sync])
public_update = OperatorPOWL(operator=Operator.AND, children=[Public_Update, Supply_Manage])
safety_monitor = OperatorPOWL(operator=Operator.AND, children=[Safety_Monitor, Incident_Log])
recovery_plan = OperatorPOWL(operator=Operator.AND, children=[Recovery_Plan, Debrief_Team])
data_archive = OperatorPOWL(operator=Operator.AND, children=[Data_Archive])

# Define the partial order
root = StrictPartialOrder(nodes=[threat_assess, resource_check, command_setup, risk_evaluate, field_deploy, public_update, safety_monitor, recovery_plan, data_archive])
root.order.add_edge(threat_assess, resource_check)
root.order.add_edge(resource_check, command_setup)
root.order.add_edge(command_setup, risk_evaluate)
root.order.add_edge(risk_evaluate, field_deploy)
root.order.add_edge(field_deploy, public_update)
root.order.add_edge(public_update, safety_monitor)
root.order.add_edge(safety_monitor, recovery_plan)
root.order.add_edge(recovery_plan, data_archive)

print(root)