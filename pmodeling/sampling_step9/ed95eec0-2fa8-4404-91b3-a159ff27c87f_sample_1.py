import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice
xor = OperatorPOWL(operator=Operator.XOR, children=[PilotLaunch, skip])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[PrototypeBuild, HybridTesting])

# Define the root POWL model
root = StrictPartialOrder(nodes=[TrendScan, IdeaHarvest, SectorMatch, BrainstormHub, ConceptFilter, loop, xor, RiskAssess, ScenarioMap, StrategyAlign, DataCapture, MarketSense, ScalePlan])
root.order.add_edge(TrendScan, IdeaHarvest)
root.order.add_edge(IdeaHarvest, SectorMatch)
root.order.add_edge(SectorMatch, BrainstormHub)
root.order.add_edge(BrainstormHub, ConceptFilter)
root.order.add_edge(ConceptFilter, PrototypeBuild)
root.order.add_edge(PrototypeBuild, HybridTesting)
root.order.add_edge(HybridTesting, RiskAssess)
root.order.add_edge(RiskAssess, ScenarioMap)
root.order.add_edge(ScenarioMap, StrategyAlign)
root.order.add_edge(StrategyAlign, PilotLaunch)
root.order.add_edge(PilotLaunch, DataCapture)
root.order.add_edge(DataCapture, MarketSense)
root.order.add_edge(MarketSense, ScalePlan)