import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[Risk_Assess, Scenario_Map])
loop = OperatorPOWL(operator=Operator.LOOP, children=[Hybrid_Testing, Stakeholder_Sync, Strategy_Align])
partial_order = StrictPartialOrder(nodes=[Trend_Scan, Idea_Harvest, Sector_Match, Brainstorm_Hub, Concept_Filter, Prototype_Build, xor, loop, Pilot_Launch, Data_Capture, Market_Sense, Scale_Plan])
partial_order.order.add_edge(Trend_Scan, Idea_Harvest)
partial_order.order.add_edge(Idea_Harvest, Sector_Match)
partial_order.order.add_edge(Sector_Match, Brainstorm_Hub)
partial_order.order.add_edge(Brainstorm_Hub, Concept_Filter)
partial_order.order.add_edge(Concept_Filter, Prototype_Build)
partial_order.order.add_edge(Prototype_Build, xor)
partial_order.order.add_edge(xor, loop)
partial_order.order.add_edge(loop, Pilot_Launch)
partial_order.order.add_edge(Pilot_Launch, Data_Capture)
partial_order.order.add_edge(Data_Capture, Market_Sense)
partial_order.order.add_edge(Market_Sense, Scale_Plan)

# Save the final result in the variable 'root'
root = partial_order