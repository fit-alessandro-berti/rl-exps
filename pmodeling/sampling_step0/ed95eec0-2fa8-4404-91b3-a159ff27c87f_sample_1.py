from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the loop nodes
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[trend_scan, idea_harvest])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[brainstorm_hub, concept_filter])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, hybrid_testing])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_sync, risk_assess])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[scenario_map, strategy_align])
loop_6 = OperatorPOWL(operator=Operator.LOOP, children=[pilot_launch, data_capture])
loop_7 = OperatorPOWL(operator=Operator.LOOP, children=[market_sense, scale_plan])

# Define the exclusive choice nodes
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[sector_match, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[sector_match, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_1, loop_2, loop_3, loop_4, loop_5, loop_6, loop_7, xor_1, xor_2])

# Define the dependencies
root.order.add_edge(loop_1, xor_1)
root.order.add_edge(loop_2, xor_1)
root.order.add_edge(loop_3, xor_1)
root.order.add_edge(loop_4, xor_1)
root.order.add_edge(loop_5, xor_1)
root.order.add_edge(loop_6, xor_1)
root.order.add_edge(loop_7, xor_1)
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_2, xor_2)

# Print the root POWL model
print(root)