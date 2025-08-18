import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Trend_Scan, Idea_Harvest, Sector_Match, Brainstorm_Hub, Concept_Filter, Prototype_Build, Hybrid_Testing, Risk_Assess, Scenario_Map, Strategy_Align])
xor = OperatorPOWL(operator=Operator.XOR, children=[Stakeholder_Sync, Data_Capture, Market_Sense, Scale_Plan])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)