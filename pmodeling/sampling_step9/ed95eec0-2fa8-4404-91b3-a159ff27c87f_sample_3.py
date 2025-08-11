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

# Define loop nodes
prototype_loop = OperatorPOWL(operator=Operator.LOOP, children=[PrototypeBuild, HybridTesting])
stakeholder_loop = OperatorPOWL(operator=Operator.LOOP, children=[StakeholderSync, RiskAssess, ScenarioMap, StrategyAlign])
pilot_loop = OperatorPOWL(operator=Operator.LOOP, children=[PilotLaunch, DataCapture, MarketSense, ScalePlan])

# Define exclusive choices
idea_choice = OperatorPOWL(operator=Operator.XOR, children=[IdeaHarvest, skip])
brainstorm_choice = OperatorPOWL(operator=Operator.XOR, children=[BrainstormHub, skip])
prototype_choice = OperatorPOWL(operator=Operator.XOR, children=[PrototypeBuild, skip])
hybrid_choice = OperatorPOWL(operator=Operator.XOR, children=[HybridTesting, skip])
stakeholder_choice = OperatorPOWL(operator=Operator.XOR, children=[StakeholderSync, skip])
scenario_choice = OperatorPOWL(operator=Operator.XOR, children=[ScenarioMap, skip])
strategy_choice = OperatorPOWL(operator=Operator.XOR, children=[StrategyAlign, skip])
pilot_choice = OperatorPOWL(operator=Operator.XOR, children=[PilotLaunch, skip])
data_choice = OperatorPOWL(operator=Operator.XOR, children=[DataCapture, skip])
market_choice = OperatorPOWL(operator=Operator.XOR, children=[MarketSense, skip])
scale_choice = OperatorPOWL(operator=Operator.XOR, children=[ScalePlan, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[prototype_loop, stakeholder_loop, pilot_loop, idea_choice, brainstorm_choice, prototype_choice, hybrid_choice, stakeholder_choice, scenario_choice, strategy_choice, pilot_choice, data_choice, market_choice, scale_choice])

# Define dependencies
root.order.add_edge(prototype_loop, stakeholder_loop)
root.order.add_edge(stakeholder_loop, pilot_loop)
root.order.add_edge(pilot_loop, data_choice)
root.order.add_edge(data_choice, market_choice)
root.order.add_edge(market_choice, scale_choice)
root.order.add_edge(idea_choice, prototype_choice)
root.order.add_edge(brainstorm_choice, prototype_choice)
root.order.add_edge(prototype_choice, hybrid_choice)
root.order.add_edge(hybrid_choice, stakeholder_choice)
root.order.add_edge(stakeholder_choice, scenario_choice)
root.order.add_edge(scenario_choice, strategy_choice)
root.order.add_edge(strategy_choice, pilot_choice)
root.order.add_edge(pilot_choice, data_choice)
root.order.add_edge(data_choice, market_choice)
root.order.add_edge(market_choice, scale_choice)

# Print the root POWL model
print(root)