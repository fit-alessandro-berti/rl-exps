import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
data_capture = Transition(label='Data Capture')
trend_scan = Transition(label='Trend Scan')
idea_workshop = Transition(label='Idea Workshop')
concept_draft = Transition(label='Concept Draft')
expert_review = Transition(label='Expert Review')
prototype_build = Transition(label='Prototype Build')
regulation_check = Transition(label='Regulation Check')
ip_alignment = Transition(label='IP Alignment')
supply_sync = Transition(label='Supply Sync')
market_mapping = Transition(label='Market Mapping')
pilot_launch = Transition(label='Pilot Launch')
feedback_loop = Transition(label='Feedback Loop')
design_iterate = Transition(label='Design Iterate')
impact_measure = Transition(label='Impact Measure')
strategy_adapt = Transition(label='Strategy Adapt')

# Define the loop for the main process
main_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    data_capture,
    trend_scan,
    idea_workshop,
    concept_draft,
    expert_review,
    prototype_build,
    regulation_check,
    ip_alignment,
    supply_sync,
    market_mapping,
    pilot_launch,
    feedback_loop,
    design_iterate,
    impact_measure,
    strategy_adapt
])

# Define the XOR for the exit point
xor = OperatorPOWL(operator=Operator.XOR, children=[main_loop, SilentTransition()])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(main_loop, xor)

print(root)