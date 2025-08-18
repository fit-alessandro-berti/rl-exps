import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
trend_scan = Transition(label='Trend Scan')
idea_harvest = Transition(label='Idea Harvest')
sector_match = Transition(label='Sector Match')
brainstorm_hub = Transition(label='Brainstorm Hub')
concept_filter = Transition(label='Concept Filter')
prototype_build = Transition(label='Prototype Build')
hybrid_testing = Transition(label='Hybrid Testing')
stakeholder_sync = Transition(label='Stakeholder Sync')
risk_assess = Transition(label='Risk Assess')
scenario_map = Transition(label='Scenario Map')
strategy_align = Transition(label='Strategy Align')
pilot_launch = Transition(label='Pilot Launch')
data_capture = Transition(label='Data Capture')
market_sense = Transition(label='Market Sense')
scale_plan = Transition(label='Scale Plan')

# Define the partial order
root = StrictPartialOrder(nodes=[
    trend_scan,
    idea_harvest,
    sector_match,
    brainstorm_hub,
    concept_filter,
    prototype_build,
    hybrid_testing,
    stakeholder_sync,
    risk_assess,
    scenario_map,
    strategy_align,
    pilot_launch,
    data_capture,
    market_sense,
    scale_plan
])

# Define the dependencies
root.order.add_edge(trend_scan, idea_harvest)
root.order.add_edge(idea_harvest, sector_match)
root.order.add_edge(sector_match, brainstorm_hub)
root.order.add_edge(brainstorm_hub, concept_filter)
root.order.add_edge(concept_filter, prototype_build)
root.order.add_edge(prototype_build, hybrid_testing)
root.order.add_edge(hybrid_testing, stakeholder_sync)
root.order.add_edge(stakeholder_sync, risk_assess)
root.order.add_edge(risk_assess, scenario_map)
root.order.add_edge(scenario_map, strategy_align)
root.order.add_edge(strategy_align, pilot_launch)
root.order.add_edge(pilot_launch, data_capture)
root.order.add_edge(data_capture, market_sense)
root.order.add_edge(market_sense, scale_plan)

# Print the root POWL model
print(root)