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

root = StrictPartialOrder(nodes=[
    Threat_Assess,
    Alert_Dispatch,
    Resource_Check,
    Team_Mobilize,
    Command_Setup,
    Intel_Gather,
    Risk_Evaluate,
    Priority_Set,
    Field_Deploy,
    Comm_Sync,
    Public_Update,
    Supply_Manage,
    Safety_Monitor,
    Incident_Log,
    Recovery_Plan,
    Debrief_Team,
    Data_Archive
])

# Assuming the order is not explicitly specified, we can set up the order in a straightforward manner
# for simplicity, we assume the order is the natural execution order of the activities
root.order.add_edge(Threat_Assess, Alert_Dispatch)
root.order.add_edge(Threat_Assess, Resource_Check)
root.order.add_edge(Threat_Assess, Team_Mobilize)
root.order.add_edge(Threat_Assess, Command_Setup)
root.order.add_edge(Threat_Assess, Intel_Gather)
root.order.add_edge(Threat_Assess, Risk_Evaluate)
root.order.add_edge(Threat_Assess, Priority_Set)
root.order.add_edge(Threat_Assess, Field_Deploy)
root.order.add_edge(Threat_Assess, Comm_Sync)
root.order.add_edge(Threat_Assess, Public_Update)
root.order.add_edge(Threat_Assess, Supply_Manage)
root.order.add_edge(Threat_Assess, Safety_Monitor)
root.order.add_edge(Threat_Assess, Incident_Log)
root.order.add_edge(Threat_Assess, Recovery_Plan)
root.order.add_edge(Threat_Assess, Debrief_Team)
root.order.add_edge(Threat_Assess, Data_Archive)