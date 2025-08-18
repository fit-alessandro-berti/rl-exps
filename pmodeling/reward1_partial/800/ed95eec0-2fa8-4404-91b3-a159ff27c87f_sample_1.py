import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the transitions as silent transitions
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, hybrid_testing])
xor = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[scenario_map, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[strategy_align, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[pilot_launch, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[data_capture, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[market_sense, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[scale_plan, skip])

# Construct the root POWL model
root = StrictPartialOrder(nodes=[trend_scan, idea_harvest, sector_match, brainstorm_hub, concept_filter, loop, xor, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(trend_scan, idea_harvest)
root.order.add_edge(idea_harvest, sector_match)
root.order.add_edge(sector_match, brainstorm_hub)
root.order.add_edge(brainstorm_hub, concept_filter)
root.order.add_edge(concept_filter, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)