import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define silent transitions (e.g., skip)
skip = SilentTransition()

# Define sub-processes
brainstorming_subprocess = OperatorPOWL(operator=Operator.XOR, children=[Sector_Match, skip])
prototype_subprocess = OperatorPOWL(operator=Operator.XOR, children=[Concept_Filter, skip])
stakeholder_sync_subprocess = OperatorPOWL(operator=Operator.XOR, children=[Prototype_Build, skip])
risk_assess_subprocess = OperatorPOWL(operator=Operator.XOR, children=[Hybrid_Testing, skip])
scenario_map_subprocess = OperatorPOWL(operator=Operator.XOR, children=[Stakeholder_Sync, skip])
strategy_align_subprocess = OperatorPOWL(operator=Operator.XOR, children=[Risk_Assess, skip])
data_capture_subprocess = OperatorPOWL(operator=Operator.XOR, children=[Scenario_Map, skip])
market_sense_subprocess = OperatorPOWL(operator=Operator.XOR, children=[Data_Capture, skip])
scale_plan_subprocess = OperatorPOWL(operator=Operator.XOR, children=[Market_Sense, skip])

# Define the main process
root = StrictPartialOrder(nodes=[
    Trend_Scan,
    Idea_Harvest,
    brainstorming_subprocess,
    prototype_subprocess,
    stakeholder_sync_subprocess,
    risk_assess_subprocess,
    scenario_map_subprocess,
    strategy_align_subprocess,
    data_capture_subprocess,
    market_sense_subprocess,
    scale_plan_subprocess
])

# Define dependencies
root.order.add_edge(Trend_Scan, Idea_Harvest)
root.order.add_edge(Idea_Harvest, brainstorming_subprocess)
root.order.add_edge(brainstorming_subprocess, prototype_subprocess)
root.order.add_edge(prototype_subprocess, stakeholder_sync_subprocess)
root.order.add_edge(stakeholder_sync_subprocess, risk_assess_subprocess)
root.order.add_edge(risk_assess_subprocess, scenario_map_subprocess)
root.order.add_edge(scenario_map_subprocess, strategy_align_subprocess)
root.order.add_edge(strategy_align_subprocess, data_capture_subprocess)
root.order.add_edge(data_capture_subprocess, market_sense_subprocess)
root.order.add_edge(market_sense_subprocess, scale_plan_subprocess)

print(root)