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

# Define silent transitions for empty labels
Skip = SilentTransition()

# Define loop nodes and exclusive choices
loopBrainstorm = OperatorPOWL(operator=Operator.LOOP, children=[BrainstormHub, ConceptFilter])
xorPrototype = OperatorPOWL(operator=Operator.XOR, children=[PrototypeBuild, Skip])
xorHybrid = OperatorPOWL(operator=Operator.XOR, children=[HybridTesting, Skip])
xorRisk = OperatorPOWL(operator=Operator.XOR, children=[RiskAssess, Skip])
xorScenario = OperatorPOWL(operator=Operator.XOR, children=[ScenarioMap, Skip])
xorStrategy = OperatorPOWL(operator=Operator.XOR, children=[StrategyAlign, Skip])
xorPilot = OperatorPOWL(operator=Operator.XOR, children=[PilotLaunch, Skip])
xorData = OperatorPOWL(operator=Operator.XOR, children=[DataCapture, Skip])
xorMarket = OperatorPOWL(operator=Operator.XOR, children=[MarketSense, Skip])
xorScale = OperatorPOWL(operator=Operator.XOR, children=[ScalePlan, Skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    TrendScan,
    IdeaHarvest,
    SectorMatch,
    BrainstormHub,
    ConceptFilter,
    PrototypeBuild,
    HybridTesting,
    StakeholderSync,
    RiskAssess,
    ScenarioMap,
    StrategyAlign,
    PilotLaunch,
    DataCapture,
    MarketSense,
    ScalePlan,
    loopBrainstorm,
    xorPrototype,
    xorHybrid,
    xorRisk,
    xorScenario,
    xorStrategy,
    xorPilot,
    xorData,
    xorMarket,
    xorScale
])

# Define dependencies between nodes
root.order.add_edge(TrendScan, IdeaHarvest)
root.order.add_edge(IdeaHarvest, SectorMatch)
root.order.add_edge(SectorMatch, BrainstormHub)
root.order.add_edge(BrainstormHub, ConceptFilter)
root.order.add_edge(ConceptFilter, PrototypeBuild)
root.order.add_edge(PrototypeBuild, HybridTesting)
root.order.add_edge(HybridTesting, StakeholderSync)
root.order.add_edge(StakeholderSync, RiskAssess)
root.order.add_edge(RiskAssess, ScenarioMap)
root.order.add_edge(ScenarioMap, StrategyAlign)
root.order.add_edge(StrategyAlign, PilotLaunch)
root.order.add_edge(PilotLaunch, DataCapture)
root.order.add_edge(DataCapture, MarketSense)
root.order.add_edge(MarketSense, ScalePlan)
root.order.add_edge(PrototypeBuild, xorPrototype)
root.order.add_edge(HybridTesting, xorHybrid)
root.order.add_edge(RiskAssess, xorRisk)
root.order.add_edge(ScenarioMap, xorScenario)
root.order.add_edge(StrategyAlign, xorStrategy)
root.order.add_edge(PilotLaunch, xorPilot)
root.order.add_edge(DataCapture, xorData)
root.order.add_edge(MarketSense, xorMarket)
root.order.add_edge(ScalePlan, xorScale)
root.order.add_edge(loopBrainstorm, xorPrototype)
root.order.add_edge(xorPrototype, xorHybrid)
root.order.add_edge(xorHybrid, xorRisk)
root.order.add_edge(xorRisk, xorScenario)
root.order.add_edge(xorScenario, xorStrategy)
root.order.add_edge(xorStrategy, xorPilot)
root.order.add_edge(xorPilot, xorData)
root.order.add_edge(xorData, xorMarket)
root.order.add_edge(xorMarket, xorScale)

# Print the root of the POWL model
print(root)