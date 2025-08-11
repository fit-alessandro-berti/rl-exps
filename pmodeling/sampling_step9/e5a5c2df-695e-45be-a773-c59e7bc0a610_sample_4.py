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

# Loop for initial assessment and resource check
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[InitialAssess, ResourceCheck])

# Exclusive choice for risk analysis and command setup
xor1 = OperatorPOWL(operator=Operator.XOR, children=[RiskAnalyze, CommandSetup])

# Loop for deploying teams and data collection
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[DeployTeams, DataCollect])

# Exclusive choice for situation update and priority adjustment
xor2 = OperatorPOWL(operator=Operator.XOR, children=[SituationUpdate, PriorityAdjust])

# Loop for external liaison and supply dispatch
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[ExternalLiaison, SupplyDispatch])

# Exclusive choice for media brief and impact review
xor3 = OperatorPOWL(operator=Operator.XOR, children=[MediaBrief, ImpactReview])

# Exclusive choice for recovery plan and process audit
xor4 = OperatorPOWL(operator=Operator.XOR, children=[RecoveryPlan, ProcessAudit])

# Overall POWL model
root = StrictPartialOrder(nodes=[loop1, xor1, loop2, xor2, loop3, xor3, xor4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, loop3)
root.order.add_edge(loop3, xor3)
root.order.add_edge(xor3, xor4)