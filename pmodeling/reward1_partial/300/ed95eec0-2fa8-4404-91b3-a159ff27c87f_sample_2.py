import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names
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

# Define the root node with the specified structure
root = StrictPartialOrder(
    nodes=[Trend_Scan, Idea_Harvest, Sector_Match, Brainstorm_Hub, Concept_Filter, Prototype_Build, Hybrid_Testing,
           Stakeholder_Sync, Risk_Assess, Scenario_Map, Strategy_Align, Pilot_Launch, Data_Capture, Market_Sense,
           Scale_Plan],
    order={
        Trend_Scan: Idea_Harvest,
        Idea_Harvest: Sector_Match,
        Sector_Match: Brainstorm_Hub,
        Brainstorm_Hub: Concept_Filter,
        Concept_Filter: Prototype_Build,
        Prototype_Build: Hybrid_Testing,
        Hybrid_Testing: Stakeholder_Sync,
        Stakeholder_Sync: Risk_Assess,
        Risk_Assess: Scenario_Map,
        Scenario_Map: Strategy_Align,
        Strategy_Align: Pilot_Launch,
        Pilot_Launch: Data_Capture,
        Data_Capture: Market_Sense,
        Market_Sense: Scale_Plan
    }
)

# Print the root node
print(root)