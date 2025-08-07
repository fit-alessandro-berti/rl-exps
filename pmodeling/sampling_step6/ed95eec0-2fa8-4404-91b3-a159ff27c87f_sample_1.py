import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the partial order workflow
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

# Add dependencies if any (if not, no edges are needed)
# Example: root.order.add_edge(trend_scan, idea_harvest)

# Now 'root' contains the POWL model for the described process
print(root)