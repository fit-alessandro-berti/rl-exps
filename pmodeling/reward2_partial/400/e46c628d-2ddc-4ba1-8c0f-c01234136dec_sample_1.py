from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
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

# Add edges to define the partial order
root.order.add_edge(Threat_Assess, Alert_Dispatch)
root.order.add_edge(Threat_Assess, Resource_Check)
root.order.add_edge(Alert_Dispatch, Team_Mobilize)
root.order.add_edge(Resource_Check, Team_Mobilize)
root.order.add_edge(Team_Mobilize, Command_Setup)
root.order.add_edge(Command_Setup, Intel_Gather)
root.order.add_edge(Intel_Gather, Risk_Evaluate)
root.order.add_edge(Risk_Evaluate, Priority_Set)
root.order.add_edge(Priority_Set, Field_Deploy)
root.order.add_edge(Field_Deploy, Comm_Sync)
root.order.add_edge(Comm_Sync, Public_Update)
root.order.add_edge(Public_Update, Supply_Manage)
root.order.add_edge(Supply_Manage, Safety_Monitor)
root.order.add_edge(Safety_Monitor, Incident_Log)
root.order.add_edge(Incident_Log, Recovery_Plan)
root.order.add_edge(Recovery_Plan, Debrief_Team)
root.order.add_edge(Debrief_Team, Data_Archive)

# Print the root POWL model
print(root)