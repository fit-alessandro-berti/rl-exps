import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define each activity
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

# Define operators for the process flow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[sector_match, idea_harvest])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[brainstorm_hub, concept_filter])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, hybrid_testing])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_sync, risk_assess])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[scenario_map, strategy_align])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[pilot_launch, data_capture])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[market_sense, scale_plan])

# Define the partial order
root = StrictPartialOrder(nodes=[trend_scan, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(trend_scan, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)