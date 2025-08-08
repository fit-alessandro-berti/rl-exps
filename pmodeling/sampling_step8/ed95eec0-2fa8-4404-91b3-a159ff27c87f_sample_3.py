import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

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

# Define the operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[Trend_Scan, Idea_Harvest])
choice_2 = OperatorPOWL(operator=Operator.XOR, children=[Sector_Match, Brainstorm_Hub])
choice_3 = OperatorPOWL(operator=Operator.XOR, children=[Concept_Filter, Prototype_Build])
choice_4 = OperatorPOWL(operator=Operator.XOR, children=[Hybrid_Testing, Stakeholder_Sync])
choice_5 = OperatorPOWL(operator=Operator.XOR, children=[Risk_Assess, Scenario_Map])
choice_6 = OperatorPOWL(operator=Operator.XOR, children=[Strategy_Align, Pilot_Launch])
choice_7 = OperatorPOWL(operator=Operator.XOR, children=[Data_Capture, Market_Sense])
choice_8 = OperatorPOWL(operator=Operator.XOR, children=[Scale_Plan])

# Define the partial order
root.nodes = [exclusive_choice, choice_2, choice_3, choice_4, choice_5, choice_6, choice_7, choice_8]
root.order.add_edge(exclusive_choice, choice_2)
root.order.add_edge(exclusive_choice, choice_3)
root.order.add_edge(choice_2, choice_4)
root.order.add_edge(choice_2, choice_5)
root.order.add_edge(choice_3, choice_6)
root.order.add_edge(choice_3, choice_7)
root.order.add_edge(choice_4, choice_8)
root.order.add_edge(choice_5, choice_8)
root.order.add_edge(choice_6, choice_8)
root.order.add_edge(choice_7, choice_8)

# Print the final POWL model
print(root)