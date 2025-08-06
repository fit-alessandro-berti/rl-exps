import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Trend_Scan = Transition(label='Trend Scan')
Idea_Harvest = Transition(label='Idea Harvest')
Sector_Match = Transition(label='Sector Match')
Brainstorm_Hub = Transition(label='Brainstorm Hub')
Concept_Filter = Transition(label='Concept Filter')
Prototype_Build = Transition(label='Prototype Build')
Hybrid_Testing = Transition(label='Hybrid Testing')
Stakeholder_Sync = Transition(label='Stakeholder Sync')
Risk_Assess = Transition(label='Risk Assess')
Scenario_Map = Transition(label='Scenario Map')
Strategy_Align = Transition(label='Strategy Align')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Capture = Transition(label='Data Capture')
Market_Sense = Transition(label='Market Sense')
Scale_Plan = Transition(label='Scale Plan')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_idea_harvest = OperatorPOWL(operator=Operator.LOOP, children=[Brainstorm_Hub, Risk_Assess, Scenario_Map, Strategy_Align, Pilot_Launch])
loop_hybrid_testing = OperatorPOWL(operator=Operator.LOOP, children=[Prototype_Build, Hybrid_Testing, Data_Capture, Market_Sense, Scale_Plan])
loop_trend_scan = OperatorPOWL(operator=Operator.LOOP, children=[Trend_Scan, Idea_Harvest, Sector_Match, Brainstorm_Hub])

# Define exclusive choice nodes
xor_sector_match = OperatorPOWL(operator=Operator.XOR, children=[Sector_Match, skip])
xor_strategy_align = OperatorPOWL(operator=Operator.XOR, children=[Strategy_Align, skip])

# Define partial order
root = StrictPartialOrder(nodes=[loop_idea_harvest, loop_hybrid_testing, loop_trend_scan, xor_sector_match, xor_strategy_align])
root.order.add_edge(loop_idea_harvest, xor_strategy_align)
root.order.add_edge(loop_hybrid_testing, xor_strategy_align)
root.order.add_edge(loop_trend_scan, xor_strategy_align)
root.order.add_edge(xor_sector_match, loop_idea_harvest)
root.order.add_edge(xor_strategy_align, loop_hybrid_testing)
root.order.add_edge(xor_strategy_align, loop_trend_scan)