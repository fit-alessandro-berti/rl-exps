import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
TrendScan = Transition(label='Trend Scan')
IdeaHarvest = Transition(label='Idea Harvest')
SectorMatch = Transition(label='Sector Match')
BrainstormHub = Transition(label='Brainstorm Hub')
ConceptFilter = Transition(label='Concept Filter')
PrototypeBuild = Transition(label='Prototype Build')
HybridTesting = Transition(label='Hybrid Testing')
StakeholderSync = Transition(label='Stakeholder Sync')
RiskAssess = Transition(label='Risk Assess')
ScenarioMap = Transition(label='Scenario Map')
StrategyAlign = Transition(label='Strategy Align')
PilotLaunch = Transition(label='Pilot Launch')
DataCapture = Transition(label='Data Capture')
MarketSense = Transition(label='Market Sense')
ScalePlan = Transition(label='Scale Plan')

# Define silent transitions (if any)
skip = SilentTransition()

# Define the process
loop = OperatorPOWL(operator=Operator.LOOP, children=[BrainstormHub, ScenarioMap])
xor = OperatorPOWL(operator=Operator.XOR, children=[HybridTesting, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[StrategyAlign, RiskAssess])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[PilotLaunch, DataCapture])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ScalePlan, MarketSense])

root = StrictPartialOrder(nodes=[TrendScan, IdeaHarvest, SectorMatch, loop, xor, xor2, xor3, xor4])
root.order.add_edge(TrendScan, IdeaHarvest)
root.order.add_edge(IdeaHarvest, SectorMatch)
root.order.add_edge(SectorMatch, loop)
root.order.add_edge(loop, BrainstormHub)
root.order.add_edge(BrainstormHub, ScenarioMap)
root.order.add_edge(ScenarioMap, xor)
root.order.add_edge(xor, HybridTesting)
root.order.add_edge(xor, skip)
root.order.add_edge(HybridTesting, xor2)
root.order.add_edge(xor2, StrategyAlign)
root.order.add_edge(xor2, RiskAssess)
root.order.add_edge(StrategyAlign, xor3)
root.order.add_edge(xor3, PilotLaunch)
root.order.add_edge(xor3, DataCapture)
root.order.add_edge(PilotLaunch, xor4)
root.order.add_edge(xor4, ScalePlan)
root.order.add_edge(xor4, MarketSense)

print(root)