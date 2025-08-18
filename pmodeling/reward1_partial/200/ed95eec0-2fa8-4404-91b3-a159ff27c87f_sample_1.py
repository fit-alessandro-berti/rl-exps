import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define silent transitions for empty labels
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, hybrid_testing, risk_assess, scenario_map, strategy_align])
xor = OperatorPOWL(operator=Operator.XOR, children=[pilot_launch, data_capture, market_sense, scale_plan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[brainstorm_hub, concept_filter])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[idea_harvest, sector_match])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[trend_scan, xor3])

root = StrictPartialOrder(nodes=[xor4, loop, xor2, xor])
root.order.add_edge(xor4, loop)
root.order.add_edge(xor4, xor2)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, xor)