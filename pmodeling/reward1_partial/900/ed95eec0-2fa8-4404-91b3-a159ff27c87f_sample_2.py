import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the relationships between the activities using OperatorPOWL
brainstorm = OperatorPOWL(operator=Operator.XOR, children=[SectorMatch, IdeaHarvest])
prototype = OperatorPOWL(operator=Operator.XOR, children=[ConceptFilter, HybridTesting])
stakeholder = OperatorPOWL(operator=Operator.XOR, children=[StakeholderSync, RiskAssess])
scenario = OperatorPOWL(operator=Operator.XOR, children=[ScenarioMap, StrategyAlign])
market = OperatorPOWL(operator=Operator.XOR, children=[MarketSense, ScalePlan])

# Create the StrictPartialOrder object
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
    ScalePlan
])

# Define the order dependencies
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