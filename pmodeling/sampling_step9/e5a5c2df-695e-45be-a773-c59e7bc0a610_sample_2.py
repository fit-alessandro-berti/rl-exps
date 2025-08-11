import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

AlertTrigger = Transition(label='Alert Trigger')
InitialAssess = Transition(label='Initial Assess')
StakeholderNotify = Transition(label='Stakeholder Notify')
ResourceCheck = Transition(label='Resource Check')
RiskAnalyze = Transition(label='Risk Analyze')
CommandSetup = Transition(label='Command Setup')
DeployTeams = Transition(label='Deploy Teams')
DataCollect = Transition(label='Data Collect')
SituationUpdate = Transition(label='Situation Update')
PriorityAdjust = Transition(label='Priority Adjust')
ExternalLiaison = Transition(label='External Liaison')
SupplyDispatch = Transition(label='Supply Dispatch')
MediaBrief = Transition(label='Media Brief')
ImpactReview = Transition(label='Impact Review')
RecoveryPlan = Transition(label='Recovery Plan')
ProcessAudit = Transition(label='Process Audit')

skip = SilentTransition()

# Initial phases
InitialPhase = OperatorPOWL(operator=Operator.XOR, children=[AlertTrigger, InitialAssess])
StakeholderPhase = OperatorPOWL(operator=Operator.XOR, children=[StakeholderNotify, ResourceCheck])

# Decision-making and resource mobilization
DecisionPhase = OperatorPOWL(operator=Operator.XOR, children=[RiskAnalyze, CommandSetup])
ResourcePhase = OperatorPOWL(operator=Operator.XOR, children=[DeployTeams, DataCollect])

# Continuous monitoring
MonitoringPhase = OperatorPOWL(operator=Operator.XOR, children=[SituationUpdate, PriorityAdjust])
ExternalPhase = OperatorPOWL(operator=Operator.XOR, children=[ExternalLiaison, SupplyDispatch])
MediaPhase = OperatorPOWL(operator=Operator.XOR, children=[MediaBrief, ImpactReview])

# Recovery and audit
RecoveryPhase = OperatorPOWL(operator=Operator.XOR, children=[RecoveryPlan, ProcessAudit])

# Loop structure
root = StrictPartialOrder(nodes=[InitialPhase, StakeholderPhase, DecisionPhase, ResourcePhase, MonitoringPhase, ExternalPhase, MediaPhase, RecoveryPhase])
root.order.add_edge(InitialPhase, StakeholderPhase)
root.order.add_edge(InitialPhase, DecisionPhase)
root.order.add_edge(StakeholderPhase, DecisionPhase)
root.order.add_edge(DecisionPhase, ResourcePhase)
root.order.add_edge(ResourcePhase, MonitoringPhase)
root.order.add_edge(MonitoringPhase, ExternalPhase)
root.order.add_edge(ExternalPhase, MediaPhase)
root.order.add_edge(MediaPhase, RecoveryPhase)
root.order.add_edge(RecoveryPhase, InitialPhase)