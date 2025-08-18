import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the transitions as SilentTransitions
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[Brainstorm_Hub, Concept_Filter])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[Prototype_Build, Hybrid_Testing])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[Stakeholder_Sync, Risk_Assess])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[Scenario_Map, Strategy_Align])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[Pilot_Launch, Data_Capture])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[Market_Sense, Scale_Plan])

# Define the partial order
root = StrictPartialOrder(nodes=[Trend_Scan, Idea_Harvest, Sector_Match, loop1, loop2, loop3, loop4, loop5, loop6])
root.order.add_edge(Trend_Scan, Idea_Harvest)
root.order.add_edge(Idea_Harvest, Sector_Match)
root.order.add_edge(Sector_Match, loop1)
root.order.add_edge(loop1, Concept_Filter)
root.order.add_edge(Concept_Filter, loop2)
root.order.add_edge(Prototype_Build, Hybrid_Testing)
root.order.add_edge(Hybrid_Testing, loop3)
root.order.add_edge(Stakeholder_Sync, Risk_Assess)
root.order.add_edge(Risk_Assess, loop4)
root.order.add_edge(Scenario_Map, Strategy_Align)
root.order.add_edge(Strategy_Align, loop5)
root.order.add_edge(Pilot_Launch, Data_Capture)
root.order.add_edge(Data_Capture, loop6)
root.order.add_edge(Market_Sense, Scale_Plan)
root.order.add_edge(Scale_Plan, loop1)