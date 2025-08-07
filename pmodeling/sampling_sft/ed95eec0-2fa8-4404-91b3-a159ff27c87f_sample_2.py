import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
trend_scan    = Transition(label='Trend Scan')
idea_harvest  = Transition(label='Idea Harvest')
sector_match  = Transition(label='Sector Match')
brainstorm    = Transition(label='Brainstorm Hub')
concept_filter= Transition(label='Concept Filter')
prototype     = Transition(label='Prototype Build')
hybrid_test   = Transition(label='Hybrid Testing')
stakeholder   = Transition(label='Stakeholder Sync')
risk_assess   = Transition(label='Risk Assess')
scenario_map  = Transition(label='Scenario Map')
strategy_align= Transition(label='Strategy Align')
pilot_launch  = Transition(label='Pilot Launch')
data_capture  = Transition(label='Data Capture')
market_sense  = Transition(label='Market Sense')
scale_plan    = Transition(label='Scale Plan')

# Define the iterative feedback loop body: Data Capture -> Market Sense -> Scale Plan
feedback_body = StrictPartialOrder(nodes=[data_capture, market_sense, scale_plan])
feedback_body.order.add_edge(data_capture, market_sense)
feedback_body.order.add_edge(market_sense, scale_plan)

# Define the loop: Risk Assess -> Scenario Map -> Strategy Align -> (feedback_body)
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, scenario_map, strategy_align, feedback_body])

# Assemble the top-level partial order
root = StrictPartialOrder(nodes=[
    trend_scan,
    idea_harvest,
    sector_match,
    brainstorm,
    concept_filter,
    prototype,
    hybrid_test,
    stakeholder,
    feedback_loop
])

# Define the control-flow dependencies
root.order.add_edge(trend_scan, idea_harvest)
root.order.add_edge(idea_harvest, sector_match)
root.order.add_edge(sector_match, brainstorm)
root.order.add_edge(brainstorm, concept_filter)
root.order.add_edge(concept_filter, prototype)
root.order.add_edge(prototype, hybrid_test)
root.order.add_edge(hybrid_test, stakeholder)
root.order.add_edge(stakeholder, feedback_loop)

print(root)