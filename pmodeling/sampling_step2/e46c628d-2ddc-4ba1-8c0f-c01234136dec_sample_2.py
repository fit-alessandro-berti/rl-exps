import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
ThreatAssess = Transition(label='Threat Assess')
AlertDispatch = Transition(label='Alert Dispatch')
ResourceCheck = Transition(label='Resource Check')
TeamMobilize = Transition(label='Team Mobilize')
CommandSetup = Transition(label='Command Setup')
IntelGather = Transition(label='Intel Gather')
RiskEvaluate = Transition(label='Risk Evaluate')
PrioritySet = Transition(label='Priority Set')
FieldDeploy = Transition(label='Field Deploy')
CommSync = Transition(label='Comm Sync')
PublicUpdate = Transition(label='Public Update')
SupplyManage = Transition(label='Supply Manage')
SafetyMonitor = Transition(label='Safety Monitor')
IncidentLog = Transition(label='Incident Log')
RecoveryPlan = Transition(label='Recovery Plan')
DebriefTeam = Transition(label='Debrief Team')
DataArchive = Transition(label='Data Archive')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    ThreatAssess,
    AlertDispatch,
    ResourceCheck,
    TeamMobilize,
    CommandSetup,
    IntelGather,
    RiskEvaluate,
    PrioritySet,
    FieldDeploy,
    CommSync,
    PublicUpdate,
    SupplyManage,
    SafetyMonitor,
    IncidentLog,
    RecoveryPlan,
    DebriefTeam,
    DataArchive
])

# Define the partial order dependencies
root.order.add_edge(ThreatAssess, AlertDispatch)
root.order.add_edge(AlertDispatch, ResourceCheck)
root.order.add_edge(ResourceCheck, TeamMobilize)
root.order.add_edge(TeamMobilize, CommandSetup)
root.order.add_edge(CommandSetup, IntelGather)
root.order.add_edge(IntelGather, RiskEvaluate)
root.order.add_edge(RiskEvaluate, PrioritySet)
root.order.add_edge(PrioritySet, FieldDeploy)
root.order.add_edge(FieldDeploy, CommSync)
root.order.add_edge(CommSync, PublicUpdate)
root.order.add_edge(PublicUpdate, SupplyManage)
root.order.add_edge(SupplyManage, SafetyMonitor)
root.order.add_edge(SafetyMonitor, IncidentLog)
root.order.add_edge(IncidentLog, RecoveryPlan)
root.order.add_edge(RecoveryPlan, DebriefTeam)
root.order.add_edge(DebriefTeam, DataArchive)