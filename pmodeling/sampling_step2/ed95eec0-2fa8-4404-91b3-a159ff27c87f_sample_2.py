import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the process
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

# Create the partial order
root = StrictPartialOrder(nodes=[Trend_Scan, Idea_Harvest, Sector_Match, Brainstorm_Hub, Concept_Filter, Prototype_Build, Hybrid_Testing, Stakeholder_Sync, Risk_Assess, Scenario_Map, Strategy_Align, Pilot_Launch, Data_Capture, Market_Sense, Scale_Plan])

# Define the dependencies between the nodes
root.order.add_edge(Trend_Scan, Idea_Harvest)
root.order.add_edge(Idea_Harvest, Sector_Match)
root.order.add_edge(Sector_Match, Brainstorm_Hub)
root.order.add_edge(Brainstorm_Hub, Concept_Filter)
root.order.add_edge(Concept_Filter, Prototype_Build)
root.order.add_edge(Prototype_Build, Hybrid_Testing)
root.order.add_edge(Hybrid_Testing, Stakeholder_Sync)
root.order.add_edge(Stakeholder_Sync, Risk_Assess)
root.order.add_edge(Risk_Assess, Scenario_Map)
root.order.add_edge(Scenario_Map, Strategy_Align)
root.order.add_edge(Strategy_Align, Pilot_Launch)
root.order.add_edge(Pilot_Launch, Data_Capture)
root.order.add_edge(Data_Capture, Market_Sense)
root.order.add_edge(Market_Sense, Scale_Plan)

# Print the root to verify the model
print(root)