import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the operators
xor = OperatorPOWL(operator=Operator.XOR, children=[concept_filter, prototype_build])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, scenario_map])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[strategy_align, pilot_launch])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[data_capture, market_sense])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[scale_plan, None])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor, xor2, xor3, xor4, xor5])

# Define the root
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, loop)

# Print the root
print(root)